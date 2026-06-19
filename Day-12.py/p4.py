l1=[4,5,3,7,6]
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def createList(l1):
    head=None
    temp=head
    for i in l1:
        newNode=None(i)
        if head is None:
            head=newNode
            temp=head
            
        else:
            temp=temp.next
            temp.next=newNode
            return head
createList(l1)
