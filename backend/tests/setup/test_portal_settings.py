"""Portal settings tests."""
from plone import api

import pytest


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["plone.site_title", "Intranet do TRE-PI"],
            ["plone.email_from_name", "Intranet do TRE-PI"],
            ["plone.email_from_address", "intranet@tre-pi.jus.br"],
            ["plone.smtp_host", "localhost"],
            ["plone.smtp_port", 25],
            ["plone.portal_timezone", "America/Sao_Paulo"],
            ["plone.navigation_depth", 4],                  
        ],
    )
    # def test_portal_title(self, portal):
    #     """Test portal title."""
    #     value = api.portal.get_registry_record("plone.site_title")
    #     expected = "Intranet do TRE-PI"
    #     assert value == expected

    def test_setting(self, portal, key: str, expected: str | int):
        """Test registry setting."""
        value = api.portal.get_registry_record(key)
        assert value == expected