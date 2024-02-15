from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def insert_text_into_element(driver, text):

    css_selector = "div.xw2csxc.x1odjw0f.x1n2onr6.x1hnll1o.xpqswwc.xl565be.x5dp1im.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1w2wdq1.xen30ot.x1swvt13.x1pi30zi.xh8yej3.x5n08af"
    try:
        # Pronalazimo element po CSS selektoru
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        
        text = text.replace('\\n', '\ue007')
        
        print(text)
        # Ubacujemo tekst u element
                # Simulacija unosa teksta pomoću tastature
        ActionChains(driver).move_to_element(element).click().send_keys(text).perform()
        

        print("Uspešno unet tekst u element.")
    except Exception as e:
        print("Nije moguće pronaći ili uneti tekst u element.")
        print("Greška:", e)
