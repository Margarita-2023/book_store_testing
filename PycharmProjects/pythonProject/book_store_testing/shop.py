########## Shop: отображение страницы товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Нажмите на вкладку "My Account"
tab_my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
tab_my_account.click()

# В разделе "Login", введите email для логина
field_username_or_email = driver.find_element_by_id("username")
field_username_or_email.send_keys("margomcalipso@yandex.ru")

# В разделе "Login", введите пароль для логина
field_login_password = driver.find_element_by_id("password")
field_login_password.send_keys("Mk068572-123")

# Нажмите на кнопку "Login"
btn_register = driver.find_element_by_css_selector(".form-row > input:nth-child(3)")
btn_register.click()

# Нажмите на вкладку "Shop"
tab_shop = driver.find_element_by_css_selector("#menu-item-40 > a")
tab_shop.click()

# Откройте книгу "HTML 5 Forms"
HTML_5_Forms = driver.find_element_by_css_selector("img[title='Mastering HTML5 Forms']")
HTML_5_Forms.click()

# Добавьте тест, что заголовок книги назвается: "HTML5 Forms" .entry-summary > h1
book_title = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".entry-summary > h1"), "HTML5 Forms"))
driver.quit()

#########  Shop: количество товаров в категории
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# # Нажмите на вкладку "My Account"
# tab_my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# tab_my_account.click()
#
# # В разделе "Login", введите email для логина
# field_username_or_email = driver.find_element_by_id("username")
# field_username_or_email.send_keys("margomcalipso@yandex.ru")
#
# # В разделе "Login", введите пароль для логина
# field_login_password = driver.find_element_by_id("password")
# field_login_password.send_keys("Mk068572-123")
#
# # Нажмите на кнопку "Login"
# btn_register = driver.find_element_by_css_selector(".form-row > input:nth-child(3)")
# btn_register.click()
#
# # Нажмите на вкладку "Shop"
# tab_shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# tab_shop.click()
#
# # Откройте категорию "HTML"
# tab_HTML = driver.find_element_by_css_selector(".cat-item-19 > a")
# tab_HTML.click()
#
# # Добавьте тест, что отображается три товара
# time.sleep(5)
# items_count = driver.find_elements_by_css_selector("a > h3")
# if len(items_count) == 3:
#     print("На странице 3 товара")
# else:
#     print("Ошибка. На странице: " + str(len(items_count)))
# driver.quit()
#
# ###########  Shop: сортировка товаров
# from selenium import webdriver
# from selenium.webdriver.support import select
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# # Нажмите на вкладку "My Account"
# tab_my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# tab_my_account.click()
#
# # В разделе "Login", введите email для логина
# field_username_or_email = driver.find_element_by_id("username")
# field_username_or_email.send_keys("margomcalipso@yandex.ru")
#
# # В разделе "Login", введите пароль для логина
# field_login_password = driver.find_element_by_id("password")
# field_login_password.send_keys("Mk068572-123")
#
# # Нажмите на кнопку "Login"
# btn_register = driver.find_element_by_css_selector(".form-row > input:nth-child(3)")
# btn_register.click()
#
# # Нажмите на вкладку "Shop"
# tab_shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# tab_shop.click()
#
# # Проверка сортировки по умолчанию
# field_selector = driver.find_element_by_class_name("orderby")
# select.Select(field_selector).select_by_index(0)
#
# # Отсортируйте товары по цене от большей к меньшей
# field_selector = driver.find_element_by_class_name("orderby").click()
# field_selector = driver.find_element_by_css_selector("option:nth-child(6)").click()
#
# # Основной селектор сортировки
# field_selector = driver.find_element_by_class_name("orderby")
# select.Select(field_selector).select_by_index(0)
#
# # Проверка сортировки по цене от большей к меньшей
# field_selector = driver.find_element_by_class_name("orderby")
# select.Select(field_selector).select_by_index(5)
# driver.quit()
#
# ############ Shop: отображение, скидка товара
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# # Нажмите на вкладку "My Account"
# tab_my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# tab_my_account.click()
#
# # В разделе "Login", введите email для логина
# field_username_or_email = driver.find_element_by_id("username")
# field_Username_or_email.send_keys("margomcalipso@yandex.ru")
#
# # В разделе "Login", введите пароль для логина
# field_login_password = driver.find_element_by_id("password")
# field_login_password.send_keys("Mk068572-123")
#
# # Нажмите на кнопку "Login"
# btn_register = driver.find_element_by_css_selector(".form-row > input:nth-child(3)")
# btn_register.click()
#
# # Нажмите на вкладку "Shop"
# tab_shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# tab_shop.click()
#
# # Откройте книгу "Android Quick Start Guide"
# android_quick_start_guide = driver.find_element_by_css_selector(".post-169 h3")
# android_quick_start_guide.click()
#
# # Получение значения новой и старой цены
# book_old_price = driver.find_element_by_css_selector(".price > del > span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# book_new_price_text = book_new_price.text
#
# # Проверка значения цен
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
#
# # Нажмите на обложку книги
# book_cover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
#
# # Закройте предпросмотр нажав на крестик
# book_cover_close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# book_cover_close.click()
# driver.quit()
#
# ###########  Shop: проверка цены в корзине
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# # Нажмите на вкладку "Shop"
# tab_shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# tab_shop.click()
#
# # Добавьте в корзину книгу "HTML5 WebApp Development"
# add_to_basket = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(5)
#
# # Получение значения количества и стоимости товара
# book_number_basket = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
# book_number_basket_text = book_number_basket.text
# book_price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# book_price_text = book_price.text
# time.sleep(5)
#
# # Проверка количества и стоимости товара
# assert book_number_basket_text == "1 Item"
# assert book_price_text == "₹180.00"
#
# # Перейдите в корзину
# basket_books = driver.find_element_by_css_selector("[title='View your shopping cart']")
# basket_books.click()
#
# # Проверка стоимости в Subtotal
# subtotal_field_text = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal"), "180.00"))
#
# # Проверка стоимости в Total
# total_field_text = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CLASS_NAME, "order-total"), "183.60"))
# driver.quit()
#
# ########### Shop: работа в корзине
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# # Нажмите на вкладку "Shop"
# tab_shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# tab_shop.click()
#
# # Проскролльте страницу вниз на 300 пикселей
# driver.execute_script("window.scrollBy(0, 300);")
#
# # Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# HTML5_webApp_basket = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(5)
# js_data_structures_basket = driver.find_element_by_css_selector("[data-product_id='180']").click()
# time.sleep(5)
#
# # Перейдите в корзину
# basket_books = driver.find_element_by_css_selector("[title='View your shopping cart']")
# basket_books.click()
# time.sleep(5)
#
# # Удалите первую книгу
# btn_delete = driver.find_element_by_css_selector("[data-product_id='182']")
# btn_delete.click()
# time.sleep(5)
#
# # Нажмите на Undo
# btn_undo = driver.find_element_by_css_selector(".woocommerce-message > a")
# btn_undo.click()
# time.sleep(5)
#
# # Увеличить количесто товара до 3 шт для "JS Data Structures and Algorithm“
# field_quantity = driver.find_element_by_css_selector("[title='Qty']").clear()
# time.sleep(3)
# field_quantity = driver.find_element_by_css_selector(".quantity input")
# field_quantity.send_keys("3")
# time.sleep(5)
#
# # Нажмите на кнопку "UPDATE BASKET"
# btn_update_basket = driver.find_element_by_css_selector(".actions [name='update_cart']")
# btn_update_basket.click()
# time.sleep(5)
#
# # Проверка количества "JS Data Structures and Algorithm" равно 3
# field_quantity = driver.find_element(by=By.CSS_SELECTOR, value="[title='Qty']")
# field_quantity_text = field_quantity.get_attribute("value")
# assert field_quantity_text == "3"
# time.sleep(5)
#
# # Нажмите на кнопку "APPLY COUPON"
# btn_apply_coupon = driver.find_element_by_css_selector(".coupon [name='apply_coupon']")
# btn_apply_coupon.click()
# time.sleep(5)
#
# # Проверка сообщения: "Please enter a coupon code."
# message_text = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By. CSS_SELECTOR, ".woocommerce-error > li"), "Please enter a coupon code."))
# driver.quit()
#
# #########  Shop: покупка товара
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# # Нажмите на вкладку "Shop" и проскролльте вниз на 300 пикселей
# tab_shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# tab_shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
#
# # Добавьте в корзину книгу "HTML5 WebApp Development"
# add_to_basket = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(5)
#
# # Перейдите в корзину
# basket_books = driver.find_element_by_css_selector("[title='View your shopping cart']")
# basket_books.click()
# time.sleep(5)
#
# # Нажмите "PROCEED TO CHECKOUT" + явное ожидание
# btn_proceed_to_checkout = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout > a")))
# btn_proceed_to_checkout.click()
#
# # Заполните все обязательные поля
# field_first_name = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "billing_first_name")))
# field_first_name.send_keys("Margarita")
# field_last_name = driver.find_element(value="billing_last_name")
# field_last_name.send_keys("Denisova")
# field_email = driver.find_element(value="billing_email")
# field_email.send_keys("margomcalipso@yandex.ru")
# field_phone = driver.find_element(value="billing_phone")
# field_phone.send_keys("9107536035")
# country_selector = driver.find_element(value="s2id_billing_country").click()
# field_country = driver.find_element(value="s2id_autogen1_search")
# field_country.send_keys("Russia")
# title_country = driver.find_element(value="select2-results-1").click()
# field_address = driver.find_element_by_css_selector("[name='billing_address_1']")
# field_address.send_keys("Ryazan, st. Kasimovskoe sh.")
# field_address = driver.find_element_by_css_selector("[name='billing_address_2']")
# field_address.send_keys("13")
# field_city = driver.find_element_by_css_selector("[name='billing_city']")
# field_city.send_keys("Ryazan")
# field_country = driver.find_element_by_css_selector("[name='billing_state']")
# field_country.send_keys("Russia")
# field_postcode = driver.find_element_by_css_selector("[name='billing_postcode']")
# field_postcode.send_keys("390000")
# time.sleep(3)
#
# # Проскролльте страницу вниз на 600 пикселей
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(5)
# # Выберите способ оплаты "Check Payments"  #payment_method_cheque
# check_payments = driver.find_element(value="payment_method_cheque").click()
#
# # Нажмите PLACE ORDER
# btn_place_order = driver.find_element(value="place_order")
# btn_place_order.click()
# time.sleep(5)
#
# # Проверка надписи: "Thank you. Your order has been received."
# message_text = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),
#     "Thank you. Your order has been received."))
#
# # В Payment Method отображается текст "Check Payments"
# payment_method_text = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CLASS_NAME, "method"),
#     "Check Payments"))
# driver.quit()
