##########  Home: добавление комментария
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")

# Нажмите на название книги "Selenium Ruby"
btn_selenium_ruby = driver.find_element_by_css_selector("img[title='Selenium Ruby']")
btn_selenium_ruby.click()

# Нажмите на вкладку "REVIEWS"
tab_reviews = driver.find_element_by_css_selector(".reviews_tab a")
tab_reviews.click()

# Поставьте 5 звёзд
your_rating = driver.find_element_by_class_name("star-5")
your_rating.click()

# Заполните поле "Review" сообщением: "Nice book!"
your_rating = driver.find_element_by_id("comment")
your_rating.send_keys("Nice book!")

# Заполните поле "Name"
field_name = driver.find_element_by_id("author")
field_name.send_keys("Margarita")

# Заполните "Email"
field_email = driver.find_element_by_id("email")
field_email.send_keys("margomcalipso@yandex.ru")

# Нажмите на кнопку "SUBMIT"
btn_submit = driver.find_element_by_css_selector(".form-submit .submit")
btn_submit.click()
driver.quit()