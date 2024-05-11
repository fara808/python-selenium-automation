from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# Click SignIn button
#data-test="@web/AccountLink"
#$x("//a[@data-test='@web/AccountLink']")
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

sleep(3)

# Click SignIn from side navigation
#$x("//a[@data-test='accountNav-signIn']")

driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(4)
#"Sign into your Target account" text is shown
actual_text = driver.find_element(By.XPATH,"//h1[contains(@class, 'styles__AuthHeading') and .//span[contains(text(), 'Sign into your Target account')]]")
print(actual_text)

driver.quit()