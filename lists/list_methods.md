## List Methods

### Append: Add item to end of list

first_list =  [1,2,3,4]
first_list.append(5)

Cannot Comma Separate Values.
prints [1,2,3,4,5]

### Extend: Add to the end of a list all values

first_list.extend([5,6,7,8])

would add the each individually.

### Insert
first_list.insert(index, item_to_add)

>>> data = [1,2,3,4]
>>> data.insert (0,2)
>>> data
[2, 1, 2, 3, 4]
>>> 

### Clear 

first_list[1,2,3,4]
first_list.clear()
first_list = []

### Pop 
list.(index or last if no index given)
Remove item at index and return it if no index removes and returns last item in list

>>> new_list = [1,2,3,4]
>>> new_list.pop()
4
>>> new_list
[1, 2, 3]
>>> 

could make a variable such as last_number = numbers.pop()

and last_number would now be 3.

### Remove

Provide a value not an index 
Removes first item whose value is x 
If none found throws error

list = [1,2,3,4,5,5]
list.remove(5)

Will only take out the first 5.

Does not return item that is removed since we already know what we are removing.

### index

numbers = [1,2,3,4]
numbers.index(9)

or 

numbers.index(item, starting_index)
numbers.index(item, starting_index, ending_index)

### count
list.count(item) and returns how many time it appears
numbers = [1,2,3,4]

numbers.count(2) === 1 since it only appears once


### reverse 

numbers = [1,2,3,4]

numbers.reverse()

changes the actual list.

>>> numbers = [1,2,3,4]
>>> 
>>> numbers.reverse()
>>> numbers
[4, 3, 2, 1]
>>> 

### sort 

sort items (in place)

another_List = [6,4,1,2,5]

another_list = [1,2,4,5,6]

### Join 

words = ["coding", "is", "fun"]

list = "I am friends with".join(words)

takes a list and turns it into a string.