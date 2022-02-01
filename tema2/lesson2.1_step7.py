import time

from selenium import webdriver
import math
from selenium.webdriver.common.by import By

try:

    browser = webdriver.Firefox()

    # 1.Открыть страницу http://suninjuly.github.io/get_attribute.html.
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    # 2.Найти на ней элемент-картинку,
    # который является изображением сундука с сокровищами.
    image = browser.find_element(By.ID, "treasure")

    # 3.Взять у этого элемента значение атрибута valuex,
    # которое является значением x для задачи.
    image_valuex = image.get_attribute("valuex")

    # 4.Посчитать математическую функцию от x

    x = int(image_valuex)
    print(f'{x=}')
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    # 5.Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    #time.sleep(2)
    # 6.Отметить checkbox "I'm the robot".
    checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
    checkbox_robot.click()
    #time.sleep(2)

    # 7.Выбрать radiobutton "Robots rule!".
    radio_robot = browser.find_element(By.ID, "robotsRule")
    radio_robot.click()
    #time.sleep(2)

    # 8.Нажать на кнопку "Submit".

    submit_button = browser.find_element(By.CLASS_NAME, ".btn.btn-default")
    submit_button.click()
    time.sleep(15)

finally:
    browser.quit()

