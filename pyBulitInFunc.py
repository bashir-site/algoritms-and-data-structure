
print("1.abs()")
list1 = [1, -6,-7, -9]

for i in range(len(list1)):
    print(abs(list1[i]))


print("2. all()")
list2 = [3,4,3,4,3,4,4,5]
print(all(list2))
print(all(a == 4 or a == 3 for a in list2))


print("3. any()")
list3 = [False,0,0,0,False,0,0]

print(any(list3))

print("4. ascii()")
print(ascii('4"абвгд'))

print("5. bin()")
print("bin(1): ",bin(1))
print("bin(2): ",bin(2))
print("bin(3): ",bin(3))
print("bin(-4): ",bin(-4))
print("bin(44): ", bin(44))
print("hex(4): ", hex(4))
print("bin(0x4): ", bin(0x4))
print("type(bin(4)): ",type(bin(4)) )

print("6. bool()")
print(bool(1), bool(0), bool(6==7), bool(6>7), bool(6>=6))

print("7. breakpoint()")
for i in range(10):
    print('i= ', i)

    if i == 5:
        breakpoint()

print("8. bytearray()")
print(bytearray([1,2,3,4]))
print(bytearray('Башир', 'UTF-8', 'strict'))
print(bytearray('Башир', 'ascii', 'ignore'))
print(bytearray('Башир', 'ascii', 'replace'))

print("9. bytes()")
print(bytes('hey', 'UTF-8'))
print(bytes('hey', 'UTF-16'))
print(bytes('hey', 'UTF-32'))
print(bytes(1))
print(bytes(4))
print(bytes([1,2,3,4]))

print("10. callable()")
print(callable('hey'))
print(callable(4))
class foo2:
    def __init__():
        return 2+4
print(callable(foo2))

print("11. chr()")
print(chr(0))
print(chr(1114111))
print(chr(98), chr(97), chr(36))

list2 = []
def func1(str2):
    for i in str2:
        list2.append(ord(i))
    print(list2)
    return list2

def func2(myList):
    newString = ''
    for i in myList:
        newString += chr(i)
    print(newString)

func2(func1("my name is Bashir"))

print("12. @classmethod")
class Car:
    def __init__(self, features):
        self.features = features

    def __repr__(self):
        return f'Car ({self.features})'

    @classmethod
    def truck(cls):
        return cls(['Highbeams', '4x4', 'Big Tires'])
    
    @classmethod
    def sport(cls,package):
        if package == 'SRT':    
            return cls(['300hp', '2x4', 'Sport Tires'])

newCar = Car.sport("SRT")
print('newCar', newCar)

print("13. compile()")
x = '5'
code = compile('x == "5"', '', 'eval')
print(type(code))
result = eval(code)
print(result)

print("14. complex()")
print(complex(0))
print(complex(1))
print(complex(2))
print(complex(0, 1))
print(complex(1, 1))
a = complex(1,3)
print(a)
print(a.real)
print(a.imag)

print("15. delattr()")
class Jeep:
    hp =  300
    model = "Wrangler"

delattr(Jeep, 'hp')
for j_keys, j_values in Jeep.__dict__.items():
    if not j_keys.startswith("__"):
        print(j_keys, j_values)

print("16. dict()")
print(dict())
print(dict(a=1, b=2))
print(dict(a=1, b = {'c': 5}))
print({'a': 1, 'b':3})
print(dict([('a', 2), ('b', 9)], c = 3))
print(dict(zip(['a', 'b'], [1,2]), c =54))

print("17. dir()")
print("Dictionary: ", dir({}))
print()
print("Tuple: ", dir(()))
print()
print("List: ", dir([]))
print()
class Jeep:
    hp = 300
    model = "Wrangler"
    print("Class: ", dir(Jeep))

print("18. divmod()")

print('divmod(10,2)', divmod(10, 2), 'or', 10//2, 10%2)
print('divmod(10,3)', divmod(10, 3), 'or', 10//3, 10%2)
print(divmod(10, 4), 'or', 10//4, 10%4)

print("19. enumerate()")

countries = ['Canada', 'USA', 'Mexico']
print(list(enumerate(countries)))
for i in enumerate(countries, 10):
    print(i)

print("20. eval()")
print(eval('1'))
print(eval('-1'))
print(eval('4 + -1'))
x = 9
print(eval('x + 10'))

print(eval('abs(-10)'))
print(eval('print("Hello world!")'))

print("21. exec()")
print(exec("print(1)"))
exec('def testFunc(): print(min(10,1))')
print(testFunc())
a = exec("print(1)", {"__builtins__": None}, {"print": print})
print(a)

print("22. filter()")
ages = [0, 0, 5, 17, 18, 24]

def myFunc(x):
    return x>=18

print(list(filter(myFunc, ages)))
print(list(filter(None, ages)))
print(list(filter(lambda x: x>=18, ages)))

print("23. float()")
print(float("+1.5"), float("-1.5"))
print(float(+5), float(-5))

a = "5.05"
print('type a', type(a))
try:
    a = float(a)
except:
    pass
print('type a', type(a))

print('24. format()')
print(format(5, '%'))
print(format(5, '.1%'))
print(format(5, '.2%'))
print(format(5, 'f'))
print(format(5, '.2f'))
print(format(5, '.1f'))
print(format(5, 'e'))
print(format(5, '.1e'))
print(format(5, '.2e'))

print("25. frozenset()")
a = frozenset([1,2,3,4,5])
print(a)
print(frozenset("hey"))
#print(frozenset([1,3], frozenset()))

print("26. getattr()")
class Jeep:
    hp = 300
    model = "Wrangler"
    @staticmethod
    def my_method():
        return 'beep beep!'
print(getattr(Jeep, 'hp'))
#print(getattr(Jeep, my_method()))

print("27. globals()")
a = 6
b = 9
print(globals())
print(globals()['b'])

print('28. hasattr()')


