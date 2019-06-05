from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chromedriver = r"G:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver.get(r"http://www.xiaoshuo777.net/files/article/html/9/9803/index.html")
#assert "Python" in driver.title
elems = driver.find_elements_by_xpath("//li[@style='width:24%;']/a")
l=[]
t=[]
for e in elems:
    l.append(e.get_attribute('href'))
    t.append(e.get_attribute('title'))
print(l)
path='d:/'

for i,h in enumerate(l):
    driver.get(h)
    elem=driver.find_element_by_xpath('//div[@class="novel_content"]')
    txt=elem.text
    f=open(path+'{}.txt'.format(t[i]),'w')
    f.write(txt)
    f.close()

#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()