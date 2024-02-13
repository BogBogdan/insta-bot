from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_on_reel_alert(driver):
    try:
        div_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'x78zum5') and contains(@class, 'x1q0g3np') and contains(@class, 'xdko459')]"))
        )


        # Kliknite na dugme OK
        div_element.click()
        # Kliknite na dugme OK

        print("Uspešno kliknuto na dugme 'Not Now'")
    except Exception as e:
        print(f"Greska prilikom klika na dugme 'Not Now': {e}")

