Student = {
    "Name": "Ruchi",
    "Roll_no": 09,
    "Branch": "CSE",
    "Marks": 90
}

print("Dictionary Elements :", Student)

print("Accessing Elements:")
print("Name:", Student["Name"])
print("Marks:", Student["Marks"])

Student["Marks"] = 90
Student["Year"] = "Second"

print("After Updating Dictionary :", Student)

Student.pop("Roll_no")
del Student["Branch"]

print("After Removing Elements :", Student)

Extra_info = {
    "College": "MIT ADT",
    "City": "Pune"
}

Merged_dict = Student | Extra_info

print("After Merging Dictionaries :", Merged_dict)