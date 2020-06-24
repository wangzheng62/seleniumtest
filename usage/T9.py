from core.class2 import engine,save
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os,random
from urllib.request import Request,urlopen,urlretrieve
URL='http://www.zhuoku.com/zhuomianbizhi/star-starcn/20190917154159(8).htm#turn'
data={'img':('//img[@id="imageview"]','src')}
d1={'img':('//div[@class="image-big"]','src')}
p="https://cl.ze53.xyz/htm_data/2006/8/3980299.html"
with engine() as e1:
    res=e1.getpng(p,d1)
    print(res)
    for i,png in enumerate(res['img']):
        with open('{}.png'.format(str(i)),'wb') as f:
            f.write(png)



