from selenium.webdriver import Chrome
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By



nav = Chrome()

def open_web1(nav):
    

    nav.get('url')

    sleep(3)

    nav.find_element(By.NAME, 'login').send_keys('')

    nav.find_element(By.NAME, 'password').send_keys('')

    button = nav.find_elements(By.TAG_NAME, 'button')
    button[1].click()



def open_web2(nav):
    

    nav.execute_script("window.open('');")
    nav.switch_to.window(nav.window_handles[1])
    sleep(1.5)
    nav.get('url')

    nav.find_element(By.NAME, 'user').send_keys('')
    nav.find_element(By.NAME, 'password').send_keys('')

    nav.find_element(By.TAG_NAME, 'button').click()


def web3(nav):
    

    nav.execute_script("window.open('');")
    nav.switch_to.window(nav.window_handles[2])
    sleep(1.5)

    nav.get('url')

    nav.find_element(By.ID, 'password').send_keys('\ue007')



open_web1(nav)
open_web2(nav)
open_web3(nav)
