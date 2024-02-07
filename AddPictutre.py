from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from driver import Driver
from loginCredentials import getCredentials
from instagramFunctions import AddImage, AddTextToImage, AuthFunction, ClickButtonNext, ClickButtonShare, NotNowStopFunction, OpenNewPostFunction, OriginalImageSize
import time
import json
import random


def start():
    driver = Driver.getDriver()
    username, password = getCredentials.usernameNpassword()
    
    driver.get("http://www.instagram.com")

    # Pauza od 5 sekundi (prilagodite prema potrebi)
    time.sleep(random.randrange(4,5))

    AuthFunction.auth(driver, username, password)

    time.sleep(random.randrange(4,5))

    OpenNewPostFunction.sacekaj_i_klikni(driver)

    time.sleep(random.randrange(4,5))

    AddImage.izaberi_sliku(driver, "C:/Users/bogda/OneDrive/Desktop/Slike/2.jpg")
    
    time.sleep(random.randrange(4,5))

    NotNowStopFunction.klikni_na_not_now(driver)

    time.sleep(random.randrange(4,5))

    OpenNewPostFunction.sacekaj_i_klikni(driver)

    time.sleep(random.randrange(4,5))

    AddImage.izaberi_sliku(driver, "C:/Users/bogda/OneDrive/Desktop/Slike/2.jpg")

    time.sleep(random.randrange(4,5))

    OriginalImageSize.optimization_of_image(driver)

    time.sleep(random.randrange(4,5))

    OriginalImageSize.select_original_optimization(driver)

    time.sleep(random.randrange(4,5))
    
    ClickButtonNext.click_on_button_next(driver)

    time.sleep(random.randrange(4,5))

    ClickButtonNext.click_on_button_next(driver)

    time.sleep(random.randrange(4,5))

    AddTextToImage.insert_text_into_element(driver, "Ovo je neki tekst \n #freedom")

    time.sleep(random.randrange(60,70))

    # Zatvaranje pregledača
    driver.quit()
    
start()