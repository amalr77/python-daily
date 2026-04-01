names=[]

count=5
for _ in range(count):
    name=input("Enter the names : ")
    names.append(name)

names.sort()
print(names)

names.sort(reverse=True)
print(names)