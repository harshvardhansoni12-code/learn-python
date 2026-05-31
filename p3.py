# # strings
s = 'ssiuc rads'
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)

# for i in s:
#     print(i)
v = 0
c = 0
for i in s:
    if i in 'aeiou':
        v += 1
    else:
        c +=1
print("vowels", v)
print("consonants", c)
