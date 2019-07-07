# Nested Lists

Lists can contain any kind of element, including other lists.

Complex data structutres, game boards, rows and columns.

nested_list = [[1,2,3], [4,5,6], [7,8,9]]
nested_list[-1][0] would return 7

For printing values in nested lists.

for l in nested_list:
    for val in l:
    print(val)

Would print out all the values.

List Comprehension.
[[print(val) for val in l for l in nested_list]]

