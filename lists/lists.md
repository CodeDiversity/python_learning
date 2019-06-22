## What are lists 
- Way of combining data into one structure.
- Very similar to arrays in other languages.

item1 = 'bananas'
item2 = 'lego set'

Items are not associated, not a good solution since they are not connected in any way.

tasks = ["Install Python", "Learn Python", "Take a Break"]

This is an example of a lists, can be any types of data, does not have to be only strings.

## Length Function

len(listItem) will return the number of items in the list.

tasks = list(range(1,4))
will return [1,2,3]

You can convert the range to a list item.

## Accessing Lists

freinds = ["Ashley", "Matt", "Michael"]

Zero based indexes in Python.

print(friends[0]) would print Ashley

- Accessing items from the end:
friends[-1] would print "Michael"

- To find if someone is in a list

"Ashley" in friends # True
"Michael" in friends # False