# default args

def area_of_circle(r,pie=3.14):
    return pie*r**2

print(area_of_circle(7))
print(area_of_circle(10,2))
print(area_of_circle(1))




def sum_of_number(a,b,*data):
    print(data)
    print(a,b)


sum_of_number("this is a",2,3,12,1,13,1,31,13,13,31,31,3,1)
sum_of_number("this is a",2)
sum_of_number("sudan",1)




def user_info(**kwargs):
    # print(kwargs['fname'])
    print(kwargs.get('fname'))




user_info(fname="sudan",lname="Bhandari",age=28)
user_info(lname="Bhandari", role="developer")



def find_largest(*args):
    if len(args)==0:
        return "please provide any number"
    largest = args[0]
    # largest= 0
    for i in args:
        if i>largest:
            largest = i
    return largest

print(find_largest(90,111,134,121,12,1,0,1))
print(find_largest(111,134,121,12,1,0,1))

print(find_largest())