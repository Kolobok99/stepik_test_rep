import time

from selenium import webdriver
import math

from selenium.webdriver.common.by import By

try:
    # 0. Запустить Browser
    browser = webdriver.Firefox()

    # 1.Открыть страницу http://suninjuly.github.io/math.html.
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    # 2.Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    #print(f"{x=}")

    # 3.Посчитать математическую функцию от x
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    # 4.Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # 5.Отметить checkbox "I'm the robot".
    check_box_robot = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check_box_robot.click()

    # 6.Выбрать radiobutton "Robots rule!".
    radio_robot = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio_robot.click()

    # 7.Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
    time.sleep(15)

finally:
    browser.quit()