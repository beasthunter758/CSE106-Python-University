list_A = [1,2,3,4,5]

print(list_A)

list_B = ["Pratik", "Sinha"]

print(list_B)

list_C= [1,'a',"bcd"]

print(list_C)

#Access values in lists

num_list = [1,2,3,4,5,6,7,8,9,10]
print("num_list is :", num_list)

print("The first element is :", num_list[0])

#list(Start:Stop:Step)

print("num_list:", num_list[3:5])
print("num_list[::5]", num_list[::5])
print("num_list[-3]", num_list[-3])

#updating values in lists

num_list[5]=100
print(num_list)
del num_list[3]
print(num_list)
del num_list[:]
print(num_list)

num_list = [1,9,12,65,45]
print(num_list)
num_list[2] = [3,5,6]
print(num_list)
#Basic list operation

print(len(num_list))
print(list_A+list_B)

print(5 in num_list)
print(5 not in num_list)

print(max(list_A))
print(min(list_A))
print((sum(list_A)))

#count index insert

list_A.insert(3,100)
print(list_A)

#pop remove reverse extend sort

print(list_A.pop())
list_A.remove(4)
print(list_A)
list_A.reverse()
print(list_A)
list_A.sort()
print(list_A)
