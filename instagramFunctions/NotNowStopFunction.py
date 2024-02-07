from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def klikni_na_not_now(driver):
    try:
        # Sačekaj da se dugme pojavi i bude klikabilno
        dugme_not_now = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='_a9-- _ap36 _a9_1' and @tabindex='0']"))
        )

        # Klikni na dugme "Not Now"
        dugme_not_now.click()

        print("Uspešno kliknuto na dugme 'Not Now'")
    except Exception as e:
        print(f"Greska prilikom klika na dugme 'Not Now': {e}")
