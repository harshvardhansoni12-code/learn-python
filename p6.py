# list
# collection of items that are ordered and changeable.
# Lists are written with square brackets.
# list can contain different data types
# one can change lists size and content
my_list = [1, 2, 3, 4, 5]
print(my_list)
print()
L = [40 , 'hello' , 3.14 , [12,23,34]]
print(L[3])
print(L[2])

# print(id(L[0]))
# speed of execution is less than array

# id shows memory location the element is stored in
x = 1
# print(id(1))
print()
k = [1,2,'a']
# list in memory
# list store memory locations of elements in the list
print(id(k[0]))
print(id(1))
print(id(k[1]))
print(id('a'))
print(id(k[2]))

# python strings are immutable
# python lists are mutable
L = [1,2,3]
L1 = [1,2,3]

print(L == L1)

print(id(1))
print(id(L1[0]))

# Creating a list
empty_list = []
print(empty_list)

oned_list = [1, 2, 3, 4, 5]
print(oned_list)

twod_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([1,2,3,[4,5]])
print(twod_list)

threed_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]] #homogeneous list    
print([1,2,3,[4,5,[6,7]]]) #heterogeneous list
print(threed_list)

print(list('hello')) # list of characters in the string
print(list(range(1, 11))) # list of numbers from 1 to 10
