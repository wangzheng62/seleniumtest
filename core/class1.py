from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from json import dumps
import os,re,random

class Field():
    def __init__(self,xpath,data='text'):
        self.xpath=xpath
        self.data=data
class Job():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
    def __del__(self):
        try:
            self.driver.close()
            self.driver.quit()
        except:
            pass

    def source(self,page):
        self.driver.get(page)
        return self.driver.page_source

    #get data in page
    #[{},{},{},{}]

    def outone(self,page,obj):
        self.driver.get(page)
        res = []
        datadict = {}
        for key in obj.__dict__:
            if isinstance(obj.__dict__[key], Field):
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, obj.__dict__[key].xpath)))
                elems = self.driver.find_elements_by_xpath(obj.__dict__[key].xpath)
                tmp = []
                for elem in elems:
                    if obj.__dict__[key].data == 'text':
                        data = elem.text

                    else:
                        data = elem.get_attribute(obj.__dict__[key].data)
                    tmp.append(data)

                datadict[key] = tmp

        res.append(datadict)
        return res
    def outmulti(self,page,obj):
        self.driver.get(page)
        res = []
        #get the wrap of data
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, obj.__dict__['wrap'].xpath)))
        wraps=self.driver.find_elements_by_xpath(obj.__dict__['wrap'].xpath)
        print(len(wraps))
        i=1
        while(i<=len(wraps)):
            datadict={}
            wrappath=obj.__dict__['wrap'].xpath+'[{}]'.format(i)

            for key in obj.__dict__:
                if key!='wrap':

                    if isinstance(obj.__dict__[key],Field):
                        elems=self.driver.find_elements_by_xpath(wrappath+obj.__dict__[key].xpath)
                        tmp=[]
                        for elem in elems:
                            if obj.__dict__[key].data == 'text':
                                data = elem.text

                            else:
                                data = elem.get_attribute(obj.__dict__[key].data)
                                if data == None:
                                    data=elem.get_property(obj.__dict__[key].data)
                            tmp.append(data)

                        datadict[key]=tmp

            res.append(datadict)
            i=i+1
        return res


def recur(obj,start,dir='.',title=False,content='content',next='next'):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    def out(page,obj):
        def do(page,obj):
            driver.get(page)
        res = []
        datadict = {}
        for key in obj.__dict__:
            if isinstance(obj.__dict__[key], Field):
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, obj.__dict__[key].xpath)))
                elems = driver.find_elements_by_xpath(obj.__dict__[key].xpath)
                tmp = []
                for elem in elems:
                    if obj.__dict__[key].data == 'text':
                        data = elem.text
                    else:
                        data = elem.get_attribute(obj.__dict__[key].data)
                    tmp.append(data)
                datadict[key] = tmp
        res.append(datadict)
        driver.close()
        driver.quit()
        return res
        try:
            res=do(start,obj)
            return res
        except Exception as e:
            print(e)
        finally:
            driver.close()
            driver.quit()
    con=out(start,obj)
    n=1
    os.chdir(dir)
    if title:
        title=con[0][title][0]
    else:
        title=str(n)
    with open(title+'.txt','wb') as f:
        f.write(con[0][content][0].encode(errors='ignore'))
    n=n+1
    while(con[0][next]):
        con=out(con[0][next][0],obj)
        try:
            with open(con[0][title][0]+'.txt','wb') as f:
                f.write(con[0][content][0].encode(errors='ignore'))
            n=n+1
        except Exception:
            with open(str(n)+'.txt','wb') as f:
                f.write(con[0][content][0].encode(errors='ignore'))
            n=n+1


def t1(x):
    print("t1:{}".format(x))
    def t2(x):
        print("t2:{}".format(x))
    x=x+1
    return t2(x)
if __name__=='__main__':
    class P1():
        title=Field('//*[@id="wrapper"]/div[5]/div/div[2]/h1')
        content=Field('//*[@id="content"]')
        next=Field('//*[@id="wrapper"]/div[5]/div/div[4]/a[4]','href')
    p='http://www.shubaoxsw.org/2_2741/296549.html'
    recur(P1,p,dir=r'F:\新建文件夹 (2)')
