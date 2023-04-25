bucky = "Hey there %s, how is %s ?"
highlow = 'Hi You, How you Doing?'
NameDic = {'Dad' : 'John' , 'Mom' : 'Maria' , 'Bro' : 'Joey'}
AgeDic = {'Dad' : 42 , 'Mom' : 48 , "Sis" : 15}
var1 = ('Betty' , 'foot')
var2 = ('Zari' , 'Hand')
sequence = ['hey', 'there', 'Ali', 'guy']
glue = 'you'
print(bucky % var1)
print(bucky % var2)
print(bucky.find('is'))
print(glue.join(sequence))
print(highlow.lower())
print(highlow.replace('Doing' , 'go'))
print(NameDic['Dad'])
print(AgeDic['Dad'])
#print(NameDic.clear())
print(AgeDic.copy())
#print(AgeDic.has_key('Apple'))
#print(AgeDic.has_key('Mom'))



Animal = "reptar"
if Animal == 'Tuna':
    print('It is a fish')
elif Animal == 'sparrow':
    print ('It is a bird')
else:
    print('I don\'t know')


thing = "bike"
if thing == "car" or thing < "motor":
    if thing == "bus":
        print('it is  a bus')
    elif thing != "bike":
        print ("comes in the first half of dictionary")
    else:
        print('it isn\'t a vehicle')
else:
    print("I am not sure what it is")



list1 = ["bread", "meat", "egg", "milk"]
for food in list1:
    print(" I Love " + food)


for item in AgeDic:
    print( item, AgeDic[item] )


while 1:
    name = input(" Enter your name : ")
    if name == "Done":
        break

    



