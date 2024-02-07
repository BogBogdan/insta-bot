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
    