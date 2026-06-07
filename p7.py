# accessing element in list 
my_list = ["hello", [2], (3), {4}, 5]

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
