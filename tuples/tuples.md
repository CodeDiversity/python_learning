## Tuples

Note: Tuples are immutable, meaning they can't be changed. 

alphabet = ('a','b','c','d')

Why use a tuple ? 

They are faster than lists, lighter in weight. Make code safer from bugs and problems showing up since it can't be changed. 

locations = {
    (35.6895, 39.6917) : "Tokyo Office"
}

they can be used as keys in dictionary. 

### Two built in methods 

Looping: Can use a for loop 

for name in names:
    print(name)

nothing is really different 

.count returns number of times a value appears in a tuple x.count('a')

.index returns the index at which a value is found in a tuple x.index('b') if it isn't find, it will return an error.

Can nest and also use slices in tuples. 

