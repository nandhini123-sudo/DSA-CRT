#count of target among all numbers
nums=input()
t=int(input())
c=0
for i in nums:
    if i.isdigit() and int(i)==t:
        c+=1
print(c)