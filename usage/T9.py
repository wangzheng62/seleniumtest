from core.class2 import engine,save
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os,random
from urllib.request import Request,urlopen,urlretrieve
URL='https://cl.ze53.xyz/htm_data/2006/8/3980299.html'
data={'img':('//div["image-big"]/img','src')}
p="https://www.louimg.com/i/?i=u/20200623/12333259.png"
with engine() as e1:
    res=e1.getpng(URL,data)
    print(res)
    for i,png in enumerate(res['img']):
        with open('{}.png'.format(str(i)),'wb') as f:
            f.write(png)



