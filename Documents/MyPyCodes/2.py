
##########################نکات پايتون مقدماتي################################

import math

#دريافت از ورودي، هر نوعي مي تواند باشد.
number = int(input('give me a number: '))
print(type(number))

#هرچه ميخواهيم ناديده گرفته شود از \ استفاده ميکنيم.
name = input(" write down\" your name\"")
print(type(name))
h = "Hi dear"

x = 10
y = 25
# تبديل int به string
x2 = str(x)
y2 = '45'

#ميتوان يک تابع را ايجاد کرد و در يک متغير ريخت و بعد ازش بارها استفاده کرد.
t = math.sqrt
list1 = ['aa','bb','cc','dd','ee']
list2 = "zahra"
list3 = [0,1,2,3,4,5,6,7,8,9]
list4 = [7,8,56,3,12]
#تاپل مثل ليست است ولي هيچ کاري جز صدازدن عناصرش نميتوان کرد.
tuple1 = (2,5,1,'g')

print(number*x + y)
print(pow(number,5))
print(math.floor(15.7))
print(t(number**y))
# چسباندن دو رشته
print(h + name)
# ساخت يک دنباله( نه يک رشته) از رشته ها
print(h , name)
print(x2 + y2)
# ساخت يک ليست x تايي از عنصر y .
print([y]* x)
print(list1[3])
print(list1[-2])
print(list2[2])
print(list3[:5] + list1[-3:] + list3[-4:-1] + list1[:])
print(list3[1:8:2])
print(list3[10:0:-2])
#تکرار يک ليست يا رشته
print(list3[::-2]*3)
print(list2*3)
#اين تابع به صورت مستقيم در پرينت کار نمي کند.
list3.append(10)
print(list3)
print(list3.count(3))
#اين تابع به صورت مستقيم در پرينت کار نمي کند.
list1.extend(list3)
print(list1.index(8))
list1.insert(3,'asb')
print(list1.pop(5))
list1.remove(8)
print(list1)
list1.reverse()
print(list1)
#اين تابع به صورت مستقيم در پرينت کار نمي کند.
list4.sort()
print(list4)
print(sorted(list2))
print('z' in list2)
print('a' in list1)
print(tuple1[2])






input("Press<Enter>")
