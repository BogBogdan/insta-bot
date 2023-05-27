from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
from selenium.webdriver.common.by import By
import numpy as np
# Username and password of your instagram account:
my_username = ''
my_password = ''

browser = webdriver.Chrome('chromedriver')

# Authorization:
def auth(username, password):
	try:
		browser.get('https://instagram.com')
		time.sleep(random.randrange(2,4))

		input_username = browser.find_element(By.NAME, "username")
		input_password = browser.find_element(By.NAME, "password")

		input_username.send_keys(username)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(password)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(Keys.ENTER)

	except Exception as err:
		print(err)
		browser.quit()


def get_into_messsages():
    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div').click()
    time.sleep(2)	

    try:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(2)
    except Exception as e:
	    print("")
	    

def number_of_chats(parent_element):
    brojac=1
    while(True):
        try:
            matching_elements = parent_element.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div['+str(brojac)+']')
            #/div/div/div[3]/div/div/span
            brojac+=1
        except Exception as e:
	        return brojac-1
    
def check_for_messages():
	# Find the parent element
    parent_element = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[3]/div')
    broj_ponavljanja=number_of_chats(parent_element)
    niz = []

    #/div/div/div[3]/div/div/span
    for brojac in range(1, broj_ponavljanja):
        name ="N1M3"
        try:
            name = parent_element.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div['+str(brojac)+']/div/div/div[2]/div/div[1]/span/span').text
        except Exception as e:
              continue
        
        par = (-1,name)
        
        try:
            parent_element.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div['+str(brojac)+']/div/div/div[3]/div/div/span')          
            par = (1, name)  # New message found in this chat
        except Exception as e:
            par = (0, name)  # No new message in this chat
        niz.append(par)
    return niz



def get_message(parent_element, brojac):
     try:
        return parent_element.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div['+str(brojac)+']/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div').text          
     except Exception as e:
        try:
            return parent_element.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div['+str(brojac)+']/div/div/div/div/h3/div[2]/span/span').text          
        except Exception as e:
            return "Error"
     
def read_messages():
    elements = browser.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div')        
    text_list = [element.text for element in elements]
    return text_list

def get_data(messages):
     niz=[]
     for message in messages:
        if r"\n" in repr(message):
            text_list = message.split("\n")
            novi=(text_list[0], text_list[1])
            niz.append(novi)
        else:
            novi=("Time", message)
            niz.append(novi)
     return niz
            

     
def answer_message(msg):

    try:
        text_bar = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')                                      
        text_bar.send_keys(msg)
        text_bar.send_keys(Keys.ENTER)
    except Exception as e:
         return "Failed"
    return "Success"

def get_into_chat(name):
    parent_element = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[3]/div')
    broj_ponavljanja=number_of_chats(parent_element)

    for brojac in range(1, broj_ponavljanja):
        try:
            if name == parent_element.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div['+str(brojac)+']/div/div/div[2]/div/div[1]/span/span').text:
                parent_element.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div['+str(brojac)+']/div/div').click()
                time.sleep(5)
                return read_messages()
        except Exception as e:
              continue
    return "Error"



retries = 0
while retries < 3:
    try:
        auth(my_username, my_password)  
        break
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        retries += 1
        time.sleep(5) 
else:
    print("Max retries reached. Failed to execute kreni().")

time.sleep(5)

get_into_messsages()

while(True):
    niz = check_for_messages()
    for acc in niz:
        if acc[0]==1:
            messages = get_data(get_into_chat(acc[1]))
            #OBRADA PORUKE
            send = (messages[-2])[1]
            print((messages[-2]))
            print(answer_message(send))
            time.sleep(10)	


