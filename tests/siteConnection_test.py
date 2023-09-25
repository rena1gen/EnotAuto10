import time

from pages.ConnectionSitePage import SiteConnectionPage


def test_connection_site(browser, auth_process):
    sc = SiteConnectionPage(browser, "https://cabinet.enot.io/connection-site")
    sc.open()
    time.sleep(2)
    sc.fill_site_connection_inputs("КЕйсы кс го", "lrеееv.ru", "луший сайт по кейсам кс го в инете")
    time.sleep(2)
    title = sc.get_page_title()
    assert title == "Подтвердите, что вы владелец сайта"
    print("Test case is passed")

