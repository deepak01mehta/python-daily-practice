#AGGREGATION 

class Customer:

    def __init__(self,name,gander,address):
        self.name = name
        self.gander = gander
        self.address = address


    def print_address(self):
        print(self.name,self.gander,self.address.city,self.address.pin,self.address.state)


class Address:

    def __init__(self,city,pin,state):

        self.city =city 
        self.pin = pin 
        self.state = state

add1 =Address("thane " "=",400601,",""maharashtra")

cust = Customer("deepak" ",","male" ",",add1)

cust.print_address()



    

#Inheritance
class User:

    def __init__(self):
        self.name ='deepak'


    def login(self):
        print('login')


class Student(User):

    # def __init__(self):
    #     self.rollno =100

    def enroll(self):
        print('enroll into the cousre')


u =User()
s = Student()

s.login() 
print(s.name)
s.enroll()


class phone:
    def __init__(self,price,brand,camera):
        print('inside phone construtor')
        self.__price =price
        self.brand = brand
        self.camera = camera
    def show(self):
        print(self.__price)



class Smartphone(phone):
    def check(self):
        print(self.__price)
        

             
    # def __init__(self, os,ram):
    #     self.os = os
    #     self.ram = ram
      

        print("inside smartphone constrctor")


s = Smartphone(200000,"redmi","64mp")
print(s.brand)
print(s.camera)
s.show()


#super keywords 


class phone:
    def __init__(self,price,brand,camera):
        print('inside phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    
# super() used to access the methods 
# and attributes of a parent class from a child class.

class smartphone(phone):
    def __init__(self, price, brand, camera,os,ram):
        print("inside smartphone constructor")
        super().__init__(price, brand, camera)

        self.os = os
        self.ram = ram
        print("inside smartphone constructor")

        

s = smartphone(20000, "apple","64mp",'ios',16)

print(s.os)
print(s.brand)

#abstract method

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass




      
        
        
        