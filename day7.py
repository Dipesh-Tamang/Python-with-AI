# loop in list
'''
for i in [1,2,3,4,5]:
    print(i)

for i in [1,2,3,4,5,6]:
    print(i)

print("------loop in list---------")
a = [1,2,3,4,5]
for i in a:
    print(i*i)
    print("this is test",i)
    if i == 3:
        print("i is 3")

#Loop in string
print("--------Loop in string----------")
for i in "broadway":
    print(i)

#Loop in dictionary
print("--------Loop in dictionary----------")

fifa_world_cup = {
    "tournament": "FIFA World Cup",
    "year": 2026,
    "host": ["Us","Canada","Mexico"],
    "champion": "Argentina",
    "runner_up": "France",
}
fifa_world_cup['year']

for i in fifa_world_cup.values():
    print(i)

for i in fifa_world_cup:
    print(i,fifa_world_cup[i])

print("------------------")

for i,j in fifa_world_cup.items():
    print(i, j)
    
#even or odd
print("-------Even or odd-----------")
for i in range (10,21,1):
    if i%2==0:
        print(i)
    elif i%2!=0:
        print(i)

#Filtering data
print("---------Filtering data---------")
data=[1,'jhon',25,'developer',100,'Python']
for i in data:  
    if isinstance(i,str):
        print(i)    
        
#Break and continue statement
print("---------Break statement---------")
for i in range(10,20,1):
    if i==15:
        break
    print(i)

print("---------Continue statement---------")
for i in range(10,20,1):
    if i==10 or i==15:
        continue
    print(i)

print("---------Nested loop---------")
#Nested Loop
for i in [1,2,3]:
    for j in [4,5,6]:
        print(i,j)
    print(" _______")
'''