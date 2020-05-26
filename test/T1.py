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
print(chrome_options.arguments)
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument(r'--user-data-dir=G:\Users\36357\AppData\Local\Google\Chrome\User Data')
#chrome_options.add_argument(r'user-agent="Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36"')
chromedriver = r"G:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver.get(r"https://sou.zhaopin.com/?jl=719&kw=%E5%8E%A8%E5%B8%88&kt=3&sf=0&st=0")
#assert "Python" in driver.title
elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "contentpile__content__wrapper__item__info__box__welfare__item"))
    )
elems=driver.find_elements_by_class_name("contentpile__content__wrapper__item__info__box__welfare__item")
for e in elems:
    print(e.text)
driver.close()
driver.quit()

#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()