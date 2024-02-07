from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def sacekaj_i_klikni(driver):
    css_selector = 'svg[aria-label="New post"].x1lliihq.x1n2onr6.x5n08af'

    try:
        # Sačekaj da se element pojavi na stranici
        element = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

        # Klikni na element
        element.click()

        print(f"Uspešno kliknuto na element sa CSS selectorom: {css_selector}")
    except Exception as e:
        print(f"Greska prilikom cekanja i klika: {e}")