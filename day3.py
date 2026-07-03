"""
#list
a=[1,2,3,4]
print(type(a))

#Order type
b=[2,"Dipesh",3.0,True,False,77] #range -3 to 2
print(b)

#index
print(b[1])
#to print from last
print(b[-1])
#TO KNOW THE LENGTH it will start from 1
print(len(b))
#Slicing
print(b[1:4])
print(b[:4])
print(b[:5])
print(b[:])

#append
a=[1,2,3,4]
a.append(6)
print(a)

data=[]
data.append(100)
print(data)

#insert
print("insert")
a=[1,2,4,5]
a.insert(1000,88)
a.insert(2,3)
print(a)

#extends
print("extends")
a=[1,2,3]
b=[4,5,6]
a.extend(b)
b.extend(a)
print(a)
print(b)


#concat
print("concat")
a=[1,2]
b=[4,5,6]
c=a+b+a+a
print(c)
print(a)
print(b)

# rEMOVE METHODS
print("_____List_____")
mixed = [1, 2, True, False, "Dipesh", 2.0, None]
print(mixed)

# delete
print("____Delete____")
del mixed[1]
print(mixed)

# remove
print("______remove_______")
mixed.remove(2.0)
print(mixed)

# pop
print("_____pop_____")
data_pooped2 = mixed.pop()
data_pooped1 = mixed.pop(1)
print(mixed)
print("popped data are:", data_pooped1, data_pooped2)

# clear
print("______clear_____")
data=mixed.clear()
print(mixed)

# reverse
print("_____Reverse_____")
names = ["Dipesh", "Hari", "Geeta", "Dipesh"]
names.reverse()
print(names)

#count
print("____count_____")
count_std= names.count("Dipesh")
print(count_std)

#index
print("_____index______")
data=names.index("Geeta")
print(data)

#ascending order
print("____Students___")
students = ["Pranav", "Ram", "Seeta", "Dipesh"]
print(students)

print("____ascending order___")
students.sort()
print(students)

#decending order
print("____decending order___")
students.sort(reverse=True)
print(students)
"""
"""
#Question Solving
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
"""
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
   