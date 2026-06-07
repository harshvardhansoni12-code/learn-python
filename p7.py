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