#def hello():
    #for i in range(5):
    #    print(i)
   #     if i==2:
  #          return
 #   print('hello')
#hello()


def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(5)