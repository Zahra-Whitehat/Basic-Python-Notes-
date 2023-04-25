first = open('C:/Users/zahra.dorostkar/Documents/MyPyCodes/a.txt','w')
first.write("Hey now brown cow \n")
first.write("this is a new line \n this is the third line")
first.close()
first = open('C:/Users/zahra.dorostkar/Documents/MyPyCodes/a.txt','r')
print(first.readline())

#اگر دوباره بازش نکنيم از ايندکس ادامه ي دستور قبلي روش کار ميکنه که در اينجا تهي ميده
first = open('C:/Users/zahra.dorostkar/Documents/MyPyCodes/a.txt','r')
print(first.read(3))

first = open('C:/Users/zahra.dorostkar/Documents/MyPyCodes/a.txt','r')
list1 = first.readlines()
list1[2] = "mmm I sure love bacon \n"
first = open('C:/Users/zahra.dorostkar/Documents/MyPyCodes/a.txt','w')
first.writelines(list1) 
first.close() 
