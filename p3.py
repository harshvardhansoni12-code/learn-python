# strings:
s = 'ssiuc rads'
rev = ""
for i in s:
    rev = i + rev
print(rev)

for i in s:
    print(i)
v = 0
c = 0
for i in s:
    if i in 'aeiou':
        v += 1
    else:
        c +=1
print("vowels", v)
print("consonants", c)


# nested loops:
for i in range (1,4):
    for j in range (1,i+1):
        print(j , end="")
    for k in range (i-1, 0, -1):
         print(k , end="")    
    print()
