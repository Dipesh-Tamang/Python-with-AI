'''
#tuple (immutable data types) (we cannot add data like in list)
a=(1,2,3,4,5)
print(type(a))
print(len(a))
print(a[0])

#typecasting
b=list(a)
b[0]=12
print(b)
a=tuple(b)
print(a)

#set (it doesnot follow an order) (it removes repeat)
a={'hello','Ram',12,True,'Dhangadi'}
print(type(a))
#to print set in order
for i in a:
    print(i,end=" ")

#Removing 1
a=[1,2,3,4,1,1,1,1,1,1]
b=set(a)
c=list(b)
c.remove(1)
print(c)
'''
#Function
#sir given question
def greet():
    a=2199
    b=a*a
    return 1,2
print(greet())

#self
def sqrt(a):
    return a**2

user=int(input("Enter a no."))
d=sqrt(user)
print(d)

#self
def add():
    data=[1,2,3,4,5,5,6]
    total=sum(data)
    return total
print(add())

#sir given question
def add_n():
    data=[1,2,3,4,5,5,6]
    total = 0
    for i in data:
        total +=i
    return total

print(add_n)