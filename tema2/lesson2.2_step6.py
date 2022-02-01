import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Firefox()

    # 1. Открыть страницу http://SunInJuly.github.io/execute_script.html.
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    # 2. Считать значение для переменной x.
    x = int(browser.find_element(By.ID, "input_value").text)

    # 3. Посчитать математическую функцию от x.
    x = math.log(abs(12 * math.sin(x)))

    # 4. Проскроллить страницу вниз.
    browser.execute_script("window.scrollBy(0,100)")

    # 5. Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer").send_keys(str(x))

    # 6. Выбрать checkbox "I'm the robot".
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox").click()

    # 7. Переключить radiobutton "Robots rule!".
    robot_radio = browser.find_element(By.ID, "robotsRule").click()

    # 8. Нажать на кнопку "Submit".
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    time.sleep(15)

finally:
    browser.quit()