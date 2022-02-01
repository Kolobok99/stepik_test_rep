import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # 2. Дождаться, когда цена дома уменьшится до $100
    # (ожидание нужно установить не меньше 12 секунд)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    # 3. Нажать на кнопку "Book"
    button = browser.find_element(By.ID, 'book').click()


    # 4. Решить уже известную нам математическую задачу
    # (используйте ранее написанный код) и отправить решение
    x = int(browser.find_element(By.ID, 'input_value').text)
    print(f"{x=}")

    result = math.log(abs(12*math.sin(x)))

    print(f"{result=}")
    answer = browser.find_element(By.ID, "answer").send_keys(float(result))
    submit_but = browser.find_element(By.ID, "solve").click()

    time.sleep(15)

finally:
    browser.quit()