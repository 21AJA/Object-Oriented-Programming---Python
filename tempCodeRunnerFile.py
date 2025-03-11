# Python Class and object with Constructor

# class student: #Class
#     def __init__(self,name, branch):#Constructor
#         self.name = name
#         self.branch = branch 
    
# stu1=student("Akshay","IT") #Object
# print(stu1.name)
# print(stu1.branch)

# # #python class and object without showing constructor

# class cricketer:
#     openor = "shikhar dhawan"
#     bowller = "Jaspreet bumrah"
# name = cricketer()
# print(name.openor)
# print(name.bowller)

# # Class & Object with methods
# class student:
#     def __init__(self,name,branch):
#         self.name=name
#         self.branch=branch
#     def hello(self):
#         print("this is method in python")
# stu1 = student("karan","IT")
# stu1.hello()
# print(stu1.name)
# print(stu1.branch)

# #Cretae student class that takes name and marks of 3 subjects as argumentsin constructor. then createa method to print the average

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
  
#     def average(self):
#         avg = sum(self.marks) / len(self.marks)
#         print(f"Average marks of {self.name}: {avg:.2f}")

# stu1 = Student("Karan", [90, 88, 46])
# print(stu1.name)
# stu1.average()