list1=[]

for i in range(0,1000):
    list1.append(i)
target=999
seen=False
list2=list(range(0,1000))
for i in list2:
    if i==target:
        seen=True
        break
      