'''
Q10. Tuple Item Update
You have to modify a tuple item without converting it into a list. Provide an example of any case where this exactly can happen. 

'''
my_tuple = (1, 2, [3, 4, 5], 6)

print("Original tuple:", my_tuple)
my_tuple[2][1] = 40

print("Modified tuple:", my_tuple)