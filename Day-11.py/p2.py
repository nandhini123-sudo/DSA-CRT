class student:
    def __init__(self,name, rollno, branch):
        self.name=name
        self.rollno=rollno
        self.branch=branch
    def display(self,name,rollno,branch):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("branch:",self.branch)
s1=student("nandhu",411,"ECE")
s1.display("sai",421,"ECE")
        