## Dictionaries 

Key value pairs to describe the data and values to represent the data.

instructor = {
    "name": "Michael, 
    "owns_dog: true
    "age": 25
}

cat2 = dict{name="kitty", age=0.5}
or
cat = {"name":"blue", "age":0.5}

using dict you don't need the parenthesis around the key.

instructor["name"] would print "Michael" can access values like this.

Accessing Individual Values

## Iterating Over Dictionaries
instructor = {
        "name" : "michael", 
        "age" : 28, 
}

.values method on any sort of dictionary is one way of doing this.
.keys method would return all the keys in the dictionary.
.items() is the last one returns the keys and values, it justs takes in two values, first one is always key 2nd is value

for value in instructor.values()
    print value


for k, v in instructor.items():
    print(f"key is {k} and value is {v}")

No specific order is guaranteed on this list.

## In in dictionary 

"name" in instructor returns true but this is only looking at the keys, but if we need the values, need to use .values()

28 in instructor.values() would return true.

## Methods

clear will clear all the keys and value sin a dictionary 

d = dict(a=1)
d.clear() this would clear it out.
c = d.copy()

fromkeys 

{}.fromkeys("a", "b") returns {"a":"b"}

new_user = {}.fromkeys(['name', 'score', 'email', 'bio'], unknown)

get

d = dict(a=1, b=2, c=3)

d.get(a) = 1

Pop (will remove an item)

d.pop("a") will remove the key / value.

d.popitem() will remove something at random.

d.update() will take a dictionary and add it to another dictionary.