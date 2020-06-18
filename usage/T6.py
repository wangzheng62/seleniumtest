p='http://www.shubaoxsw.org/2_2741/296549.html'
from core.classdef import Job,Field
from core.funcdef import recur

class P1():
    title=Field('//*[@id="wrapper"]/div[5]/div/div[2]/h1')
    content=Field('//*[@id="content"]')
    next=Field('//*[@id="wrapper"]/div[5]/div/div[4]/a[4]','href')
recur(P1,p,dir=r'F:\新建文件夹 (2)')

if __name__=='__main__':
    n=1
    def test():
        global n
        if True:
            pass
        else:
            pass
        print(n)