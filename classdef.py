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
        chrome_options.add_argument("--disable-gpu")
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
    def out(self,page,obj):
        self.driver.get(page)
        res = []
        if 'wrap' in obj.__dict__:
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
                                tmp.append(data)

                            datadict[key]=tmp

                res.append(datadict)
                i=i+1
        else:
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


class Do(Job):
    pass



#
class Dir():
    title=Field('//div[@class="tt"]/h3/a','text')
    url=Field('//div[@class="tt"]/h3/a','href')
    next=Field('//a[@class="next"]','href')

class Url():
    title=Field('//div[@class="ml_list"]/ul/li/a','text')
    url=Field('//div[@class="ml_list"]/ul/li/a','href')
class Artcle():
    title=Field('//div[@class="nr_title"]/h3','text')
    content=Field('//p[@id="articlecontent"]','text')

#
class Li():
    title=Field('//dl[@class="chapterlist"]/dd/a','text')
    url=Field('//dl[@class="chapterlist"]/dd/a','href')
class Artcle01():
    content=Field('//div[@id="BookText"]','text')
    next=Field('//div[@class="link xb"]/a[3]','href')
    nexttext=Field('//div[@class="link xb"]/a[3]','text')

if __name__=='__main__':

    p1=r"http://www.xinyushuwu.com/4/4834/"
    p2=r'http://www.xinyushuwu.com/lawen/1.html'
    p3=r'https://www.31bz.org/9_9669/'
    p4=r'https://www.31bz.org/9_9669/0.html'
    j1=Job()
    dir1=j1.out(p3, Li)
    print(dir1)
    os.chdir('d:/')
    for index,url in enumerate(dir1['url']):
        tmp=j1.out(url,Artcle01)
        title=dir1['title'][index]
        while(tmp['nexttext'][0]=='下一页'):
            f=open('{}.txt'.format(title),'a')
            f.write(tmp['content'][0])
            f.close()
            tmp=j1.out(tmp['next'][0],Artcle01)
        f = open('{}.txt'.format(title), 'a')
        f.write(tmp['content'][0])
        f.close()


    dir2=j1.out(p4,Artcle01)
    print(dir2)


    def ma(s):
        pattern = r'[-\(\)\d\w\u4e00-\u9fa5]'
        p = re.compile(pattern)
        l = p.findall(s)
        res = ''.join(l)
        return res
    def dd(dir):
        i=0
        root='F:/新建文件夹 (2)/test/'
        os.chdir(root)
        while(i<len(dir['title'])):
            path=dir["title"][i]
            try:
                os.mkdir(path)
            except Exception as e:
                print(e)
                break
                print(path)
                path=ma(path)
                try:
                    os.mkdir(path)
                except:
                    path=ma(dir['url'][i])
                    os.mkdir(path)
            ##
            os.chdir(path)
            urls=j1.out(dir['url'][i],Url)
            for url in urls['url']:
                data=j1.out(url,Artcle)
                title=data['title'][0]
                content=data['content'][0]
                title=ma(title)
                with open('{}.txt'.format(title),'w') as f:
                    try:
                        f.write(content)
                    except:
                        tmpb = content.encode('gbk', errors='ignore')
                        content = tmpb.decode('gbk', errors='ignore')
                        f.write(content)
            os.chdir(root)
            i=i+1
        ##
        next = dir['next'][0]
        dir = j1.out(next, Dir)
        return dd(dir)


    #dir1 = j1.out(p2, Dir)
    #dir=j1.out(p2,Dir)
    #dd(dir1)

    j1.driver.quit()




