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