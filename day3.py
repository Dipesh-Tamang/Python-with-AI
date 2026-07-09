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

List:
name=['Dipesh', 'Denish', 'Jenish']
name.sort(reverse=True)
print(name)
"""
