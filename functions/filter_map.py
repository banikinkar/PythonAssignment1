#The filter() function is a built-in Python tool used to extract items from an iterable (like a list or range) that meet a specific condition.
seq = [1,2,3,4,5,6]
odd = lambda x: x % 2 != 0
filter_output = filter(odd, seq)
print(filter_output)
print(list(filter_output))

# OR

seq = [1,2,3,4,5,6]
filter_output = list(filter((lambda x: x % 2 != 0),seq))

print(filter_output)


### map keeps all output for the entire seq
seq = [1,2,3,4,5,6]
map_output = list(map((lambda x: x % 2 != 0),seq))
map_squares = list(map((lambda x: x ** 2), seq))
print(map_output)
print(map_squares)
