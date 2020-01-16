from core.classdef import Job,Field
from core.funcdef import savexls,sav,savejson



#递归
def do(start,job,page):

    tmp=job.out(start,page)
    with open('女友的迷奸日记.txt','a') as f:
        f.write(tmp[0]['title'][0]+'\n')
        f.write(''.join(tmp[0]['content']))
    if tmp[0]['tag'][1]=='读完了':
        return '结束'
    np=tmp[0]['href'][1]
    return do(np)
#列表

def dolist(url,mainpage,page):
    j=Job()
    res=j.out(url,mainpage)
    print(res)
    with open('{}.txt'.format(res[0]['title'][0]),'ab') as f:
        for l in res[0]['href']:
            tmp=j.out(l,page)
            content=''.join(tmp[0]['content']).encode(encoding='utf8')
            f.write(content)
    return True

if __name__=="__main__":
    #job1
    '''
    class Next():
        title=Field('//*[@id="top"]/span','text')
        href=Field('//*[@id="pb_next"]','href')
        tag=Field('//*[@id="pb_next"]','text')
        content=Field('//*[@id="chaptercontent"]','text')
    j1=Job()
    start='http://m.avxs.cc/45839/1.html'
    l1=j1.out(start,Next)
    print(l1)
    do(start)'''
    #job2
    '''
    class Mainpage():
        title=Field('//div[@id="info"]/h1','text')
        href=Field('//ul[@class="_chapter"]/li/a','href')
    class Page():
        content=Field('//div[@id="content"]')
    url='http://www.sanhaoxs.net/html/1/1141/'
    dolist(url,Mainpage,Page)
    '''
    url='http://www.wuwuxs.com/5_5422/'
    class Mainpage():
        title=Field('//*[@id="info"]/h1','text')
        href=Field('//*[@id="list"]/dl/dd/a','href')
    class Page():
        content=Field('//*[@id="content"]')
    dolist(url,Mainpage,Page)
