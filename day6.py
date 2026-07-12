# dictionary
Student = {
    "Name": "Dipesh",
    "Address": "Balaju",
    "Roll_no": 1,
    "Studying": "BBS",
    "Name": "Tshering",
}
print(Student)

print("__________" * 10)
print("Len of Student")
print(len(Student))

print("__________" * 10)
print("Name Only:")
print(Student["Name"])

print("__________" * 10)
print("Get names")
print(Student.get("names"))
print(Student.get("Name"))
print(Student.get("names", "Dipesh Tamang"))

print("__________" * 10)
print("Updating Address")
Student["Address"] = "Dhalko"
print(Student)


print("__________" * 10)
print("Updating using update")
# Update
Student.update({"age": 10, "Studying": "BIT"})
print(Student)

# Removing items
# Delete
print("__________" * 10)
print("Delete")
del Student["Roll_no"]
print(Student)

# Pop
print("__________" * 10)
print("Pop")
data = Student.pop("Address")
print(data)

# Pop Item
print("__________" * 10)
print("Pop item")
data2 = Student.popitem()
print(data2)
print(Student)

# Clear
# print("__________" * 10)
# Student.clear()
# print(Student)

#Printing Keys,values and items
print("__________" * 10)
print("Printing Keys Values and Items")
print(Student.keys())
print(Student.values())
print(Student.items())

print("__________"*10)
Student2 = {
    "Students": ["Aayush", "Aashisma", "Aakash"],
    "Address": {
        "0":"Balaju",
        "1":"Dhalko",
        "2":"Chunikhel"},
    "Roll_no": [1, 2, 3],
    "Studying": "BBS",
    "Name": "Tshering",
}
print("__________" * 10)
print("Student2 Records")
print(Student2)

print("__________" * 10)
print("Address finding from dictionary using array")
print(Student2["Address"]["0"])

print("__________" * 10)
print("Finding Names from List using array")
print(Student2['Students'][0])