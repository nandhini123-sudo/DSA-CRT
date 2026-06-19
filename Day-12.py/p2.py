#simple queue
Front=0
rear=-1
queue=[None]*5
size=0
def Enqueue(value):
    if size==len(queue): return False
    rear+=1
    size+=1
    queue[rear]=value
def Dequeue():
    if size==0:return False
    front+=1
    return True
def peek():
    return queue[front]
def isFull():
    return size==len(queue)
def isEmpty():
    return size==0