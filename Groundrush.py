from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

chrome_driver_path = r"C:/Users/pranjalchaubey/Desktop/Groundrush/chromedriver-win64/chromedriver.exe"
service = Service(chrome_driver_path)
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(
    "https://ai.decaturfm.com/")
time.sleep(1)

username = driver.find_element(By.ID, "username")
username.send_keys("pran")  # Enter Your Email Address
time.sleep(3)
pword = driver.find_element(By.ID, "password")
pword.send_keys("Pranjal@#190103")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)
driver.find_element(By.ID, "rss_url").send_keys("https://moxie.foxnews.com/google-publisher/latest.xml")
time.sleep(3)
gender = driver.find_element(By.NAME, "voice_gender")
gender.send_keys("Male")
wait = WebDriverWait(driver, 10)
upload_file = driver.find_element(By.ID, "music_file").send_keys("c:/Users/pranjalchaubey/Downloads/Ambient.mp3")
time.sleep(4)
limit= driver.find_element(By.NAME, "limit")
limit.send_keys("2")
time.sleep(3)
driver.find_element(By.ID, "sftp_host").send_keys("75.43.156.99")
driver.find_element(By.ID, "sftp_port").send_keys("2022")
driver.find_element(By.ID, "sftp_username").send_keys("haljordan")
driver.find_element(By.ID, "sftp_password").send_keys("RawNotesandBeats$!")
driver.find_element(By.ID, "sftp_remote_path").send_keys("/ANNOUNCEMENTS_FOLDER")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//a[@href='/logout/']").click()
time.sleep(10)
driver.refresh

time.sleep(10)