from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import date

chrome_options = Options()
chrome_options.add_argument("--headless=new")

driver= webdriver.Chrome(options=chrome_options)
driver.get("https://github.com/settings/tokens")
elem = driver.find_element(By.ID, "login_field")
elem.send_keys("")
elem2 = driver.find_element(By.ID, "password")
elem2.send_keys("")
elem3= driver.find_element(By.NAME, "commit")
elem3.click()
#time.sleep(3)
elem4= driver.find_element(By.CLASS_NAME, "authentication")

#right now only covers the two factor authentication from authenticator app, will add for other methods
if(elem4):
    morebtn = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div/div[2]/div[2]/div/button")
    morebtn.click()
    auth = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div/div[2]/div[2]/div/ul/li[1]/a")
    auth.click()
    time.sleep(1)
    enter = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div/div[2]/div[2]/form/input[2]")
    enter.send_keys(input("enter two factor auth:"))

newbtn= driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div/div/div[2]/div/div/div[1]/div[1]/div/details/summary")
newbtn.click()

classic = driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/main/div/div/div[2]/div/div/div[1]/div[1]/div/details/details-menu/div/div/div/a[2]")
classic.click()
time.sleep(1)

# authelem= driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div")
# if(authelem):
#     authagain= driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div/sudo-credential-options/div[5]/div/ul/li[2]/button")
#     authagain.click()
#     time.sleep(1)
#     enter= driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div/sudo-credential-options/div[3]/form/div/input")
#     enter.send_keys(input("enter two factor auth:"))

note= driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/main/div/div/div[2]/div/div/form/dl/dd/input")
note.send_keys("{}".format(date.today()))

checkes= driver.find_elements(By.NAME, "oauth_access[scopes][]")

for i in checkes:
    i.click()

generate= driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div/div/div[2]/div/div/form/p/button")
generate.click()

time.sleep(1)

#copy= driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/span/clipboard-copy")
#copy.click()

el = driver.find_element(By.ID, "new-oauth-token")
token = el.text
print(token)

time.sleep(1)

driver.close()

