# accessing element in list 
my_list = ["hello", [2], (3), {4}, 5]
print(len(my_list))
# positive indexing
print(my_list[0]) # first element
for i in range(0,5):
    print(my_list[i])
print()
# negative indexing
# -1 is last element
print(my_list[-1]) # last element    

print()

h = [[[1,2],[2,3]],[[3,4],[4,5]]]
print(h[0]) 
print(h[0][0])
print(h[0][1][1])

print()

l = [1, 2, 3, 4, 5]
# slicing list positivwe
print(l[0:3]) # slicing list from index 0 to 2
print(l[2:5]) # slicing list from index 2 to 4
print(l[:3]) # slicing list from index 0 to 2
print()
print(l[2:]) # slicing list from index 2 to end
print(l[:]) # slicing list from index 0 to end

# NEGATIVE SLICING
print(l[-3:]) # slicing list from index -3 to -2   
print(l[:-2]) # slicing list from index 0 to -3
print(l[-4:-1]) # slicing list from index -4 to -2
print()
print(l[0::2]) # slicing list from index 0 to end with step 2
print(l[-5:-2:2]) # slicing list from index -5 to -3 with step 2    

# Adding elements to list 

h = [[[1,2],[2,3]],[[3,4],[4,5]]]

# append
h.append([6,6]) # adding element to end of list
print(h)

# extend
h.extend([[7,7]]) # adding element to end of list
print(h)

new_list = ["harsh","arun","asim","atul"]
new_list.extend(["sahil","rsd"]) # adding element to end of list
print(new_list)

# insert
new_list.insert(2,"sahil") # adding element at index 2
new_list.insert(3,"rsd") # adding element at 4 th place 
print(new_list)

L = [1, 2, 3, 4, 5]
L.insert(4,6) # adding element at index 4
print(L)
print(len(L))


k = [1, 2, 3, 4, 5, 6]
k[-1] = 400
k[0] = 100
k[2] = 300
k[4] = 500
k[1:3] = ["123","23333","HARSH"]
print(k) # replacing last element with 400

# deleting items from list

# keyword -->>  del // element index is given
L = [1, 2, 3, 4, 5]
del L[0] # deleting element at index 0
print(L)
del L[1:3] # deleting elements from index 1 to 2
print(L)
del L[:] # deleting all elements
print(L)

# keyword -->>  remove // element value is given
L = [1, 2, 3, 4, 5]
L.remove(3) # deleting element with value 3
print(L)
L.remove(5) # deleting element with value 5


print(L)
l = [1, 2, 3, 4, 5]
l.remove(2) # deleting element with value 2
# l.remove(l[1:4]) this will give error because remove() method takes only one argument

# keyword -->>  pop // element index is given
L = [1, 2, 3, 4, 5]
L.pop() # deleting last element
print(L)

L.pop(1) # deleting element at index 1
print(L)


# keyword -->>  clear // all elements are deleted
L = [1, 2, 3, 4, 5]
L.clear() # deleting all elements
print(L)

# operations on list