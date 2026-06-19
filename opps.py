class student:
    def __init__(self,name,branch):
        self._name=name
        self._branch=branch

    def eating(self):
        print("eating")
    def playing(self):
        print(f'{self.name} is playing')
student1=student("nandhu","ece")
print(student1.name)

student1.playing()
