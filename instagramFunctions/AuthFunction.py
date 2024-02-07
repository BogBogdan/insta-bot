from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def auth(driver, username, password):
	try:
		
		time.sleep(random.randrange(2,4))

		input_username = driver.find_element(By.NAME, "username")
		input_password = driver.find_element(By.NAME, "password")

		input_username.send_keys(username)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(password)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(Keys.ENTER)

	except Exception as err:
		print(err)
		driver.quit()