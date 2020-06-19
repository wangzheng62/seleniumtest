from core.class2 import engine,save
import os

data={'title':('//*[@id="wrapper"]/div[5]/div/div[2]/h1','text'),
      'content':('//*[@id="content"]','text'),
      'next':('//*[@id="wrapper"]/div[5]/div/div[4]/a[4]','href')}
data1={'title':('//*[@id="wrapper"]/div[5]/div/div[2]/h1','text'),
       'content':('//*[@id="content"]','text'),
       'next1':('//*[@id="wrapper"]/div[5]/div/div[4]/a[4]','href')}

p=['http://www.shubaoxsw.org/15_15522/1260320.html',
   'http://www.shubaoxsw.org/15_15301/1252776.html',
   'http://www.shubaoxsw.org/4_4846/412929.html',
   'http://www.shubaoxsw.org/2_2061/194401.html',
   'http://www.shubaoxsw.org/2_2053/192745.html',
   'http://www.shubaoxsw.org/0_467/146037.html',
   'http://www.shubaoxsw.org/8_8940/490410.html']

dir=r'F:\新建文件夹 (2)'
for index,url in enumerate(p):
    os.chdir(dir)
    os.mkdir(str(index))
    os.chdir(dir+'/'+str(index))
    with engine() as e1:
        print(e1.recuv(url,data,func=save))