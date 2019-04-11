# Import Selenium webdrive
from selenium import webdriver
import pyautogui
# invoke chrome option to load extensions
options = webdriver.ChromeOptions()


driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()  # maximize the
driver.get("https://www.google.com")
# extension image is saved in project folder as findicon.png
# locateOnScreen, a pyautogui method to locate the extension' x & y coordinates in screen
# save the extension as image
buttonx, buttony = pyautogui.locateCenterOnScreen('mic.png')
# print(pyautogui.locateCenterOnScreen('mic.png'))
# trigger click event using the pyutogui click method
pyautogui.click(buttonx, buttony)
