from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyautogui
captch=False
from anticaptchaofficial.recaptchav2proxyless import *
import os
from mailtm import Email
import requests
from bs4 import BeautifulSoup
botcount = 0
import random
chrome_options=webdriver.ChromeOptions()
random_playlist=['https://open.spotify.com/playlist/164fshuZcE0Scul7y6NVkz?si=ZjNKGKeMQJONfq2ZtD7xAw', 'https://open.spotify.com/playlist/1jRam4tFRtmPUvVoXGEBIM?si=M-jdTt0OQoiiq53uRlbPhQ', 'https://open.spotify.com/playlist/3SlK3Meetc1l7OxHYjyH7G?si=5Prb-YmyT8qdY5-q5qap-g', 'https://open.spotify.com/playlist/7mLiDqehe8Fae1iboVRJUh?si=zopRKUyyRumYuMXxBwILvw', 'https://open.spotify.com/playlist/2EmINGcohTI6Qtezw4cWIy?si=10szaVB7REq4CEAvliW68Q', 'https://open.spotify.com/playlist/4LXg7o2j9brKLNM8gEaoal?si=9OozF1bpS6uZgGhYc_pnHQ', 'https://open.spotify.com/playlist/7gdqXHUaODvSp8vyinMpc1?si=YasK4jBHSW22h7KB99Nsdw', 'https://open.spotify.com/playlist/3fkZhShArEgcvGghLKvDy5?si=PrQ1YS5CQLuU8VDQAwjiMg', 'https://open.spotify.com/playlist/4ctoDGbBZrqNxrjARgM2cz?si=iTm3QdVxTviysfiqFg02hQ', 'https://open.spotify.com/playlist/6njZSOR4is919eVTJl21So?si=W12v0hpzQDyqwrF0Dav_fA', 'https://open.spotify.com/playlist/06crwKAjb9adcdJadbHIhP?si=35QG6Y1XQ9efqphJwK-r4Q', 'https://open.spotify.com/playlist/2SpA0rC9EoXFeGOW2vPyGK?si=G3h-eC58RCiBF63LCACWww', 'https://open.spotify.com/playlist/6SBhJI5JkfQ9osBCOD5WQa?si=-xM8hA1zRyOgabuu23Kq8w', 'https://open.spotify.com/playlist/4sDyMTrdCBoisZpdL8YiTH?si=e6qVdkYBT4yCD1U2OFOaIA', 'https://open.spotify.com/playlist/6jS6r4XRaDcT3NH22o4ZyF?si=4Xcb1GT7Tr-ebR8t-nK55A', 'https://open.spotify.com/playlist/1hglBZmeD8dhOVAA16OvHO?si=3IY4TXZtTymGK_-B_D-bfg', 'https://open.spotify.com/playlist/7lYZR416v7jkYWfwAhOcPE?si=yzd05srISdeuzlUX8lF1-g', 'https://open.spotify.com/playlist/5VIyhGUlwChbflXfaFGNfa?si=IMw-4yuvRYW_1zSV-yUEmQ', 'https://open.spotify.com/playlist/1dHhNOr2lJO7dBBX3qBwPp?si=wAtExkavQ8mkjzWg1hK4Kg', 'https://open.spotify.com/playlist/2y6uWobVyL8TmGjA0Mzech?si=OSWMMbRBRHKFCO4dzReH6A']
driver=uc.Chrome(use_subprocess=True)
driver.get("https://open.spotify.com/")
while True:
   try:
       driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').click()
       break
   except:
       pass
for line in range(5):
        ndriver2=uc.Chrome(use_subprocess=True)
        ndriver2.get("https://www.randomlists.com/random-names#:~:text=Random%20names%3A%201%20Callie%20Porter%202%20Ethen%20Schmidt,7%20Heaven%20Day%208%20Belinda%20Key%20More%20items")
        name = ndriver2.find_element(By.XPATH,'/html/body/div/div[1]/main/article/div[2]/ol/li[1]').text
        name=name.split()
        ndriver2.close()
        incorrectacc=False
        test=Email()
        test.register()
        email=test.address
        while True:
            try:
                driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[1]').click()
                break
            except:
                pass
        while True:
            try:
                driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(email)
                break
            except:
                pass
        driver.find_element(By.XPATH,'//*[@id="confirm"]').send_keys(email)
        driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Spotpass123!")
        driver.find_element(By.XPATH,'//*[@id="displayname"]').send_keys(f"{name[0]} {name[1]}")
        driver.find_element(By.XPATH,'//*[@id="day"]').send_keys("04")
        driver.find_element(By.XPATH,'//*[@id="month"]').click()
        driver.find_element(By.XPATH,'//*[@id="month"]/option[5]').click()
        driver.find_element(By.XPATH,'//*[@id="year"]').send_keys("2000")
        driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div/form/fieldset/div/div[1]/label/span[1]').click()
        driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div/form/div[7]/div/label/span[1]').click()
        while True:
            try:
                driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a')
                break
            except:
                pass
            try:
                if driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/span').text:
                    incorrectacc=True
            except:
                pass
        if not incorrectacc:
            while True:
                try:
                    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a')
                    break
                except:
                    pass
            driver.get("https://open.spotify.com/playlist/3SlK3Meetc1l7OxHYjyH7G")
            while True:
                try:
                    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/button[1]').click()
                    break
                except:
                    pass
            while True:
                try:      
                    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/div/button').click()
                    break
                except:
                    pass
