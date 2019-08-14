from classdef import Job,Field,Do
from openpyxl import Workbook
import numpy as np
class Chef():
    wrap=Field('//div[@id="listContent"]/div')
    href=Field('//div[@class="contentpile__content__wrapper__item clearfix"]/a','href')
    jobname=Field('//span[@class="contentpile__content__wrapper__item__info__box__jobname__title"]','text')
    saray=Field('//p[@class="contentpile__content__wrapper__item__info__box__job__saray"]','text')
    welfare=Field('//div[@class="contentpile__content__wrapper__item__info__box__welfare job_welfare"]/div','text')
def wt(d,name):


    wb=Workbook()
    ws=wb.active
    tmp=[]
    for key in d:
        tmp.append(d[key])
    a=np.array(tmp)
    at=a.T.tolist()
    for row in at:
        ws.append(row)
    wb.save('{}.xlsx'.format(name))


if __name__=='__main__':
    p1='https://sou.zhaopin.com/?jl=719&kw=%E5%8E%A8%E5%B8%88&kt=3&sf=0&st=0'
    p3='https://sou.zhaopin.com/?p={}&jl=719&kw=%E5%8E%A8%E5%B8%88&kt=3&sf=0&st=0'
    j1 = Job()
    dir1 = j1.out(p1, Chef)
    #wt(dir1,1)
    i=2
    #while(i<=10):
    #    p='https://sou.zhaopin.com/?p={}&jl=719&kw=%E5%8E%A8%E5%B8%88&kt=3&sf=0&st=0'.format(i)
    #    j=Job()
    #    d=j.out(p,Chef)
     #   wt(d,i)
     #   i=i+1
