from selenium import webdriver
from selenium.webdriver.common.by import By

import math, time

try:
    # 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Firefox()
    browser.get(link)

    #first_window = browser.window_han

    # 2. Нажать на кнопку
    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()

    # 3. Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(1)

    # 4. Пройти капчу для робота и получить число-ответ
    x = int(browser.find_element(By.ID, "input_value").text)
    result = math.log(abs(12*math.sin(x)))
    print(f"{x=}")
    print(f"{result=}")
    input1 = browser.find_element(By.ID, "answer").send_keys(float(result))

    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

    time.sleep(15)

finally:
    browser.quit()