# empty tuple
# Output: ()
my_tuple = ()
print(id(my_tuple))

# tuple having integers
# Output: (1, 2, 3)
my_tuple = (1, 2, 3)
print(id(my_tuple))
print(id(1))
print(id(2))
print(id(3))


# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(id(my_tuple))
print(id(1))
print(id("Hello"))
print(id(3.4))


# nested tuple
# Output: ("mouse", [8, 4, 6], (1, 2, 3))
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(id(my_tuple))

# tuple can be created without parentheses
# also called tuple packing
# Output: 3, 4.6, "dog"

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
# Output:
# 3
# 4.6
# dog
a, b, c = my_tuple
print(a)
print(b)
print(c)
