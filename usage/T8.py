from core.class2 import engine,save
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os
log='//a[@id="login_tab"]'
email='//input[@id="log_email"]'
password='//input[@id="log_password"]'
button='//button[@id="logsub"]'
url1="chrome-extension://ldbcplcolkhgemejdgibfmhemnkecgni/login.html"
def logfuc(driver,url):
    driver.get(url)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH,log)))

    logem=driver.find_element_by_xpath(log)
    logem.click()

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH,email)))

    emailem=driver.find_element_by_xpath(email)
    emailem.send_keys('1967564050@qq.com ')
    passwordem=driver.find_element_by_xpath(password)
    passwordem.send_keys('258369')
    buttonem=driver.find_element_by_xpath(button)
    buttonem.click()
    print(2)
    ws=driver.window_handles
    print(ws)
    driver.switch_to.window(ws[1])
    driver.close()
    driver.switch_to.window(ws[0])
data={'title':('//h1[@class="entry-title"]','text'),
      'content':('//div[@class="entry-content"]','text'),
      'next':('//span[@class="nav-previous"]/a','href')}
dir=r'F:\新建文件夹 (2)'
os.chdir(dir)
href="https://qingsewenxue.wordpress.com/2011/12/31/%e6%b7%ab%e8%95%a9%e5%b0%91%e5%a9%a6%e7%99%bd%e6%bd%94/"
with engine() as e1:
    e1.predo(logfuc,e1.driver,url1)
    print(1)
    print(e1.recuv(href,data,func=save))
