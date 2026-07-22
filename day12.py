#oop
#This is a class
class Test():
    a = 10#attributes
    b = 12

#This is a object
#It changes the value only here
c1=Test() #c1 is a object
c1.a=90 #chaning value
c1.c=100
print(c1.a)
print(c1.c)

#This is a object
c2=Test()
print(c2.a)

class Test1():
    a=10
    b=5
    #This is a method
    def add(plus):
        return plus.a+plus.b
    def sub(minus):
        return minus.a-minus.b
    def result(self):
        add=self.add()
        sub=self.sub()
        return add,sub

obj=Test1()
print(obj.result())


