from core.classdef import Job,Field
from core.funcdef import savexls,sav,savejson
class Work():
    wrap=Field('//div[@id="listContent"]/div')
    href=Field('//div[@class="contentpile__content__wrapper__item clearfix"]/a','href')
    cname=Field('//a[@class ="contentpile__content__wrapper__item__info__box__cname__title company_title"]','title')
    jobname=Field('//span[@class="contentpile__content__wrapper__item__info__box__jobname__title"]','text')
    saray=Field('//p[@class="contentpile__content__wrapper__item__info__box__job__saray"]','text')
    welfare=Field('//div[@class="contentpile__content__wrapper__item__info__box__welfare job_welfare"]/div','text')
if __name__=='__main__':
    #chef
    p1='https://sou.zhaopin.com/?jl=719&kw=%E5%8E%A8%E5%B8%88&kt=3&sf=0&st=0'
    #data
    p01='https://sou.zhaopin.com/?jl=719&sf=0&st=0&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3'
    j1 = Job()
    l1 = j1.out(p01, Work)

    savexls(l1,1)
    i=2
    while(i<=20):
        p='https://sou.zhaopin.com/?p={}&jl=719&sf=0&st=0&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3'.format(i)
        j=Job()
        d=j.out(p,Work)
        savexls(d,i)
        i=i+1

