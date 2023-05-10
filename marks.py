from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os

# os.environ['PATH']+=r"/home/siddharth/Documents/ITC/selenium/driver"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://vtop.vit.ac.in/vtop/login")
driver.implicitly_wait(4)
button=driver.find_element(By.CLASS_NAME, "fa-3")
button.click()

username=driver.find_element(By.NAME, "username")
username.send_keys("")
password=driver.find_element(By.NAME, "password")
password.send_keys("")


try:
    cap=driver.find_element(By.ID, "captchaStr")
    cap.click()
    while True:
        str=cap.get_attribute("value")
        if len(str)==6:
            subbut = driver.find_element(By.ID, "submitBtn")
            subbut.click()
            break
except:
    subbut = driver.find_element(By.ID, "submitBtn")
    subbut.click()
    time.sleep(10)

elem = WebDriverWait(driver, 60).until(
EC.presence_of_element_located((By.XPATH, "//strong[@class='fw-bold h3 text-dark']")) #This is a dummy element
)
elem = WebDriverWait(driver, 60).until(
EC.presence_of_element_located((By.XPATH, "//strong[@class='fw-bold h3 text-dark']")) #This is a dummy element
)

driver.find_element(By.XPATH, "//button[@class='btn btn-outline-primary btn-sm dropdown-toggle text-light']").click()

driver.find_element(By.XPATH, "//a[@data-url='examinations/StudentMarkView']").click()

select = Select(driver.find_element(By.ID, 'semesterSubId'))
select.select_by_value("VL20222305")

print(driver.page_source)


while True:
    pass

