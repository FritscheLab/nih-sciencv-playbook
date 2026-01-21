#!/usr/bin/env python3
"""validate_cpos_xml.py

Lightweight validation for SciENcv CPOS XML (Current & Pending (Other) Support).

This is NOT a replacement for SciENcv's own validation. It aims to catch the
most common structural and formatting issues that cause upload failures or
post-upload red exclamation marks.

This targets the SciENcv CPOS Data Ingest (XML upload) simple template
(bare <profile>, no namespaces or profile attributes) and aligns with the
browser validator in tools/index.html.

Usage:
  python tools/validate_cpos_xml.py path/to/file.xml

Exit codes:
  0 = no errors
  1 = errors found
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional, Tuple
import xml.etree.ElementTree as ET

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
YEAR_RE = re.compile(r"^\d{4}$")
INT_RE = re.compile(r"^\d+$")
SUSPICIOUS_RE = re.compile(r"[\u201C\u201D\u2018\u2019\u2013\u2014\u2022\u00A0]")

LIMITS = {
    "awardamount_digits": 13,
    "awardnumber": 50,
    "supportsource": 60,
    "location": 60,
    "projecttitle": 300,
    "inkinddescription": 500,
    "overallobjectives": 1500,
    "potentialoverlap": 5000,
}

SUPPORT_ORDER = [
    "projecttitle",
    "awardnumber",
    "supportsource",
    "location",
    "contributiontype",
    "awardamount",
    "inkinddescription",
    "overallobjectives",
    "potentialoverlap",
    "startdate",
    "enddate",
    "supporttype",
    "commitment",
]


@dataclass
class Finding:
    level: str  # ERROR | WARN
    message: str


def _split_tag(tag: str) -> Tuple[Optional[str], str]:
    """Return (namespace, localname) for an ElementTree tag."""
    if tag.startswith("{") and "}" in tag:
        ns, local = tag[1:].split("}", 1)
        return ns, local
    return None, tag


def _qname(ns: Optional[str], local: str) -> str:
    return f"{{{ns}}}{local}" if ns else local


def _local_name(tag: str) -> str:
    return _split_tag(tag)[1]


def _get_text(el: Optional[ET.Element]) -> str:
    if el is None or el.text is None:
        return ""
    return el.text.strip()


def _attr_name(attr: str) -> str:
    if attr.startswith("{") and "}" in attr:
        return attr.split("}", 1)[1]
    return attr


def _find(parent: ET.Element, ns: Optional[str], path: str) -> Optional[ET.Element]:
    # ElementTree's limited XPath: supports tag/tag.
    # We map each segment to a namespaced tag when needed.
    cur = parent
    for seg in path.strip("/").split("/"):
        child = cur.find(_qname(ns, seg))
        if child is None:
            return None
        cur = child
    return cur


def _findall(parent: ET.Element, ns: Optional[str], tag: str) -> Iterable[ET.Element]:
    return parent.findall(_qname(ns, tag))


def validate(xml_path: Path) -> Tuple[list[Finding], list[Finding]]:
    errors: list[Finding] = []
    warns: list[Finding] = []

    try:
        xml_text = xml_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        xml_text = xml_path.read_bytes().decode("utf-8", errors="replace")

    leading = xml_text.lstrip("\ufeff").lstrip()
    if not leading.startswith("<?xml"):
        warns.append(Finding("WARN", "Missing XML declaration (<?xml version=\"1.0\" encoding=\"utf-8\"?>). Fix: add it at the top (recommended)."))

    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        errors.append(Finding("ERROR", f"XML not well-formed or could not be parsed: {e}. Fix: ensure tags are properly closed and reserved characters are escaped (e.g., & => &amp;)."))
        return errors, warns

    ns, root_local = _split_tag(root.tag)
    if root_local != "profile":
        errors.append(Finding("ERROR", f"Root element must be <profile>. Found <{root_local}>."))
        return errors, warns

    # Root attributes / namespaces (UPLOAD template expects none)
    root_attrs = list(root.attrib.keys())
    if root_attrs or ns:
        attrs = ", ".join(_attr_name(a) for a in root_attrs)
        msg = "Root <profile> must NOT have any attributes in upload mode (no xmlns, doctype, schemaLocation, accession). Fix: use a bare <profile> tag with no attributes."
        if attrs:
            msg += f" Found attributes: {attrs}."
        if ns:
            msg += f" Found namespace: {ns}."
        errors.append(Finding("ERROR", msg))

    # Basic child order under profile
    child_names = [_local_name(child.tag) for child in list(root)]
    allowed_top = ["identification", "employment", "funding"]
    for name in child_names:
        if name not in allowed_top:
            warns.append(Finding("WARN", f"Unexpected top-level element <{name}> under <profile>. Fix: remove it or ensure SciENcv upload supports it."))

    idx_id = child_names.index("identification") if "identification" in child_names else -1
    idx_emp = child_names.index("employment") if "employment" in child_names else -1
    idx_fund = child_names.index("funding") if "funding" in child_names else -1

    if idx_fund == -1:
        errors.append(Finding("ERROR", "Missing <funding> block. Fix: add <funding> with one or more <support> entries."))
        return errors, warns

    if idx_id == -1:
        warns.append(Finding("WARN", "Missing <identification> block. Fix: include <identification> with <id>, <account>, and <name current=\"yes\">."))

    if idx_emp == -1:
        warns.append(Finding("WARN", "Missing <employment> block. Fix: include <employment> with at least one <position>."))

    def _in_order(a: int, b: int) -> bool:
        if a == -1 or b == -1:
            return True
        return a < b

    if not _in_order(idx_id, idx_emp) or not _in_order(idx_emp, idx_fund) or not _in_order(idx_id, idx_fund):
        errors.append(Finding("ERROR", "Incorrect element order under <profile>. Fix: order must be <identification>, then <employment>, then <funding>."))

    # Identification checks (recommended but common failure cause)
    identification = _find(root, ns, "identification")
    if identification is not None:
        id_el = _find(identification, ns, "id")
        acct_el = _find(identification, ns, "account")
        name_el = _find(identification, ns, "name")

        if id_el is None:
            warns.append(Finding("WARN", "Missing <id> in <identification>. Fix: add <id idtype=\"orcid\">0000-0000-0000-0000</id> (value may be blank)."))
        else:
            idtype = (id_el.attrib.get("idtype") or "").strip()
            if not idtype:
                warns.append(Finding("WARN", "<id> is missing idtype attribute. Fix: <id idtype=\"orcid\">...</id>."))

        if acct_el is None:
            warns.append(Finding("WARN", "Missing <account> in <identification>. Fix: add <account accounttype=\"eRA-Commons\">...</account> (value may be blank)."))
        else:
            acct_type = (acct_el.attrib.get("accounttype") or "").strip()
            if not acct_type:
                warns.append(Finding("WARN", "<account> is missing accounttype attribute. Fix: <account accounttype=\"eRA-Commons\">...</account>."))

        if name_el is None:
            errors.append(Finding("ERROR", "Missing <name> in <identification>. Fix: add <name current=\"yes\"> with <firstname>, <middlename/>, <lastname>."))
        else:
            cur = (name_el.attrib.get("current") or "").strip()
            if cur != "yes":
                warns.append(Finding("WARN", "<name> should include current=\"yes\" (recommended). Fix: <name current=\"yes\">..."))

            fn = _find(name_el, ns, "firstname")
            ln = _find(name_el, ns, "lastname")
            if fn is None or not _get_text(fn):
                warns.append(Finding("WARN", "<firstname> is missing or blank. Fix: provide a first name (or leave blank if intentionally omitted)."))
            if ln is None or not _get_text(ln):
                warns.append(Finding("WARN", "<lastname> is missing or blank. Fix: provide a last name (or leave blank if intentionally omitted)."))

    # Employment checks (years must not be empty)
    employment = _find(root, ns, "employment")
    if employment is not None:
        positions = list(_findall(employment, ns, "position"))
        if not positions:
            warns.append(Finding("WARN", "No <position> found under <employment>. Fix: add <position featured=\"true\" current=\"no\">..."))
        else:
            for p_idx, pos in enumerate(positions, start=1):
                for tag in ("startdate", "enddate"):
                    date_el = _find(pos, ns, tag)
                    if date_el is None:
                        continue
                    year_el = _find(date_el, ns, "year")
                    if year_el is None:
                        errors.append(Finding("ERROR", f"employment position[{p_idx}]: <{tag}> is missing <year>. Fix: use <{tag}><year>YYYY</year></{tag}> or omit <{tag}> entirely."))
                        continue
                    year_val = _get_text(year_el)
                    if not YEAR_RE.match(year_val):
                        errors.append(Finding("ERROR", f"employment position[{p_idx}]: <{tag}><year> must be YYYY and not blank. Found '{year_val}'. Fix: provide a 4-digit year or omit the entire <{tag}> block."))

    # Funding/support checks
    funding = _find(root, ns, "funding")
    if funding is None:
        errors.append(Finding("ERROR", "Missing <funding> block. Fix: add <funding> with one or more <support> entries."))
        return errors, warns

    supports = list(_findall(funding, ns, "support"))
    if not supports:
        warns.append(Finding("WARN", "No <support> entries found under <funding>. Fix: add at least one <support> block."))
        return errors, warns

    for idx, sup in enumerate(supports, start=1):
        # Validate support child order
        last_pos = -1
        for child in list(sup):
            child_name = _local_name(child.tag)
            try:
                pos = SUPPORT_ORDER.index(child_name)
            except ValueError:
                warns.append(Finding("WARN", f"support[{idx}]: Unexpected element <{child_name}> inside <support>. Fix: remove it or ensure SciENcv upload supports it."))
                continue
            if pos < last_pos:
                errors.append(Finding("ERROR", f"support[{idx}]: Incorrect element order. Fix: child elements must follow: {', '.join(SUPPORT_ORDER)}."))
            last_pos = max(last_pos, pos)

        # contributiontype required
        ct_el = _find(sup, ns, "contributiontype")
        ct = _get_text(ct_el)
        if ct_el is None or not ct:
            errors.append(Finding("ERROR", f"support[{idx}]: Missing or empty <contributiontype>. Fix: set to 'award' or 'inkind'."))
        elif ct not in {"award", "inkind"}:
            errors.append(Finding("ERROR", f"support[{idx}]: <contributiontype> must be 'award' or 'inkind'. Found '{ct}'. Fix: change it to 'award' or 'inkind'."))

        # supporttype allowed values
        st_el = _find(sup, ns, "supporttype")
        st = _get_text(st_el)
        if st_el is not None and st and st not in {"current", "pending"}:
            errors.append(Finding("ERROR", f"support[{idx}]: <supporttype> must be 'current' or 'pending'. Found '{st}'. Fix: change to 'current' or 'pending'."))

        # Dates: startdate/enddate format
        for tag in ("startdate", "enddate"):
            d_el = _find(sup, ns, tag)
            if d_el is None:
                continue
            d = _get_text(d_el)
            if d and not DATE_RE.match(d):
                errors.append(Finding("ERROR", f"support[{idx}]: <{tag}> must be YYYY-MM-DD. Found '{d}'. Fix: convert to YYYY-MM-DD or omit <{tag}> if unknown."))

        # awardamount digits-only + <=13 digits
        aa_el = _find(sup, ns, "awardamount")
        aa = _get_text(aa_el)
        if aa:
            if not INT_RE.match(aa):
                errors.append(Finding("ERROR", f"support[{idx}]: <awardamount> must be an integer (digits only). Found '{aa}'. Fix: remove $ signs, commas, decimals."))
            elif len(aa) > LIMITS["awardamount_digits"]:
                errors.append(Finding("ERROR", f"support[{idx}]: <awardamount> has {len(aa)} digits (max {LIMITS['awardamount_digits']}). Fix: shorten to <=13 digits or leave blank if unknown."))

        # Length limits
        length_checks = [
            ("awardnumber", LIMITS["awardnumber"]),
            ("supportsource", LIMITS["supportsource"]),
            ("location", LIMITS["location"]),
            ("projecttitle", LIMITS["projecttitle"]),
            ("inkinddescription", LIMITS["inkinddescription"]),
            ("overallobjectives", LIMITS["overallobjectives"]),
            ("potentialoverlap", LIMITS["potentialoverlap"]),
        ]
        for tag, max_len in length_checks:
            el = _find(sup, ns, tag)
            txt = _get_text(el)
            if txt and len(txt) > max_len:
                errors.append(Finding("ERROR", f"support[{idx}]: <{tag}> is {len(txt)} chars (max {max_len}). Fix: shorten <{tag}> to <= {max_len} characters."))

        # In-kind special rules
        if ct == "inkind":
            pt_el = _find(sup, ns, "projecttitle")
            loc_el = _find(sup, ns, "location")
            end_el = _find(sup, ns, "enddate")

            if pt_el is not None and _get_text(pt_el):
                errors.append(Finding("ERROR", f"support[{idx}]: In-kind <projecttitle> must be empty. Fix: move this text to <inkinddescription> and make <projecttitle/> empty."))
            if loc_el is not None and _get_text(loc_el):
                errors.append(Finding("ERROR", f"support[{idx}]: In-kind <location> must be empty. Fix: move this text to <inkinddescription> and make <location/> empty."))
            if end_el is not None:
                warns.append(Finding("WARN", f"support[{idx}]: In-kind entry includes <enddate>. Many working templates omit in-kind end dates. Fix: remove <enddate> for in-kind if SciENcv upload fails."))

        # commitment required
        commitment = _find(sup, ns, "commitment")
        if commitment is None:
            errors.append(Finding("ERROR", f"support[{idx}]: Missing <commitment>. Fix: add <commitment> with one or more <personmonth year=\"YYYY\">...</personmonth>."))
        else:
            pms = list(_findall(commitment, ns, "personmonth"))
            if not pms:
                errors.append(Finding("ERROR", f"support[{idx}]: <commitment> has no <personmonth> entries. Fix: add at least one <personmonth year=\"YYYY\">...</personmonth>."))
            for pm in pms:
                year = (pm.attrib.get("year") or "").strip()
                if not YEAR_RE.match(year):
                    errors.append(Finding("ERROR", f"support[{idx}]: <personmonth> has invalid year='{year}'. Fix: year must be a 4-digit YYYY."))
                val = (pm.text or "").strip()
                if val:
                    try:
                        fval = float(val)
                    except ValueError:
                        warns.append(Finding("WARN", f"support[{idx}] year {year}: personmonth value '{val}' is not numeric. Fix: use a number (e.g., 0.5, 1, 12)."))
                    else:
                        if fval < 0:
                            warns.append(Finding("WARN", f"support[{idx}] year {year}: personmonth is negative ({val}). Fix: use 0 or a positive value."))
                        if fval > 12:
                            warns.append(Finding("WARN", f"support[{idx}] year {year}: personmonth > 12 ({val}). Fix: verify (calendar months/year is usually <= 12)."))

    if SUSPICIOUS_RE.search(xml_text):
        warns.append(Finding("WARN", "Found smart quotes, en/em dashes, bullets, or non-breaking spaces. Fix: normalize special characters before upload."))

    return errors, warns


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] in {"-h", "--help"}:
        print(__doc__.strip())
        return 0 if argv[1:] and argv[1] in {"-h", "--help"} else 1

    xml_path = Path(argv[1])
    if not xml_path.exists():
        print(f"ERROR: file not found: {xml_path}")
        return 1

    errors, warns = validate(xml_path)

    for f in errors:
        print(f"{f.level}: {f.message}")
    for f in warns:
        print(f"{f.level}: {f.message}")

    if errors:
        print(f"\nFAIL: {len(errors)} error(s), {len(warns)} warning(s)")
        return 1

    print(f"\nOK: 0 errors, {len(warns)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
