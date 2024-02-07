from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def optimization_of_image(driver):
    try:
        # Pronalaženje SVG elementa po atributu aria-label
        svg_element = driver.find_element(By.XPATH, f'//*[@aria-label="Select crop"]')

        # Simulacija klika na SVG element
        svg_element.click()
    except Exception as e:
        print("Greška:", e)


def select_original_optimization(driver):

    css_selector = "span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.x1s688f.x1roi4f4.x1tu3fi.x3x7a5m.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
    try:
        element = driver.find_element("css selector", css_selector)

        # Klik na element
        element.click()
        
    except Exception as e:
        print("Greška:", e)