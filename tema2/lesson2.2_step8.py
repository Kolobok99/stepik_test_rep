import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Firefox()

    # 1.Открыть страницу http://suninjuly.github.io/file_input.html
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    # 2. Заполнить текстовые поля: имя, фамилия, email
    name_input = browser.find_element(By.CSS_SELECTOR, "[placeholder*='first']").send_keys("Ivan")

    last_name_input = browser.find_element(By.CSS_SELECTOR, "[placeholder*='last'").send_keys("Petrov")

    email_input = browser.find_element(By.CSS_SELECTOR, "[placeholder*='email'").send_keys("mail@mail.ru")

    # 3. Загрузить файл.
    # Файл должен иметь расширение .txt и может быть пустым

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(current_dir, '../number.txt')
    file_input = browser.find_element(By.ID, "file").send_keys(file)

    #time.sleep(5)

    # 4. Нажать кнопку "Submit"

    submit_but = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

    time.sleep(15)

finally:
        browser.quit()