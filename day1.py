'''
#Checking 
b = 111
a = "dipesh"
print(a)
print(a, 1, 2, 3, 4, 5)
print(type(a))
print(type(b))

#Type Casting
data = input("enter the value")
c=int(data)
print(type(c))

#Isinstance
a = "45"
print(isinstance(a, str))

#String formatting
Name = "Dipesh"
Address = "Dhalko"
a = f"My name is {Name} and I live in {Address} {1+1}"
print(a)

#Installing the library 
import pyjokes
# Fetch a random programmer joke
joke = pyjokes.get_joke()
print(joke)
'''