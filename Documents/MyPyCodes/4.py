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

print(func1("Tony"))
print(func2(6))
func3("Ali", "Zare")
func4()
func4("Samira", "Gholipour")
func4('Shahnaz')
func4(y = "Zare")
func5("apple")
