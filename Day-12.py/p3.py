# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# Node1=Node(10)
# Node2=Node(20)
# Node1.data=30
# Node1.next=Node2
# Node1.data=None
# print(Node1.data)
# print(Node1.next.data)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
Node1=Node(10)
Node2=Node(20)
Node3=Node(40)
Node1.data=50
Node2.data=90
Node3.data=69
Node1.next=Node2
Node2.next=Node3
print(Node1.data)
print(Node2.data)
print(Node3.data)
print(Node1.next.data)
print(Node2.next.data)
