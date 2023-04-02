from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from mailtm import Email
import time
incorrectacc=False
from bs4 import BeautifulSoup
chrome_options=webdriver.ChromeOptions()
inp=input("bots: ")
for line in range(int(inp)):
        if line==0:
            driver=uc.Chrome(use_subprocess=True)
            driver.get("https://open.spotify.com/")
            while True:
                try:
                    driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').click()
                    break
                except:
                    pass
        else:
            driver.execute_script('''window.open();''')#
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[line])
            driver.get("https://open.spotify.com/")
            while True:
                try:
                    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/header/button[2]').click()
                    break
                except:
                    pass
            while True:
                try:
                    driver.find_element(By.XPATH,'//*[@id="context-menu"]/div/ul/li[5]/button').click()
                    break
                except:
                    pass
        ndriver2=uc.Chrome(use_subprocess=True)
        ndriver2.get("https://www.randomlists.com/random-names#:~:text=Random%20names%3A%201%20Callie%20Porter%202%20Ethen%20Schmidt,7%20Heaven%20Day%208%20Belinda%20Key%20More%20items")
        name = ndriver2.find_element(By.XPATH,'/html/body/div/div[1]/main/article/div[2]/ol/li[1]').text
        name=name.split()
        ndriver2.close()
        incorrecacc=False
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
                driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div/form/div[8]/div/button').click()
                break
            except:
                pass
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
            time.sleep(7)
            try:
                driver.find_element(By.XPATH,'//*[@id="encore-web-main-content"]/div/div/div/div/div/button').click()
            except:
                pass
            while True:
                try:
                    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a')
                    break
                except:
                    pass
            driver.get("https://open.spotify.com/playlist/1HMKoB9u4sTtWdBBi0BA7S?si=845d77f7830e4017")
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
            while True:
                try:
                    driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/footer/div/div[3]/div/div[3]/button').click()
                    break
                except:
                    pass
            time.sleep(2)
            print(line)
        if line==int(inp)-1:
            while True:
                for win in range(line):
                    print(win)
                    driver.switch_to.window(driver.window_handles[win])
                    while True:
                        try:
                            driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[2]/div[1]')
                            break
                        except:
                            pass
                    seconds=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[2]/div[1]').text
                    seconds=int(seconds.split(":")[1])
                    print(seconds)
                    if seconds>35:
                        while True:
                            try:
                                driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[1]').click()
                                break
                            except:
                                pass
                    time.sleep(1)
