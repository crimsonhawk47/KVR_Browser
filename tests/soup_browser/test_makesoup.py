import pytest
from bs4 import BeautifulSoup
from KVR_Browser.src.bSoupBrowserClass import BSoupBrowser


@pytest.mark.static
def test_makesoup_before_any_other_functions():
    browser = BSoupBrowser()
    with pytest.raises(RuntimeError):
        assert browser.MakeSoup()
