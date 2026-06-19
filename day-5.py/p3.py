#sum of all numbers
nums=input()
s=1
for i in nums:
    if i.isdigit():
        s*=int(i)
print(s)
    
