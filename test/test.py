from itertools import count,cycle,repeat
print(count(10).__next__())
print(cycle('abcd').__next__())
print(repeat(11,5).__next__())