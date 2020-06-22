from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from json import dumps
import os,re,random
from time import sleep

class Engine():
    def __init__(self,extension=None):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("load-extension=G:/Users/36357/AppData/Local/Google/Chrome/User Data/Default/Extensions/ldbcplcolkhgemejdgibfmhemnkecgni/8.10.8_0")
        #chrome_options.add_argument("--disable-gpu")
        if extension:
            chrome_options.add_extension(extension)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        print("__init__")
    def __enter__(self):
        print('__enter__')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            print(e)
    def predo(self,fuc,*args,**kwargs):
        fuc(*args,**kwargs)
    def testurl(self,url):
        self.driver.get(url)
        sleep(20)
        res=self.driver.page_source
        return res

    def __getddata(self,url,data):
        self.driver.get(url)
        print(self.driver.current_url)
        res={}
        for key in data:
            try:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,data[key][0])))
            except Exception as e:
                print(e)
                if key=='next':
                    res[key]=None
                    return res
            elem = self.driver.find_element_by_xpath(data[key][0])
            if data[key][1] == 'text':
                res[key] = elem.text
            else:
                res[key] = elem.get_attribute(data[key][1])
        return res
    def singleget(self,url,data):
        try:
            con=self.__getddata(url,data)
            return con
        except Exception as e:
            print(e)
#递归
    def __recuv(self,url,data):
        if 'next' not in data:
            raise ValueError('递归检索数据中必须包含key为"next"，value为url的定义项')
        n=0
        while True:
            print(n)
            nexturl=yield self.__getddata(url,data)
            url=nexturl
            n=n+1
    def recuv(self,url,data,func=print):
        r=self.__recuv(url,data)
        try:
            con=r.send(None)
        except Exception as e:
            print(e)
            return
        func(con)
        while con['next']:
            try:
                con=r.send(con['next'])
                func(con)
            except Exception as e:
                print(e)
                break
        r.close()
#树遍历

def ma(s):
    pattern=r'[-\(\)\.\d\w\u4e00-\u9fa5]'
    p=re.compile(pattern)
    l=p.findall(s)
    res=''.join(l)
    return res

def save(con):
    title=ma(con['title'])
    with open(title+'.txt','ab') as f:
        f.write(con['content'].encode(errors='ignore'))
def engine():
    e=Engine()
    return e
if __name__=='__main__':
    pass