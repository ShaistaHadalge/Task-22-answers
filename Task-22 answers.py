from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
chrome_service = ChromeService(r"C:\Users\shais\OneDrive\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.instagram.com/guviofficial/")

driver. find_element(By.XPATH, '//*[@id="mount_0_0_ay"]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button'). text
driver. find_element(By. XPATH, '//*[@id="mount_0_0_ay"]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[1]/button'). text
driver. find_element(By.XPATH, '//*[@id="mount_0_0_ay"]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button'). text
