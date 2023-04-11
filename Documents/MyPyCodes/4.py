def func1 (x):
    return "What\'s up " + x

def func2 (x):
    return x+10

def func3(x,y):
    print("%s %s" % (x,y))
    
#تابعي که مقدار پيشفرض دارد.
def func4(x = "Mohammad", y = "Ghorbani"):
    print("%s %s" % (x,y))

#يک ليست خالي ميسازد که ميتوان تعداد نامعيني عنصر به آن اضافه کرد.
def func5(*param):
    print(param)

#وقتي براي يکي از پارامترها نميدانيم چه تعداد مقادير داريم و آنها را به صورت يک ليست ذخيره ميکنيم.
def func6(name, *ages):
    print(name,ages)

#مثل مورد قبل ولي به صورت ديکشنري
def func7(**items):
    print(items)

def useless_func8(first,last,*ages,**items):
    print(first,last)
    print(ages)
    print(items)

def func9(x,y,z):
    return x*y+z

def func10(**this):
    print(this)

    
print(func1("Tony"))
print(func2(6))
func3("Ali", "Zare")
func4()
func4("Samira", "Gholipour")
func4('Shahnaz')
func4(y = "Zare")
func5("apple")
func6("Aslan" , 15,17, 62, 28,83)
func7(apple = 5 , peach = 7 , beef = 9)
useless_func8("bucky", "roberts", 24, 23, 45, 84, 12, bacon = 4, souce = 65)
num = (5,6,2)
print(func9(*num))
dic1 = {"book" : 154, "notebook" : 123, "pen" : 87}
func10(**dic1)
func10
