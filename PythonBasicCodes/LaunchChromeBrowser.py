from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\PythonWorkspace\chromedriver.exe")

driver.get("https://zeenyx.com/")

print(driver.title)

driver.close()

driver.quit()
