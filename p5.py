# for i in 'delhi':
#     print('pune')

# print('c' in 'Delhi')

s = 'delhi'
# common functions for string
# len
print(len(s))
# max
print(max(s)) # max is found on the basis of ascii value of the character
# min
print(min(s))
# sorted
print(sorted(s)) # sorted returns a list of characters in ascending order of their ascii values

# Capitalize / Title / Upper / Lower

s = 'hello world'

print(s.capitalize())

print(s.title())

print(s.upper())

print(s.lower())

# Count/find/index

s = 'hello world'
print(s.count('l')) # count returns the number of occurrences of the substring in the string
print(s.find('l')) # find returns the index of the first occurrence of the substring in the string
print(s.index('l')) # index returns the index of the first occurrence of the substring in the string

# Replace
s = 'hello world'
print(s.replace('l', 'x')) # replace returns a new string with all occurrences of the first argument replaced by the second argument    