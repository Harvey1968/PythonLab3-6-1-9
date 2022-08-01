# 3.6.1.9 LAB: Operating with lists - basics

my_list = [1, 2, 4, 4, 9, 1, 4, 2, 6, 2, 9]	# I have added an extra '9' at position 4 [0,1,2,etc..] to prove 'sort()'.
my_list.sort()	# Sorts list for readability only ;; this can be done at the beginning or end.
new_list = []	# 'new_list' created as a temporary work area, so that I don't need to update the list in situ.
for number in my_list:  # Checks all numbers in the original list.
	if number not in new_list:  # If the number isn't in the new list then
		new_list.append(number)  # it will append (add/copy) it here.
my_list = new_list[:]  # Copies 'new_list' to the oridginal 'my_list'.
print("The list with unique elements only:\n", my_list, "\n")
