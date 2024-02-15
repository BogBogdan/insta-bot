from driver import Driver
from loginCredentials import getCredentials
from instagramFunctions import AddImage, AddTextToImage, AuthFunction, ClickButtonNext, ClickButtonShare, NotNowStopFunction, OpenNewPostFunction, OriginalImageSize, ClickReelsAlert
import time
import random
import sys


def addReelOnInstagram(imgUrl, imgText):
    
    driver = Driver.getDriver()
    username, password = getCredentials.usernameNpassword()
    
    driver.get("http://www.instagram.com")

    # Pauza od 5 sekundi (prilagodite prema potrebi)
    time.sleep(random.randrange(4,5))

    AuthFunction.auth(driver, username, password)

    time.sleep(random.randrange(4,5))

    OpenNewPostFunction.sacekaj_i_klikni(driver)

    time.sleep(random.randrange(4,5))

    AddImage.izaberi_sliku(driver, imgUrl)
    
    time.sleep(random.randrange(4,5))

    NotNowStopFunction.klikni_na_not_now(driver)

    time.sleep(random.randrange(4,5))

    OpenNewPostFunction.sacekaj_i_klikni(driver)

    time.sleep(random.randrange(4,5))

    AddImage.izaberi_sliku(driver, imgUrl)

    time.sleep(random.randrange(4,5))

    ClickReelsAlert.click_on_reel_alert(driver)

    time.sleep(random.randrange(4,5))

    OriginalImageSize.optimization_of_image(driver)

    time.sleep(random.randrange(4,5))

    OriginalImageSize.select_original_optimization(driver)

    time.sleep(random.randrange(4,5))
    
    ClickButtonNext.click_on_button_next(driver)

    time.sleep(random.randrange(4,5))

    ClickButtonNext.click_on_button_next(driver)

    time.sleep(random.randrange(4,5))

    AddTextToImage.insert_text_into_element(driver, imgText)

    time.sleep(random.randrange(14,15))

    ClickButtonShare.shere_photo(driver)


    # Zatvaranje pregledača
    driver.quit()
    

def main():
    # Provera broja argumenata
    if len(sys.argv) != 3:
        print("Molimo vas unesite tačno dva argumenta.")
        print("Na primer: python test.py arg1 arg2")
        return
    
    # Čitanje argumenata iz komandne linije
    image_path = sys.argv[1]
    caption = sys.argv[2]
    
    # Poziv funkcije addImageOnInstagram sa argumentima iz komandne linije
    addReelOnInstagram(image_path, caption)

if __name__ == "__main__":
    main()