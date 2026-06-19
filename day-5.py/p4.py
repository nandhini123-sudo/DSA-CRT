#sum of all numbers
nums=input()
s=0
for i in nums:
    if i.isdigit():
        s+=int(i)
print(s)
    
