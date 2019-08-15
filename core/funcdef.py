from openpyxl import Workbook
from itertools import chain
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
