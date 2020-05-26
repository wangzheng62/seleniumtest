from core.classdef import Job,Field
from core.funcdef import savexls,sav,savejson
from jieba  import lcut
class Work():
    wrap=Field('//div[@id="listContent"]/div')
    href=Field('//div[@class="contentpile__content__wrapper__item clearfix"]/a','href')
    cname=Field('//a[@class ="contentpile__content__wrapper__item__info__box__cname__title company_title"]','title')
    jobname=Field('//span[@class="contentpile__content__wrapper__item__info__box__jobname__title"]','text')
    saray=Field('//p[@class="contentpile__content__wrapper__item__info__box__job__saray"]','text')
    welfare=Field('//div[@class="contentpile__content__wrapper__item__info__box__welfare job_welfare"]/div','text')
class Info():
    address=Field('//span[@class ="job-address__content-text"]')
    details=Field('//div[@class ="describtion__detail-content"]/p')
def fpass():
    pass
def fstop():
    pass
if __name__=='__main__':
    ss=['中国平安人寿保险股份有限公司河南分公司优才之家团队']
    fliterkey=['保险','诺万信息','未之来','平安','中科院']
    flitersaray=['2','3','4']
    fliterwelfare=['']
    for key in fliterkey:
        if key in ''.join(ss):
            print('hahaha')


    #chef
    p1='https://sou.zhaopin.com/?jl=719&kw=%E5%8E%A8%E5%B8%88&kt=3&sf=0&st=0'
    #data
    p01='https://sou.zhaopin.com/?jl=719&sf=0&st=0&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3'
    p02='https://sou.zhaopin.com/?jl=719&sf=0&st=0&kw=%E8%B0%B7%E6%AD%8C&kt=3'
    j1 = Job()
    l1 = j1.out(p1, Work)

    print(l1)

    i=2

'''   while(i<=20):
        p='https://sou.zhaopin.com/?p={}&jl=719&sf=0&st=0&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3'.format(i)
        j=Job()
        try:
            d=j.out(p,Work)
            res=res+f(d)
        except:
            break
        i=i+1
    savexls(res,123)'''

