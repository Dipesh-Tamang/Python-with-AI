'''
#Positional Argument
def num(*data):
    print(data)
num(1,2,3,4,5)

#Keywords arguments
def student(**kwargs):
    print(kwargs)
    print(kwargs.get('Name'))

student(Name='Dipesh',Age=20,Gpa=3.23,Roll_no=2)
student(Age=21,Gpa=3.9,Roll_no=1)

#Find largest number using positional argument
def student(*arg):
    if len(arg)==0:
        return'Please provide number'
    else:
        largest=arg[0]
        for i in arg:
            if i>largest:
                largest=i
        return largest
print(student(90,10,100,50,60,200))
print(student())
'''
#Adding from positional argument
def add(*data):
    total=0
    for i in data:
        total+=i
    return total

print(add(1,2,3))
