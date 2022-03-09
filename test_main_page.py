import time

def test_guest_can_go_to_login_page(browser): # pytest -v --tb=line --language=en Crosslanguage/test_main_page.py
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
    time.sleep(5)
    # опция PyTest --tb=line указывает, что нужно выводить только одну строку из лога каждого упавшего теста