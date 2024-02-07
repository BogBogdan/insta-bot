from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
import random

def ucitaj_podatke_iz_fajla(putanja):
    try:
        with open(putanja, 'r') as fajl:
            podaci = json.load(fajl)
            return tuple(sorted(podaci.items()))  # Vraća uredjen par (tuple)
    except FileNotFoundError:
        print(f"Fajl na putanji '{putanja}' nije pronađen.")
    except json.JSONDecodeError:
        print(f"Greška prilikom dekodiranja JSON-a u fajlu na putanji '{putanja}'.")
    except Exception as e:
        print(f"Neočekivana greška: {e}")

def auth(username, password):
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

def sacekaj_i_klikni():
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

def izaberi_sliku(putanja_do_slike):
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

def klikni_na_not_now():
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

def optimization_of_image():
    try:
        # Pronalaženje SVG elementa po atributu aria-label
        svg_element = driver.find_element(By.XPATH, f'//*[@aria-label="Select crop"]')

        # Simulacija klika na SVG element
        svg_element.click()
    except Exception as e:
        print("Greška:", e)

def select_original_optimization():

    css_selector = "span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.x1s688f.x1roi4f4.x1tu3fi.x3x7a5m.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
    try:
        element = driver.find_element("css selector", css_selector)

        # Klik na element
        element.click()
        
    except Exception as e:
        print("Greška:", e)

def click_on_button_next():

    css_selector = "div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37[tabindex='0']"
    try:
        # Pronalazimo element po CSS selektoru
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        
        # Klik na element
        element.click()
        print("Uspešno kliknuto na element.")
    except Exception as e:
        print("Nije moguće pronaći ili kliknuti element.")
        print("Greška:", e)

def insert_text_into_element(text):

    css_selector = "div.xw2csxc.x1odjw0f.x1n2onr6.x1hnll1o.xpqswwc.xl565be.x5dp1im.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1w2wdq1.xen30ot.x1swvt13.x1pi30zi.xh8yej3.x5n08af"
    try:
        # Pronalazimo element po CSS selektoru
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        
        # Ubacujemo tekst u element
        element.send_keys(text)
        print("Uspešno unet tekst u element.")
    except Exception as e:
        print("Nije moguće pronaći ili uneti tekst u element.")
        print("Greška:", e)

def shere_photo(driver):

    css_selector = "div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37[tabindex='0']"
    try:
        # Pronalazimo element po CSS selektoru
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        
        # Klik na element
        element.click()
        print("Uspešno kliknuto na element.")
    except Exception as e:
        print("Nije moguće pronaći ili kliknuti element.")
        print("Greška:", e)

def login(username, password):

    # Otvaranje web stranice
    driver.get("http://www.instagram.com")

    # Pauza od 5 sekundi (prilagodite prema potrebi)
    time.sleep(random.randrange(4,5))

    auth(username, password)

    time.sleep(random.randrange(4,5))

    sacekaj_i_klikni()

    time.sleep(random.randrange(4,5))

    izaberi_sliku("C:/Users/bogda/OneDrive/Desktop/Slike/2.jpg")
    
    time.sleep(random.randrange(4,5))

    klikni_na_not_now()

    time.sleep(random.randrange(4,5))

    sacekaj_i_klikni()

    time.sleep(random.randrange(4,5))

    izaberi_sliku("C:/Users/bogda/OneDrive/Desktop/Slike/2.jpg")

    time.sleep(random.randrange(4,5))

    optimization_of_image()

    time.sleep(random.randrange(4,5))

    select_original_optimization()

    time.sleep(random.randrange(4,5))
    
    click_on_button_next()

    time.sleep(random.randrange(4,5))

    click_on_button_next()

    time.sleep(random.randrange(4,5))

    insert_text_into_element("Ovo je neki tekst \n #freedom")

    time.sleep(random.randrange(60,70))

    # Zatvaranje pregledača
    driver.quit()



# Primer korišćenja
putanja_do_fajla = './credentials.json'
password, username = ucitaj_podatke_iz_fajla(putanja_do_fajla)

username = username[1]
password = password[1]


chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
#chrome_options.add_argument('--headless')

# Konfigurišite ChromeDriver pomoću Service objekta
chrome_service = ChromeService(ChromeDriverManager().install())

capabilities = DesiredCapabilities.CHROME
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}


# Inicijalizacija WebDriver-a (npr. ChromeDriver)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options, desired_capabilities=capabilities)

login(username, password)