import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    # 1. Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Firefox()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    # 2. Нажать на кнопку
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    time.sleep(1)
    # 3. Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    # 4.На новой странице решить капчу для роботов,
    # чтобы получить число с ответом
    x = int(browser.find_element(By.ID, "input_value").text)
    result = math.log(abs(12*math.sin(x)))

    input1 = browser.find_element(By.ID, "answer").send_keys(str(result))
    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

    time.sleep(15)

finally:
    browser.quit()


