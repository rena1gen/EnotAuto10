import time

from pages.ConnectionSitePage import SiteConnectionPage


def test_connection_site(browser, auth_process):
    sc = SiteConnectionPage(browser, "https://cabinet.enot.io/connection-site")
    sc.open()
    time.sleep(2)
