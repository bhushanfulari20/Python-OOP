# Object Oriented Programming in Python
# By Bhushan Fulari

# 1. Programmer Class
class programmer:
    company = "Microsoft"
    
    def __init__(self, name, product):
        self.name = name
        self.product = product
    
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

Bhushan = programmer("Bhushan", "GitHub")
Tejas = programmer("Tejas", "Infotech")
Bhushan.getInfo()
Tejas.getInfo()

# 2. Calculator Class
print("\n")
z = int(input("Enter the num: "))

class calculator:
    def __init__(self, num):
        self.number = num
    
    def square(self):
        print(f"The value of {self.number} square is {self.number**2}")
    
    def squareRoot(self):
        print(f"The value of {self.number} square root is {self.number**0.5}")
    
    def cube(self):
        print(f"The value of {self.number} cube is {self.number**3}")

a = calculator(z)
a.square()
a.squareRoot()
a.cube()

# 3. Sample Class
print("\t")

class sample:
    a = "Bhushan"

obj = sample()
obj.a = "GitHub"
sample.a = "GitHub"
print(sample.a)
print(obj.a)

# 4. Employee Class
print("\t")

class employee:
    "Common base class for all employees"
    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.empCount += 1
    
    def displayCount(self):
        print("Total Employee %d" % employee.empCount)
    
    def displayEmployee(self):
        print("Name:", self.name, ", Salary:", self.salary)

# Creating employee objects
emp1 = employee("Bhushan", 200000)
emp2 = employee("Tejas", 150000)
emp3 = employee("Yash", 100000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print("Total Employee %d" % employee.empCount)