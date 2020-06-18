from openpyxl import Workbook
from itertools import chain
from core.classdef import Job
import os
#function about excel
def savexls(l,filename):
    # [{},{},{},{}]
    wb=Workbook()
    ws=wb.active
    for d in l:
        tmp = []
        for key in d:
            s=" ".join(d[key])
            tmp.append(s)
        ws.append(tmp)
    wb.save('{}.xlsx'.format(filename))
def sav(l,filename):
    # [{},{},{},{}]
    wb = Workbook()
    ws = wb.active
    for i in chain.from_iterable(l):
        print(i)

import json
def savejson(l,filename):
    # [{},{},{},{}]
    with open("{}.json".format(filename),'a',encoding='utf8') as f:
        for d in l:
            f.write(json.dumps(d))

#遍历方法
#Traverse tree
#recursion
def recur(obj,start,dir='.',title=False,content='content',next='next'):
    j1=Job()
    con=j1.out(start,obj)
    n=1
    os.chdir(dir)
    if title:
        title=con[0][title][0]
    else:
        title=str(n)
    with open(title+'.txt','wb') as f:
        f.write(con[0][content][0].encode(errors='ignore'))
    n=n+1
    while(con[0][next]):
        con=j1.out(con[0][next][0],obj)
        try:
            with open(con[0][title][0]+'.txt','wb') as f:
                f.write(con[0][content][0].encode(errors='ignore'))
            n=n+1
        except Exception:
            with open(str(n)+'.txt','wb') as f:
                f.write(con[0][content][0].encode(errors='ignore'))
            n=n+1