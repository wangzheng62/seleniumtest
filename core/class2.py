from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from json import dumps
import os,re,random

class Engine():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
    def __enter__(self):
        print('__enter__')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        try:
            self.driver.close()
            self.driver.quit()
        except:
            self.driver.close()
            self.driver.quit()
    def __del__(self):
        try:
            self.driver.close()
            self.driver.quit()
        except:
            self.driver.close()
            self.driver.quit()
    def __getddata(self,url,data):
        self.driver.get(url)
        res={}
        for key in data:
            elem = self.driver.find_element_by_xpath(data[key][0])
            if data[key][1] == 'text':
                res[key] = elem.text
            else:
                res[key] = elem.get_attribute(data[key][1])
        return res

    def walk(self,urltree,data,save='text'):
        return self.__getddata(urltree,data)

def engine():
    e=Engine()
    return e

data={'title':('//*[@id="wrapper"]/div[5]/div/div[2]/h1','text'),
      'content':('//*[@id="content"]','text'),
      'next':('//*[@id="wrapper"]/div[5]/div/div[4]/a[4]','href')}

p='http://www.shubaoxsw.org/2_2741/296549.htl'
with engine() as e1:
    print(e1.walk(p,data))

