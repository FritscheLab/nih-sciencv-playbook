#!/usr/bin/env python3
"""validate_cpos_xml.py

Lightweight validation for SciENcv CPOS XML (Current & Pending (Other) Support).

This is NOT a replacement for SciENcv's own validation. It aims to catch the
most common structural and formatting issues that cause upload failures or
post-upload red exclamation marks.

It supports both:
- SciENcv CPOS Data Ingest (XML upload) style (often no namespaces)
- SciENcv-exported XML that may include a default namespace

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
        tree = ET.parse(xml_path)
    except ET.ParseError as e:
        errors.append(Finding("ERROR", f"XML not well-formed: {e}"))
        return errors, warns

    root = tree.getroot()
    ns, root_local = _split_tag(root.tag)
    if root_local != "profile":
        errors.append(Finding("ERROR", f"Root element should be <profile>, found <{root_local}>."))

    # Basic structure checks
    identification = _find(root, ns, "identification")
    if identification is None:
        warns.append(Finding("WARN", "Missing <identification> block (allowed for upload, but usually present)."))
    else:
        name = _find(identification, ns, "name")
        if name is None:
            warns.append(Finding("WARN", "Missing <name> under <identification>."))

    employment = _find(root, ns, "employment")
    if employment is None:
        warns.append(Finding("WARN", "Missing <employment> block (allowed for upload, but usually present)."))

    funding = _find(root, ns, "funding")
    if funding is None:
        errors.append(Finding("ERROR", "Missing <funding> block."))
        return errors, warns

    supports = list(_findall(funding, ns, "support"))
    if not supports:
        warns.append(Finding("WARN", "No <support> entries found under <funding>."))
        return errors, warns

    for idx, sup in enumerate(supports, start=1):
        # contributiontype is required for upload per NLM guidance
        ct_el = _find(sup, ns, "contributiontype")
        ct = (ct_el.text or "").strip() if ct_el is not None else ""
        if not ct:
            errors.append(Finding("ERROR", f"support[{idx}]: <contributiontype> is empty or missing. Must be 'award' or 'inkind'."))
        elif ct not in {"award", "inkind"}:
            warns.append(Finding("WARN", f"support[{idx}]: <contributiontype> has unexpected value '{ct}'. Expected 'award' or 'inkind'."))

        st_el = _find(sup, ns, "supporttype")
        st = (st_el.text or "").strip() if st_el is not None else ""
        if st and st not in {"current", "pending", "completed"}:
            warns.append(Finding("WARN", f"support[{idx}]: <supporttype> value '{st}' is not one of current|pending|completed."))

        for date_tag in ("startdate", "enddate"):
            d_el = _find(sup, ns, date_tag)
            if d_el is None:
                continue
            d = (d_el.text or "").strip()
            if d and not DATE_RE.match(d):
                warns.append(Finding("WARN", f"support[{idx}]: <{date_tag}> value '{d}' is not YYYY-MM-DD."))

        aa_el = _find(sup, ns, "awardamount")
        aa = (aa_el.text or "").strip() if aa_el is not None else ""
        if aa and not INT_RE.match(aa):
            warns.append(Finding("WARN", f"support[{idx}]: <awardamount> should be digits only (no $ or commas). Found '{aa}'."))

        commitment = _find(sup, ns, "commitment")
        if commitment is None:
            warns.append(Finding("WARN", f"support[{idx}]: Missing <commitment> block."))
            continue

        pms = list(_findall(commitment, ns, "personmonth"))
        if not pms:
            warns.append(Finding("WARN", f"support[{idx}]: No <personmonth> entries under <commitment>."))
            continue

        for pm in pms:
            year = (pm.attrib.get("year") or "").strip()
            if not YEAR_RE.match(year):
                warns.append(Finding("WARN", f"support[{idx}]: <personmonth> has invalid year attribute '{year}'."))
            val = (pm.text or "").strip()
            if not val:
                # allowed per NLM guidance, but show as warn
                warns.append(Finding("WARN", f"support[{idx}] year {year}: <personmonth> is blank."))
                continue
            try:
                fval = float(val)
                if fval < 0:
                    warns.append(Finding("WARN", f"support[{idx}] year {year}: person-months is negative ({val})."))
                if fval > 12.0:
                    warns.append(Finding("WARN", f"support[{idx}] year {year}: person-months > 12 ({val}). Double-check."))
            except ValueError:
                warns.append(Finding("WARN", f"support[{idx}] year {year}: person-months '{val}' is not numeric."))

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
