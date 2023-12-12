# # Datatypes
print(type(1)) # int
print(type(1.2)) # float
print(type(1+2j)) # complex

print(type([1,2])) # list
print(type((1,2))) # tuple
print(type("hem")) # string
print(type({1:1,2:2})) # dictionary
print(type({1,2})) # set
print(type(True)) # boolean

# # Operators
print(1+2, 1-2, 1*2, 1/2, 1//2, 1**2) # arithmatic
print(1 and 0, 1 or 0, not 1) # logical
print(1<2, 1>2, 1<=2, 1>=2, 1==2, 1!=2) # comparison

a = 1
a += 1
a -= 1
a *= 1
a /= 1
a //=1
a **= 1
print(a) # assignment
print(2 & 3, 2 | 3, ~2) # bitwise
print(1 in [1,2], 1 not in [1,2]) # membership

a = [1,2]
b = (1,2)
print(a is b, a is not b) # identity