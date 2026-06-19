class Dog:
    def __init__(self,name,color,age):
        self.name=name
        self.color=color
        self.age=age
    def display(self,name,color,age):
        print("name:",self.name)
        print("color:",self.color)
        print("age:",self.age)
    def shout(self):
        print(f"{self.name}  bit him. 😄")
d1=Dog("leo","brown and black",1)
d1.display("name","color","age")
d1.shout()
        