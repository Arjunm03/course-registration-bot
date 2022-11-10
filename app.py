from time import sleep
from encrypt import getDecryptedFile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username, password = getDecryptedFile("credentials.txt").split("\n")
with open("crns.txt", "r") as file:
        crns = file.read()
crns = crns.split("\n")

driver = webdriver.Chrome()
driver.get("https://oscar.gatech.edu")
driver.get("https://sso.sis.gatech.edu/ssomanager/c/SSB")
driver.find_element(By.NAME, 'username').send_keys('amannan8')
driver.find_element(By.NAME, 'password').send_keys('Gatechpa5503')
driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'plaintable')))
driver.get("https://oscar.gatech.edu/bprod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu")
driver.get("https://oscar.gatech.edu/bprod/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu")
driver.get("https://oscar.gatech.edu/bprod/bwskfreg.P_AltPin")
driver.find_element(By.NAME, 'term_in').send_keys('Spring 2023')
driver.find_element(By.NAME, 'term_in').send_keys(Keys.ENTER)
for i, crn in enumerate(crns):
    driver.find_element(By.ID, 'crn_id' + str(i + 1)).send_keys(crn)
driver.find_element(By.ID, 'crn_id1').send_keys(Keys.ENTER)

sleep(1000)