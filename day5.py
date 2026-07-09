#learning Pull request
user=[]
for i in range(1,5):
    name=input(f"{i}.Enter your name:")
    user.append(name)
user.sort()
count=0
for i in user:
    if i.startswith("a") or i.startswith("A"):
        count+=1
        print(i)
if count==0:
    print("Noone of the user names starts with A") 
print(f"There are {count} users whose name starts with a.")        