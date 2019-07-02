import re,numpy,os


def ma(s):
    pattern = r'[\u4e00-\u9fa5]'
    p = re.compile(pattern)
    l = p.findall(s)
    return l
def hhh(f):
    with open(f,'rb') as f:
        bs=f.read()
        try:
            s=bs.decode(encoding='utf8')
        except:
            s=bs.decode(encoding='gbk')
        #s=bs.decode(encoding='gbk',errors='ignore')
        l=ma(s)
        print(len(l))
        #print(l)
        res={'char':[],'num':[]}
        for c in l:
            if c not in res['char']:
                res['char'].append(c)
                res['num'].append(1)
            else:
                i=res['char'].index(c)
                res['num'][i]=res['num'][i]+1
        #print(res)
        ll=[res['char'],res['num']]
        for index,n in enumerate(ll[1]):
            ll[1][index]='{:0>4}'.format(n)
        a=numpy.asarray(ll)


        b=a.argsort(axis=1)

        c=[[],[]]
        for index in b[1]:
            c[0].append(ll[0][index])
            c[1].append(ll[1][index])
        d=numpy.asarray(c)
        print(c[0][-50:])
        print(c[1][-50:])
if __name__=='__main__':
    path=r'F:/新建文件夹 (2)/文本/cooked/s/'
    l=os.walk(path)
    os.chdir(path)
    for fs in l:
        print(fs)
        os.chdir(fs[0])
        for f in fs[2]:
            hhh(f)
