'''
#Question 1 Solving
List=["Banana","Apple","Cereals","Coffee","Milk","Tomato","Potato"]
List.append("Ps5")
List.append("Milk")
List.append("Glue")
List.insert(2,"Bag")
List.remove("Coffee")
print(List)
del List[9]
print(List)
List.reverse()
print(List)
if "Milk" in List:
    if List.index("Milk")<3:
        print("Easy to find")
    else:
        print("Far in the list")
else:
    print("Milk not available")

#Question Solving 2
players = input("Enter player names (comma-separated): ").split(",")
players.append("Dipesh")
substitute=["Bijay", "Jenish"]
players.extend(substitute)
players.insert(100,"Captain")
players.remove("Bijay")
players.reverse()
if players[0]=="Captain":
    print("captain is leading")
else:
    print("Captains position changed")
print(players)

#Question 3 solving
n=int(input("How many records do you want to keep?"))
salary=[]
for i in range(n):
    salary_asked=int(input("Enter the salary:"))
    salary.append(salary_asked)
salary_2=int(input("Enter the salary to add in index 2:"))
salary.insert(2,salary_2)
salary_3=int(input("Enter another salary to append:"))
salary.append(salary_3)
del salary[1]
salary.sort()
salary.sort(reverse=True) #descending 
maximum=max(salary)
minimum=min(salary)
if maximum>=100000:
    if minimum<=30000:
        print("Huge Salary Difference!")
else:
    print("Balanced Series")

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
#Question 4
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


#Question 5
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

#Question 6 Solving 
Student = {}
n = int(input("How many student records do you want to enter? "))
for i in range(1, n + 1):
    Student[f"Student{i}"] = {
        "Name": input(f"Enter Student {i} Name: "),
        "Age": input(f"Enter Student {i} Age: "),
        "Faculty": input(f"Enter Student {i} Faculty: "),
        "Subjects": [],
        "Address": {
            "City": input(f"Enter Student {i} City: "),
            "Ward_no": input(f"Enter Student {i} Ward no: "),
            "Street": input(f"Enter Student {i} Street: ")
        }
    }
    subject_count = int(input(f"How many subjects for Student {i}? "))
    for j in range(1, subject_count + 1):
        subject = input(f"Enter Subject {j}: ")
        Student[f"Student{i}"]["Subjects"].append(subject)

print("\nStudent Records:")
print("\n========== Student Records ==========\n")

for i in range(1, n + 1):
    print(f"Student {i}")
    print("Name     :", Student[f"Student{i}"]["Name"])
    print("Age      :", Student[f"Student{i}"]["Age"])
    print("Faculty  :", Student[f"Student{i}"]["Faculty"])
    print("Subjects :", Student[f"Student{i}"]["Subjects"])
    print("City     :", Student[f"Student{i}"]["Address"]["City"])
    print("Ward No  :", Student[f"Student{i}"]["Address"]["Ward_no"])
    print("Street   :", Student[f"Student{i}"]["Address"]["Street"])
    print("-" * 40)

print("\n========== Dictionary Information ==========\n")

print("Keys:")
print(Student.keys())

print("\nValues:")
print(Student.values())

print("\nItems:")
print(Student.items())

print("\nTotal Student Records:", len(Student))

print("\n========== Update Faculty ==========\n")

faculty_no = int(input("Enter the student number to update: "))
new_faculty = input("Enter new faculty: ")

Student[f"Student{faculty_no}"].update({"Faculty": new_faculty})

print("\nFaculty Updated Successfully!")
print("New Faculty:", Student[f"Student{faculty_no}"]["Faculty"])

print("\n========== Remove Age ==========\n")

age_pop = Student["Student1"].pop("Age")
print("Removed Age of Student1:", age_pop)

print("\n========== Student Status ==========\n")

if len(Student["Student1"]["Subjects"]) == 5:
    city = Student["Student1"]["Address"]["City"].upper()

    if city == "KATHMANDU":
        print("Student1 Status : Local Student")
    else:
        print("Student1 Status : Outside Valley")
else:

#Question 7 solving
data=[100,'Ram', 55.5, True, 'Python', 200, False, 'Kathmandu']
print("-------Strings only---------")
for i in data:
    if isinstance(i,str):
        print(i,end=",")
print("\n-------Integers only---------")
for i in data:
    if isinstance(i,int):
        if type(i)==int:
            print(i,end=",")

print("\n-------Boolean values only---------")
for i in data:
    if isinstance(i,bool):
        print(i,end=",")

print("\n-------How many strings are present---------")
count=0
for i in data:
    if isinstance(i,str):
        count+=1
print(count)

temp=[]
for i in data:
    if type(i)==str:
        null=i
        temp.append(null)
print(len(temp))
    print("Student1 Status : Incomplete Subject List")

#Question 8 solving
num=[]
for i in range(1,11):
    n=int(input("Enter the number:"))
    if n==0:
        break
    num.append(n)
print(f"The numbers before you entered 0:{num}")


#Question 9 solving 
students=[]
for i in range(1,6):
    name=input(f"Enter name {i}:")
    students.append(name)

for i in students:
    print(i)

count=0
for i in students:
    if i.startswith("a") or i.startswith("A"):
        count+=1
print(f"There are {count} students whose name starts with A.")

lng_name=[]
shrt_nam=[]
for i in students:
    if len(i)>6:
        lng=i
        lng_name.append(lng)
    else:
        shrt=i
        shrt_nam.append(shrt)
print(f'These students have :{lng_name} long name')
print(f'These students have :{shrt_nam} short name')
'''