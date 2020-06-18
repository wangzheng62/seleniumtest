p='https://www.rousewu.info/read/26412/3473318/'
from core.classdef import Job,Field

class P1():
    content=Field('//*[@id="main"]/div[2]/div[1]/p[4]')
    next=Field('//*[@id="main"]/div[2]/div[3]/a[4]','href')
j1=Job()
con=j1.out(p,P1)
print(con)
n=1
with open(str(n)+'.txt','wb') as f:
    f.write(con[0]['content'][0].encode(errors='ignore'))
n=n+1
while(con[0]['next']):
    con=j1.out(con[0]['next'][0],P1)
    with open(str(n)+'.txt','wb') as f:
        f.write(con[0]['content'][0].encode(errors='ignore'))
    n=n+1