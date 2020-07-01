from src.bSoupBrowserClass import BSoupBrowser
import pytest

def test_selectbycss_with_no_file_or_response():
    browser = BSoupBrowser()
    with pytest.raises(RuntimeError):
        cssPath = ".topics .topictitle"
        assert browser.SelectByCss(cssPath)