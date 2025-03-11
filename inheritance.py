#Single inheritance
class student:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    @staticmethod
    def hello():
        print("hello world")
    @staticmethod
    def welcome():
        print("welcome to the class...")
class IT(student):
    subject = "DSA"
    labsubject="PPS"
stu1=student("akshay","IT")
print(stu1.hello())
print(stu1.welcome())
print(stu1.name)
print(stu1.branch)

#multi level inheritance
class Car:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    @staticmethod
    def start():
        print("Car is started")
    @staticmethod
    def stop():
        print("Car is stop") 
class Bike:
    def __init__(self,brand1,company):
        self.brand1=brand1
        self.company=company 
    @staticmethod
    def race():
        print("bike is in a race")
    @staticmethod
    def parking():
        print("bike is in a parking") 
class Van(Car,Bike):
    color="blue"
    collection="old"
    
obj1 = Van(Car,Bike)
print(obj1.race())
print(obj1.start())
   
    
    

    