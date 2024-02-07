from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def izaberi_sliku(driver, putanja_do_slike):
    try:
        # Pronađi dugme "Select from computer" po klasi
        dugme = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_acan"))
        )

        # Izvrši JavaScript kako bi kliknulo na dugme, bez obzira na njegovu interaktivnost
        driver.execute_script("arguments[0].click();", dugme)

        # Pronađi input za unos fajla (type="file") i pošalji putanju do slike
        input_fajla = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
        )
        input_fajla.send_keys(putanja_do_slike)

        print(f"Uspešno izabrana slika sa putanje: {putanja_do_slike}")
    except Exception as e:
        print(f"Greska prilikom izbora slike: {e}")