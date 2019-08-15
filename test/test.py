from itertools import count,cycle,repeat,groupby,filterfalse
print(count(10).__next__())
print(cycle('abcd').__next__())
print(repeat(11,5).__next__())
l=[list(g) for k, g in groupby('AAAABBBCCD')]
print(l)
for i in filterfalse(lambda x: x%2, range(10)):
    print(i)