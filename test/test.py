import jieba
seg=jieba.lcut('中国平安人寿保险股份有限公司河南分公司优才之家团队',cut_all=True)
print(seg)
fliterkey=['保险','诺万信息','未之来','平安','中科院']
s=set(seg)
s1=set(fliterkey)
print(s)
print(s1)
d=s&s1
print(len(d))