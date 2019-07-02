
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from json import dumps
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)
if __name__=='__main__':
    u1=r'http://www.w3school.com.cn/xpath/xpath_syntax.asp'
    u2=r'https://www.google.com/flights#flt=LAX.LHR,LGW,CDG,ORY,ARN.2019-09-05*BCN,MAD,FRA,GVA,FCO.LAX.2019-09-24;c:USD;e:1;so:1;sd:1;t:f;tt:m'
    driver.get(u2)
    elems=driver.find_elements_by_xpath('//span[class="gws-flights__ellipsize"]/span/span')
    elems1=driver.find_elements_by_class_name('gws-flights__footer-picker-value')
    print(len(elems))
    for e in elems:
        print(e.text)