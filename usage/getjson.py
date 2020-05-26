import json,os
from core.funcdef import savexls
pwd=os.getcwd()
print(pwd)
filename='666'
with open(pwd+'/{}.json'.format(filename),'rb') as f:
    l=[]
    d=json.load(f)
    print(d["data"]["results"][0])
    for i in d["data"]["results"]:
        print("{} {} {} {} {}".format(i['jobName'],i["company"]['name'],i['salary'],i['welfare'],i['positionURL']))
        tmp={}
        tmp['jobName']=i['jobName']
        tmp['salary']=i['salary']
        tmp['companyName']=i["company"]['name']
        tmp['welfare']=i['welfare']
        tmp['positionURL']=i['positionURL']
        l.append(tmp)

savexls(l,'666')