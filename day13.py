"""
def student_info(*args,**kwargs):
    total = sum(args)
    percentage = total/len(args)
    return f"{kwargs['name']} total marks is {total} and percentage is {percentage}%"


print(student_info(70,90,56,77,100,name="Harilal"))
# harilal total marks is 345 and percentage is 78%

print(student_info(70,56,100,name="Suman"))
# Suman total marks is 213 and percentage is 78%
print(student_info(70,name="Sumanlal"))
# sumanlal total marks is 70 and percentage is 70%



"""

#

"""
print("----------->")
def library_management(*args, **kwargs):
    print(kwargs['name'], kwargs['member_id'])
    print(kwargs['max_books'])
    print(len(args))
    for i in args:
        print(i)



library_management(
    "Python Crash Course",
    "Clean Code",
    "The Pragmatic Programmer",
    name="Sudan",
    member_id="M102",
    membership_type="Premium",
    max_books=5
)


# lambda func
x = lambda a,b : a+b
print(x(1,2))



def add(a,b):
    return a+b


detail = lambda *args, **kwargs :  f"{kwargs['name']} total marks is {sum(args)} and percentage is {sum(args)/len(args)}%"


print(detail(70,90,56,77,100,name="Harilal"))
# harilal total marks is 345 and percentage is 78%

print(detail(70,56,100,name="Suman"))
# Suman total marks is 213 and percentage is 78%
print(detail(70,name="Sumanlal"))
"""

"""
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

print(student_info(1,2,3,4,5,6,67,8,'test','hero',Name="Dipesh",Country="Nepal"))


def student(*arg,**kwargs):
    total=0
    x=len(arg)
    for i in arg:
        total+=i
    percentage=total//x
    return f'{kwargs.get('name')},total marks is {total} and percentage is {percentage}%'

print(student(70,90,56,77,100,name='Harilal'))
print(student(70,56,100,name='Sudan'))
print(student(70,name='Sumanlal'))
"""
# 6. Library Management

# Create a function that accepts:

# Multiple book titles using *args
# Member information using **kwargs
# Requirements
# Display the member's name and membership ID.
# Print the list of borrowed books.
# If max_books is provided, check whether the borrowing limit has been exceeded.

'''
def library_management(*args, **kwargs):
    count = 0
    limit=5
    if len(args) == 0:
        print(f"Name:{kwargs.get('name')}, MembersId:{kwargs['members_id']}")
        print(f"You havent burrowed any books. You can burrow {limit} books.")
    else:
        print(f"Name:{kwargs['name']}, MembersId:{kwargs['members_id']}")
        a = 1
        limit-=len(args)
        if limit>=1 and limit<=4:
            print(f'You can still get {limit} more book.')
        else:
            print("You've reached your limit")
        print(f"Burrowed books:{len(args)}")
        for i in args:
            print(f"{a}.{i}")
            a += 1
            count += 1


library_management(
    "Atomic Habits",
    "Python Basic",
    "Django",
    "Rich dad",
    name="Dipesh",
    members_id="M102",
    members_type="Premium",
    max_book=5,
)

library_management(name='Hari', members_id='MG09')

library_management(
    "QBASIC",
    "C",
    "Comics",
    "Game of thrones",
    "Hero",
    name="Dipesh",
    members_id="M102",
    members_type="Premium",
    max_book=5,
)
'''

#Lambda Function
detail=lambda *args,**kwargs:f'{kwargs.get('name')},Your total marks is:{sum(args)} and percentage is:{sum(args)//len(args)}%'
print(detail(20,30,40,20,name="Dipesh"))
print(detail(10,70,60,30,name="Aashray"))
