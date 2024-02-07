from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

def getDriver():
    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    #chrome_options.add_argument('--headless')

    # Konfigurišite ChromeDriver pomoću Service objekta
    chrome_service = ChromeService(ChromeDriverManager().install())

    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

    # Inicijalizacija WebDriver-a (npr. ChromeDriver)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options, desired_capabilities=capabilities)

    return driver

