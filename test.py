from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

name = "Crime Boss"
keywords = name.split(' ')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://store.epicgames.com/en-US/")
driver.maximize_window()

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    if name in link.get_attribute("innerHTML"):
        link.click()