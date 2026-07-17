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

        _errors, warns = validate_text(xml)

        self.assertTrue(any("personmonth value '1abc' is not numeric" in finding.message for finding in warns))

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
