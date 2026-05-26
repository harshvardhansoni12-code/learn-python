# Operator

# Arithmetic
print("Arithmetic")
print(5+6)
print(5-6)
print(5*6)
print(5/6)
print(5//3)
print(5%2)
print(5**2)

# Relational
print("Relational")
print(4>5)
print(4<5)
print(4>=4)
print(4<=4)
print(4==7)

# Logical (AND , OR , NOT)
print("Logical")
print(1 and 0)

print(1 or 0)

print(not 1 ,sep='\n\n')

# Bitwise 

# Assignment Operators
print("Assignment Operators",end='\n\n')
a = 6
a+=5
print(a)

#  Membership operator
print("Membership operator:" , end='\n\n\n')

print('D' in 'Delhi')
print('l' not in 'list')
print('k' in 'delhi')
print('f' in 'fish')

# //30:15

# if 'k' in 'list':
#     print("i love my india")
# else:
#      print("i will still love india") 

# number = 543
# a = number%10
# print(a)
# number = number//10
# b = number%10
# print(b)  #this is rem
# c =number//10
# print(c)
# # 43:20
# sum = a+b+c
# print(sum)

name = input("Enter your name:")
password = input("Enter your password:")
if name == "admin" and password == "admin123":
    print("Welcome admin!")
elif name == "admin" and password != "admin123":
    password = input("Incorrect password. Please try again:")
    if password == "admin123":
        print("Welcome admin!")
    else:
        print("Invalid password.")
else:
    print("Invalid credentials. Access denied.")