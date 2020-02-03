s = {1, 2.0, "abc"}

print(s)

print(type(s))

s = set([1, 2, 'a', 'b', "yes", 4.67])

print(s)

list1 = [1, 2, 3, 4, 5]
s = set(list1)
print(s)

Tup1 = ('a', 'b', 'c', 'd')
print(set(Tup1))

str = "Helloworld"
print(set(str))

print(set("A quick brown fox jumps over the dog".split()))

Coders = set(["Arnab", "Pratik"])
print(Coders)

Analysts = set(["Krishna", "Pratik", "Arnab"])
print(Analysts)

print("Intersection:", Coders.intersection(Analysts))
print("Union:", Coders.union(Analysts))
print("(Coders-Analysts:", Coders.difference(Analysts))
print("(Analysts-Coders):",Analysts.difference(Coders))
print(Coders.intersection(Coders))
print(Coders.union(Coders))
print(Coders.difference(Coders))
print(Coders.symmetric_difference(Analysts))

print(Coders.intersection_update(Analysts))
print(Coders.difference_update(Analysts))
