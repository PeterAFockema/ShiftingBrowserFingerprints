import pytest
import unittest
from unittest.mock import MagicMock, patch

from shiftingbrowserfingerprints.firefox_scrapers import FirefoxScrapers as Scrapers

@pytest.fixture
def instance():
    return Scrapers()

def test_firefox_driver_valid_extension_list(instance):
    
    with patch("shiftingbrowserfingerprints.firefox_scrapers.os.path") as mock_path, \
         patch("shiftingbrowserfingerprints.firefox_scrapers.webdriver.Firefox") as mock_firefox, \
         patch("shiftingbrowserfingerprints.firefox_scrapers.OptionsFirefox") as mock_options:

        mock_path.dirname.return_value = "/mock/dir"
        mock_path.abspath.return_value = "/mock/dir"
        
        mock_driver_instance = MagicMock()
        mock_firefox.return_value = mock_driver_instance
        
        mock_options_instance = mock_options.return_value

        choices = ["audio", "battery"]

        result_driver = instance.firefox_driver_extension_list_implementation(choices)

        mock_options_instance.set_preference.assert_any_call("extensions.webextensions.restrictedDomains", "")
        mock_options_instance.set_preference.assert_any_call("extensions.experiments.enabled", True)
        mock_options_instance.set_preference.assert_any_call("xpinstall.signatures.required", False)
        assert mock_options_instance.accept_insecure_certs is True

        mock_firefox.assert_called_once_with(options=mock_options_instance)

        mock_driver_instance.install_addon.assert_any_call(
            "/mock/dir/__assets__/extensions/aud_ff/web-ext-artifacts/aud_ff.xpi", temporary=True
        )
        mock_driver_instance.install_addon.assert_any_call(
            "/mock/dir/__assets__/extensions/batt_ff/web-ext-artifacts/batt_ff.xpi", temporary=True
        )
        
        assert mock_driver_instance.install_addon.call_count == 2
        assert result_driver == mock_driver_instance


def test_firefox_driver_extension_with_empty_list(instance):

    with patch("shiftingbrowserfingerprints.firefox_scrapers.os.path") as mock_path, \
        patch("shiftingbrowserfingerprints.firefox_scrapers.webdriver.Firefox") as mock_firefox, \
        patch("shiftingbrowserfingerprints.firefox_scrapers.OptionsFirefox") as mock_options:
    
        mock_driver_instance = MagicMock()
        mock_firefox.return_value = mock_driver_instance

        result_driver = instance.firefox_driver_extension_list_implementation([])

        mock_driver_instance.install_addon.assert_not_called()
        assert result_driver == mock_driver_instance

if __name__ == '__main__':
    unittest.main()