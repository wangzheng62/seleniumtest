from core.classdef import Job,Field


class P1():
    content=Field('//div[@class="mcc"]')
n=746
j1=Job()
with open('nn2.txt','ab') as f:
    while(n<=755):
        p="http://www.shubao202.com/read/105803/{}".format(n)
        print(p)
        con=j1.out(p,P1)
        print(con)
        f.write(con[0]['content'][0].encode(errors='ignore'))
        n=n+1
