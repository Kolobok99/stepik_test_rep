import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Firefox()

    # 1.Открыть страницу http://suninjuly.github.io/selects1.html
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    # 2.Посчитать сумму заданных чисел
    x1 = int(browser.find_element(By.ID, "num1").text)
    x2 = int(browser.find_element(By.ID, "num2").text)
    sum = x1 + x2

    # 3.Выбрать в выпадающем списке значение равное расчитанной сумме
    select_sum = Select(browser.find_element(By.ID, "dropdown")).select_by_value(str(sum))

    # 4.Нажать кнопку "Submit"
    #submit = browser.find_element(By.CLASS_NAME, "btn btn-default")
    #submit.click()
    time.sleep(10)

finally:
    browser.quit()