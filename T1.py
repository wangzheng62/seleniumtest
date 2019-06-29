from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument(r'--user-data-dir=G:\Users\36357\AppData\Local\Google\Chrome\User Data')
#chrome_options.add_argument(r'user-agent="Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36"')
chromedriver = r"G:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver.get(r"http://www.xinyushuwu.com/4/4834/")
#assert "Python" in driver.title
elems=driver.find_elements_by_xpath('//div[@class="ml_list"]/ul/li/a')

path=r"F:/新建文件夹 (2)/文本/"
urls=[]
for e in elems:
    url=e.get_attribute('href')
    urls.append(url)

for url in  urls:
    driver.get(url)
    title=driver.title
    content=driver.find_element_by_id('articlecontent').text
    with open(path+'{}.txt'.format(title),'w') as f:
        f.write(content)
driver.close()



#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()