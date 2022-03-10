from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_product_page()  # выполняем проверки
    page.add_to_busket()          # выполняем метод страницы — добавляем в корзину
    page.solve_quiz_and_get_code()
# pytest -s -v --language=en test_product_page.py
# опция PyTest --tb=line указывает, что нужно выводить только одну строку из лога каждого упавшего теста
