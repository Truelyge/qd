from datetime import datetime
import time


print(datetime.now())

a1 = datetime.now()
print(a1)
print(type(a1))
# time.sleep(6)
a2 = datetime.now()
print(a1, a2, a2 - a1)
a = a2 - a1
print(a.days, a.seconds)
# print(float(a1),float(a2))
# print(float(a2-a1))


print(a2.year,a2.month,a2.day)
a="2018-7-1"
b="2018-7-31"
c="2018-6-31"
print(a>b)
print(a>c)
print(str(2018)>"2017")
