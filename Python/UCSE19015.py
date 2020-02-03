# Creating a list of numbers from 1-20 that is either divisible by 2 or 4 using filter.

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


solution = filter(lambda x: x % 2 == 0, list1)
solution = filter(lambda x: x % 4 == 0, list1)
print(list(solution))

