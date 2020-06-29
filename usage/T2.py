from core.class2 import engine
p='https://www.jd.com/'
with engine(notgui=False) as e:
    e.testurl(p)