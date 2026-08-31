from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "tools" / "validate_cpos_xml.py"

spec = importlib.util.spec_from_file_location("validate_cpos_xml", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


def validate_text(xml_text: str):
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".xml", delete=False) as tmp:
        tmp.write(xml_text)
        path = Path(tmp.name)
    try:
        return validator.validate(path)
    finally:
        path.unlink(missing_ok=True)


class CposXmlValidatorTests(unittest.TestCase):
    def test_nlm_blank_template_has_no_upload_blocking_errors(self):
        xml = """<profile>
    <identification/>
    <employment />
    <funding>
        <support>
            <projecttitle />
            <awardnumber />
            <supportsource />
            <location />
            <contributiontype>award</contributiontype>
            <awardamount />
            <inkinddescription />
            <overallobjectives />
            <potentialoverlap />
            <startdate />
            <enddate/>
            <supporttype />
            <commitment/>
        </support>
    </funding>
</profile>"""

        errors, warns = validate_text(xml)

        self.assertEqual([], errors)
        self.assertTrue(any("Missing <name>" in finding.message for finding in warns))
        self.assertTrue(any("<commitment> has no <personmonth>" in finding.message for finding in warns))

    def test_missing_contributiontype_remains_error(self):
        xml = """<profile>
    <funding>
        <support>
            <contributiontype/>
            <commitment/>
        </support>
    </funding>
</profile>"""

        errors, _warns = validate_text(xml)

        self.assertTrue(any("Missing or empty <contributiontype>" in finding.message for finding in errors))

    def test_personmonth_rejects_partial_numeric_text(self):
        xml = """<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <commitment>
                <personmonth year="2026">1abc</personmonth>
            </commitment>
        </support>
    </funding>
</profile>"""

        errors, warns = validate_text(xml)

        self.assertTrue(any("personmonth value '1abc' must be numeric" in finding.message for finding in errors))
        self.assertFalse(any("personmonth value '1abc'" in finding.message for finding in warns))

    def test_support_dates_must_be_real_calendar_dates(self):
        for invalid_date in ("2026-02-29", "2026-04-31", "2026-13-01", "0000-01-01"):
            with self.subTest(invalid_date=invalid_date):
                xml = f"""<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <startdate>{invalid_date}</startdate>
            <commitment/>
        </support>
    </funding>
</profile>"""

                errors, _warns = validate_text(xml)

                self.assertTrue(any("must be a valid calendar date" in finding.message for finding in errors))

    def test_valid_leap_day_is_accepted(self):
        xml = """<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <startdate>2028-02-29</startdate>
            <commitment/>
        </support>
    </funding>
</profile>"""

        errors, _warns = validate_text(xml)

        self.assertFalse(any("calendar date" in finding.message for finding in errors))

    def test_personmonth_rejects_values_outside_zero_through_twelve(self):
        for invalid_value in ("-0.5", "12.01"):
            with self.subTest(invalid_value=invalid_value):
                xml = f"""<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <commitment>
                <personmonth year="2026">{invalid_value}</personmonth>
            </commitment>
        </support>
    </funding>
</profile>"""

                errors, warns = validate_text(xml)

                self.assertTrue(any("outside the allowed range" in finding.message for finding in errors))
                self.assertFalse(any("personmonth value" in finding.message for finding in warns))

    def test_personmonth_rejects_more_than_two_decimal_places(self):
        xml = """<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <commitment>
                <personmonth year="2026">1.234</personmonth>
            </commitment>
        </support>
    </funding>
</profile>"""

        errors, warns = validate_text(xml)

        self.assertTrue(any("more than 2 decimal places" in finding.message for finding in errors))
        self.assertFalse(any("personmonth value" in finding.message for finding in warns))

    def test_personmonth_accepts_boundaries_and_two_decimal_places(self):
        for valid_value in ("0", "0.25", "12", "12.00"):
            with self.subTest(valid_value=valid_value):
                xml = f"""<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <commitment>
                <personmonth year="2026">{valid_value}</personmonth>
            </commitment>
        </support>
    </funding>
</profile>"""

                errors, _warns = validate_text(xml)

                self.assertFalse(any("personmonth value" in finding.message for finding in errors))

    def test_numeric_fields_reject_non_ascii_digits(self):
        xml = """<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <awardamount>١٢٥٠</awardamount>
            <startdate>٢٠٢٦-01-01</startdate>
            <commitment>
                <personmonth year="٢٠٢٦">١.٢</personmonth>
            </commitment>
        </support>
    </funding>
</profile>"""

        errors, _warns = validate_text(xml)
        messages = [finding.message for finding in errors]

        self.assertTrue(any("<awardamount> must be an integer" in message for message in messages))
        self.assertTrue(any("must be a valid calendar date" in message for message in messages))
        self.assertTrue(any("invalid year='٢٠٢٦'" in message for message in messages))
        self.assertTrue(any("personmonth value '١.٢' must be numeric" in message for message in messages))

    def test_browser_numeric_patterns_and_mirror_stay_in_sync(self):
        browser_source = (REPO_ROOT / "tools" / "index.html").read_text(encoding="utf-8")
        docs_source = (REPO_ROOT / "docs" / "tools" / "index.html").read_text(encoding="utf-8")

        self.assertEqual(browser_source, docs_source)
        self.assertIn("const DATE_RE = /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/;", browser_source)
        self.assertIn("const YEAR_RE = /^[0-9]{4}$/;", browser_source)
        self.assertIn("const INT_RE = /^[0-9]+$/;", browser_source)
        self.assertIn(
            "const PERSONMONTH_RE = /^-?(?:[0-9]+(?:\\.[0-9]+)?|\\.[0-9]+)$/;",
            browser_source,
        )

    def test_official_simple_sample_name_and_position_need_no_extra_attributes(self):
        xml = """<profile>
    <identification>
        <id idtype="orcid">0000-0002-1825-0097</id>
        <account accounttype="eRA-Commons">JDOE1</account>
        <name>
            <firstname>Jane</firstname>
            <lastname>Doe</lastname>
        </name>
    </identification>
    <employment>
        <position>
            <positiontitle>Researcher</positiontitle>
        </position>
    </employment>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <commitment/>
        </support>
    </funding>
</profile>"""

        errors, warns = validate_text(xml)

        self.assertEqual([], errors)
        self.assertFalse(any("current=\"yes\"" in finding.message for finding in warns))
        self.assertFalse(any("featured=\"true\"" in finding.message for finding in warns))

    def test_blank_personmonth_value_is_allowed_when_year_is_present(self):
        xml = """<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <commitment>
                <personmonth year="2026"/>
            </commitment>
        </support>
    </funding>
</profile>"""

        errors, _warns = validate_text(xml)

        self.assertFalse(any("personmonth" in finding.message for finding in errors))

    def test_blank_personmonth_value_still_requires_year(self):
        xml = """<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <commitment>
                <personmonth/>
            </commitment>
        </support>
    </funding>
</profile>"""

        errors, _warns = validate_text(xml)

        self.assertTrue(any("invalid year=''" in finding.message for finding in errors))

    def test_valid_unicode_punctuation_is_accepted(self):
        xml = """<?xml version="1.0" encoding="utf-8"?>
<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <overallobjectives>Smart \u201cquotes\u201d, \u2018apostrophes\u2019, en\u2013dash, em\u2014dash, bullet \u2022, and non-breaking\u00a0space.</overallobjectives>
            <commitment/>
        </support>
    </funding>
</profile>"""

        errors, warns = validate_text(xml)

        self.assertEqual([], errors)
        self.assertFalse(any("special character" in finding.message.lower() for finding in warns))

    def test_unescaped_reserved_character_remains_parse_error(self):
        xml = """<profile>
    <funding>
        <support>
            <contributiontype>award</contributiontype>
            <overallobjectives>Research & Development</overallobjectives>
            <commitment/>
        </support>
    </funding>
</profile>"""

        errors, _warns = validate_text(xml)

        self.assertTrue(any("XML not well-formed" in finding.message for finding in errors))


if __name__ == "__main__":
    unittest.main()
