from selenium import webdriver
# Save a screenshot from spotify.com in current directory. “””
DRIVER = './chromedriver'
#driver = webdriver.Chrome(DRIVER)
# driver.get('https://www.spotify.com')
#screenshot = driver.save_screenshot('my_screenshot.png')
# driver.quit()


driver = webdriver.Chrome(DRIVER)

driver.get('https://www.spotify.com')
el = driver.find_element_by_tag_name('body')
el.screenshot('my_screenshot.png')
driver.quit()
