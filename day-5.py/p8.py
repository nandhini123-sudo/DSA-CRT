#sum of square of all numbers
#printing square of all numbers
nums=input().split()
s=0
for i in nums:
   # print(int(i)*int(i))
    #s+=int(i)*int(i)
    x=(int(i)*int(i))
    s+=x
    print("square",x)
print("sum",s)