# Write a Python program to get the difference between the two lists.

list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 4, 6, 7, 8]

diff_1_2 = list(set(list1)-set(list2))
diff_2_1 = list(set(list2)-set(list1))
total_diff = diff_1_2+diff_2_1
print((total_diff))