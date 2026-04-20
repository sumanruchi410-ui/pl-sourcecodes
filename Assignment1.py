My_list = [1, 3, 5, 2, 4]
print("Original List :", My_list)

print("First Element :", My_list[0])
print("Last Element :", My_list[-1])

My_list.append(60)
print("After adding 60 :", My_list)

My_list.insert(2, 25)
print("After inserting 25 at index 2 :", My_list)

My_list.remove(3)
print("After removing 3 :", My_list)

My_list.pop()
print("After popping last element :", My_list)

My_list.sort()
print("Sorted List :", My_list)

My_list.reverse()
print("Reversed List :", My_list)