'''
#Basic Operators
a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%2)

#str
n1="Hello"
n2="World"
print(n1+n2)

#pydantic
print("1"*3)

#Comparison Operators
print(5==5)
print(5>=4)
print(5!=3)
print(5<=6)
print(5<5)
print(5>5)

#Logical Operators
print(not(5==5 and 6>5))
print(not(5==5 and 5>6))

#If else
a=5
b=5
if(a-b==0):
    print("The answer is 0")
else:
    print("The answer is not 0")

#Nested If
percentage=100
if percentage>=80 and percentage<=100:
    if percentage==90:
        print("You are Excellent")
    elif percentage==100:
        print("You are Brilliant:")
    print("A+")
elif percentage>=70 and percentage<80:
    print("B+")
else:
    print("C")

gender="M"
data = "Female" if gender=="F" else "Male"
print(data)
'''
'''
#Question1
account_balance = 500000
pin1=9999
daily_limit=20000
pin2=int(input("Enter your pin:"))

if pin1==pin2:
    print("Welcome")
    withdraw = int(input("How much do you want to withdraw?:"))
    if withdraw<=daily_limit:
        print("You have successfully withdrawn your money.")
    else:
        print("Daily Limit exceeded!. Can't Withdraw your money.\nTo withdraw more than 20000 you must have our membership")
else:
    print("Wrong Password")
'''

#Question2
Name=input("Enter your name:").upper()

if Name=="DIPESH":
    exp=2
    performance=90
    department="Technical Department"
    salary=20000
    if exp>=2:
        print(f"Name:Dipesh Tamang\nDepartment:{department}\t Salary:{salary}\tPerformance:{performance}")
        if performance>=70:
            if performance>=90 and performance<=100:
                bonus90=(25/100)*salary
                print(f"You'll get a bonus of 25% which is Rs.{bonus90}")
                print(f"{salary}+{bonus90}=Rs.{salary+bonus90}only.")
            elif performance>=80 and performance<90:
                bonus80=(12/100)*salary
                print(f"You'll get a bonus of 12% which is Rs.{bonus80}")
                print(f"{salary}+{bonus80}=Rs.{salary+bonus80}only.")
            else:
                bonus70=(5/100)*salary
                print(f"You'll get a bonus of 12% which is Rs.{bonus70}")
                print(f"{salary}+{bonus70}=Rs.{salary+bonus70}only.")          
        else:
            print("Not enough performance!")
    else:
        print("More than 2 years experience required.")

if Name=="LARRY":
    exp=5
    performance=80
    department="HR"
    salary=35000
    if exp>=2:
        print(f"Name:Larry\nDepartment:{department}\t Salary:{salary}\tPerformance:{performance}")
        if performance>=70:
            if performance>=90 and performance<=100:
                bonus90=(20/100)*salary
                print(f"You'll get a bonus of 25% which is Rs.{bonus90}")
                print(f"{salary}+{bonus90}=Rs.{salary+bonus90}only.")
            elif performance>=80 and performance<90:
                bonus80=(12/100)*salary
                print(f"You'll get a bonus of 12% which is Rs.{bonus80}")
                print(f"{salary}+{bonus80}=Rs.{salary+bonus80}only.")
            else:
                bonus70=(5/100)*salary
                print(f"You'll get a bonus of 12% which is Rs.{bonus70}")
                print(f"{salary}+{bonus70}=Rs.{salary+bonus70}only.")          
        else:
            print("Not enough performance!")
    else:
        print("More than 2 years experience required.")

if Name=="ABHISEK":
    exp=10
    performance=70
    department="CSR"
    salary=35000
    if exp>=2:
        print(f"Name:Abhisek\nDepartment:{department}\t Salary:{salary}\tPerformance:{performance}")
        if performance>=70:
            if performance>=90 and performance<=100:
                bonus90=(18/100)*salary
                print(f"You'll get a bonus of 25% which is Rs.{bonus90}")
                print(f"{salary}+{bonus90}=Rs.{salary+bonus90}only.")
            elif performance>=80 and performance<90:
                bonus80=(12/100)*salary
                print(f"You'll get a bonus of 12% which is Rs.{bonus80}")
                print(f"{salary}+{bonus80}=Rs.{salary+bonus80}only.")
            else:
                bonus70=(5/100)*salary
                print(f"You'll get a bonus of 12% which is Rs.{bonus70}")
                print(f"{salary}+{bonus70}=Rs.{salary+bonus70}only.")          
        else:
            print("Not enough performance!")
    else:
        print("More than 2 years experience required.")

else:
    print("No result found")


