import re
string = "She sells sea shells on the sea shore"
patter1 = "sells"

if re.match(patter1,string):
    print("Match found")
else:
    print(patter1, "is not present")

if re.search(patter1, string):
    print("Match found")
else:
    print(patter1, "is not present")

if re.findall(patter1, string):
    print("Match found")
else:
    print(patter1, "is not present")


