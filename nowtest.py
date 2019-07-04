
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from json import dumps
from time import sleep
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument(r'user-agent="Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36"')
driver = webdriver.Chrome(chrome_options=chrome_options)
#
#u2=r'https://www.google.com/flights#flt=LAX.LHR,LGW,CDG,ORY,ARN.2019-09-05*BCN,MAD,FRA,GVA,FCO.LAX.2019-09-24;c:USD;e:1;so:1;sd:1;t:f;tt:m'
#driver.get(u2)
#print(driver.get_cookies())
#driver.delete_all_cookies()
d={
'1P_JAR':r'2019-07-03-07',
'ANID': r'AHWqTUkm8n9siBzdjnPmnQ8hRLlj3UjSaetbyhZDUOZSsITMGYctihVNLfaMPA46',
'APISID':r'k5Sgy3VPFtpsSRjr/Abw1cvjAUzcNmXIyS',
'CONSISTENCY':'AKJVzcqvFbttBjvzMTYi9NqLaH7e0MlDfSb8XvEeQYO5o2ygxy722SIjFTWmjIKNaupeP1N5o_WKzdXc9PPtJQHOZpn9nNTW6S11-Eduo1400MT-5nfgqCkDaaekHKd_DpuZI5w_X_NI',
'DV':r'o9Yoxo844PwnsLVGvYba-S9_jWZsu5ZAM0G0z9_5IwAAAAA',
'HSID':r'A0fGxjvflWcvPebYL',
'NID':r'187=R54R3H7eQcmxNlmJ8Io8eczJfeqpfVD2o8VK02WB6jlG7cZmR9_BZBdGBkre_NOXZCN1qXg5eAXmXcTW3PCpoZwZKeUiwCQ1Yy6pTFK8YwH901xnUcbZWyRS4dLzDnk6zEQeZltcmzENF2yRhH9T0zoB5qDz5v6ivOVDVHrKmRjdYiZ8mUphB0dLoC1FrprfAYb0Lk0rB1r9fJVoQrRijSnm',
'SAPISID':'leJaKUdIq_zC6kpx/Alj_BXpi34Cbqany9',
'SID':'lAdje08OA71eNSBbJ_RivuwWEH2x9jlpQGzhoC5zJLt0GsR8l9mE4FjwLeBh8dgK9TWHSg.',
'SIDCC':'AN0-TYtYRH6f6_LHMCSRNMJS9YrcNYOrjE8k9_J-dEzcZxiJHeQUae6bhAVAVXOrH2FvdxB4',
'SSID':'AuOAp1lBYwgAhH-Z2'
}
d1={'domain': '.google.com', 'expiry': 1577953201.380879, 'httpOnly': True,  'path': '/', 'secure': False}
for (key,value) in d.items():
    tmp=d1
    tmp['name']=key
    tmp['value']=value
    #driver.add_cookie(tmp)
actions = ActionChains(driver)
if __name__=='__main__':
    u1=r'http://www.w3school.com.cn/xpath/xpath_syntax.asp'
    u2=r'https://www.google.com/flights#flt=LAX.LHR,LGW,CDG,ORY,ARN.2019-09-05*BCN,MAD,FRA,GVA,FCO.LAX.2019-09-24;c:USD;e:1;so:1;sd:1;t:f;tt:m'
    #driver.implicitly_wait(20)
    driver.get(u2)
    e=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@target="_top"]')))
    print(e.text)
    actions.move_to_element(e)
    actions.click(e)
    actions.perform()
    #sleep(60)
    e1=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]')))
    #elems=driver.find_elements_by_xpath('//span[@class="gws-flights__ellipsize"]/span/span')
    print('222')
    print(e1.text)
    e1.send_keys('wz363579018@gmail.com')
    e2=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="identifierNext"]')))
    e2.click()
    e3 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]')))
    e3.send_keys('w4852358')
    e4=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="passwordNext"]')))
    e4.click()
    tt = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@type="text"]')))
    w=input("输入验证码:")
    print(w)
    tt.send_keys(w)
    e3.send_keys('w4852358')
    e4.click()

    '''
    print(len(elems))
    for e in elems:
        print(e.text)
    with open('test.html','wb') as f:
        f.write(driver.page_source.encode()'''
    #elem1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@jstcache="8892"]')))
    #print(elem1)
    sleep(10)
    driver.refresh()
    sleep(100)
    driver.close()
    driver.quit()