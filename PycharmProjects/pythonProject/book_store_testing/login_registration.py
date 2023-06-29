########  Registration_login: регистрация аккаунта
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Нажмите на вкладку "My Account"
tab_my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
tab_my_account.click()

# В разделе "Register", введите email для регистрации
field_email_address = driver.find_element_by_id("reg_email")
field_email_address.send_keys("margomcalipso@yandex.ru")

# В разделе "Register", введите пароль для регистрации
field_password = driver.find_element_by_id("reg_password")
field_password.send_keys("Mk068572-123")

# Нажмите на кнопку "Register"
btn_register = driver.find_element_by_css_selector(".woocomerce-FormRow .woocommerce-Button")
btn_register.click()
driver.quit()

############   Registration_login: логин в систему
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
# # Добавьте проверку, что на странице есть элемент "Logout"
# window_my_account = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation li:nth-child(6) > a"), "Logout"))
# driver.quit()
