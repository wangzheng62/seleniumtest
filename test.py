from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument(r'--user-data-dir=G:\Users\36357\AppData\Local\Google\Chrome\User Data')
chrome_options.add_argument(r'user-agent="Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36"')
chromedriver = r"G:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver.get(r"https://www.douyu.com/")
#assert "Python" in driver.title
print(driver.current_url)
print(driver.page_source)
elem = driver.find_element_by_class_name("HomeHeader-search")
#
actions=ActionChains(driver)
actions.move_to_element(elem)
actions.click(elem)
actions.perform()

print(driver.current_url)
print(driver.page_source)
elem1=driver.find_element_by_class_name('SearchPage-headerInput')
elem1.clear()
elem1.send_keys('牛叔')
elem1.send_keys(Keys.RETURN)

print(driver.current_url)
print(driver.page_source)
sleep(10)
print(driver.page_source)
#driver.refresh()
actions.click()
sleep(10)
print(driver.page_source)
elem2 = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="SearchResultAllAnchor-show"]/div[1]')))
actions.move_to_element(elem2)
actions.click(elem2)
actions.perform()

#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()