set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Accessing Set 1 elements :")
for element in set1:
    print(element)

print("Accessing Set 2 elements :")
for element in set2:
    print(element)

union_set = set1.union(set2)
print("Union of Set1 and Set2 :", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2 :", intersection_set)

difference_set = set1.difference(set2)
print("Difference of Set1 and Set2 :", difference_set)