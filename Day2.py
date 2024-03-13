#multiple assignents
name, age, attractive = "Samuel", 20, True
print(name)
print(age)
print(attractive)

sam = Luke = John = 30
print(sam)
print(Luke)
print(John)

#string methods
name = "Samuel"

print(len(name))
print(name.find("e"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("e","i"))
print(name*3)

#type casting
x = 3
y = 24.5
z = "Pizza"
y = int(y)
print(y)
#the above is one way of doing it
print(int(y))

#accepting user inputs
name = input("Enter your name: ")
age = input("Enter your age: ")
height = float(input("Enter your height: "))

height+=1

print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+" cm tall")

#math functions
import math
pi = 3.14
x = 3
y = 4
z = 6

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(pi))
print(max(x, y, z))
print(min(x, y, z))
