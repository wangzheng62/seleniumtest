from core.classdef import Job,Field
from core.funcdef import savexls,sav,savejson

class T():
    title=Field('//div[@id="list"]/dl/dd','text')
    href=Field('//div[@id="list"]/dl/dd/a','href')
class Con():
    tt=Field('//div[@id="content"]','text')
if __name__=="__main__":
    j1=Job()
    p1='http://www.dlhtxs.com/27/27061/'
    l1=j1.out(p1,T)
    print(l1)
    for n,h in zip(l1[0]['title'],l1[0]['href']):
        con=j1.out(h,Con)[0]['tt'][0]
        f=open('{}.txt'.format(n),'w')
        f.write(con)
        f.close()
