## List Comprehensions

[ ___ for ___ in ___]

nums = [1,2,3]

[x*10 for x in nums]
[10,20,30]

doubled_nums = [num * 2 for num in numbers]

is easier than looping, it's more concise than for loops.

Name = "Michael"

[char.upper() for char in name]

[num*10 for num (1,6)]
Can also do this with ranges.

[bool(val) for val in [0,[], ""]] False, false, false

[str(num) for num in numbers] - convert to strings


## Conditional Logic

numbers = [1,2,3,4,5]

evens = [num for num in numbers if num % 2 == 0]

if keyword comes at the end.

[num * 2 if num %2 == 0 else num /2 for num in numbers]

can also use the else statements too.

