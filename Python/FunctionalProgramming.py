def add(x,y):
    return x+y;


list1 =[1,2,3,4,5,6,7]
list2 =[8,9,10]
list3 =list(map(add,list1,list2))

print(list3)

# Getting the even numbers using filter

def check(x):
    if (x%2 ==0 or x%4 ==0):
        return 1

list_1 = [1,2,3,4,5,6,7,8]
evens=list(filter(check,list_1))
print(evens)

#Reduce function(Imp for mid sems and end sems)

import functools

def add(x,y):
    return x+y

numlist = [1,2,3,4,5]
print(functools.reduce(add,numlist))
