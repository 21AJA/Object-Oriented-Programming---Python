# Python Class and object with Constructor

class student: #Class
    def __init__(self,name, branch):#Constructor
        self.name = name
        self.branch = branch 
    
stu1=student("Akshay","IT") #Object
print(stu1.name)
print(stu1.branch)

# #python class and object without showing constructor

class cricketer:
    openor = "shikhar dhawan"
    bowller = "Jaspreet bumrah"
name = cricketer()
print(name.openor)
print(name.bowller)

#Class & Object with methods
class student:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def hello(self):
        print("this is method in python")
stu1 = student("karan","IT")
stu1.hello()
print(stu1.name)
print(stu1.branch)
