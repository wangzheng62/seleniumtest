from openpyxl import Workbook
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