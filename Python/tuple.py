# 1. Mutable
# 2. Syntax
# 3. No of functions
# 4. Faster
# 5. Key/value pair used as a dictionary

Tup1 = ()

print(Tup1)

Tup1 = (5)
print(Tup1)

Tup1 = (1,2,3,4,5)
print(Tup1)

Tup2 = ('a','b','c')
print(Tup2)

a,b = 10,20
print(a,b)

c = (10)
print(type(c))

c = (10,)
print(type(c))

quo,rem = divmod(100,3)
print(quo,rem)

Tup1 = (1,2,3,4,5,6,7,8,9,10)
print("Tup[3:6]=",Tup1[3:6])

Tup1 = (1,2,3,4,5)
Tup2 = (6,7,8,9,10)
Tup3 = Tup1+Tup2
print(Tup3)
del Tup1[30]
print(Tup1)

