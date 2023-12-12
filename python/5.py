print([i for i in dir(__builtins__) if "Error" in i])

try:
    a = 1+'1'
except TypeError:
    print("type error")

try:
    a = 1/0
except ZeroDivisionError:
    print("zero divison error")

try:
    import y
except ImportError:
    print("import error")

try:
    l =[1,2,3]
    l[4]
except IndexError:
    print("index error")

try:
    l ={1:1,2:2,3:3}
    l[4]
except KeyError:
    print("key error")

try:
    with open("meow.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found error")

try:
    a = 1/0
except ArithmeticError:
    print("arithmatic error")
try:
    class Person:
        pass
    Person.new
except AttributeError:
    print("attribute error")

try:
    l =[1,2,3]
    l[4]
except LookupError:
    print("lookup error")

try:
    int("Meow")
except ValueError:
    print('value error')

class DivisorOfTwoError(Exception):
    pass

try:
    a = 4
    if a%2 == 0:
        raise DivisorOfTwoError
except DivisorOfTwoError:
    print("divided by two error")