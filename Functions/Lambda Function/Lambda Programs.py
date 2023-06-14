#sort tuple
tuple = [('mi',20),('rr',18),('gt',16),('csk',14)]
tuple.sort(key=lambda  a:a[0])
print(tuple)

#program to sort a list of dict using lambda
dict1 = [{'a':5,'z':10,'k':7},{'a':6,'k':12,'z':31},{'k':61,'a':12,'z':21}]
sorted_dict = sorted(dict1,key = lambda x:x['a'])
print(sorted_dict)

#to extrac year,month,date and time using lambda
#2022-01-15 09;03:32
import datetime

now = datetime.datetime.now()
print(now)
year = lambda x:x.year
month = lambda x:x.month
day = lambda x:x.day
t = lambda x:x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))

