# print hello world
print("hello world")
# take input
a = input("enter the name:")
print(type(True))
#boolean is True not 'true'
# python is case sensitive

print("hello",1,0.1,True,sep=',')
print("hello",end='-')
print("world")
print("world")
print("rdj")
# data types:

# Integers
print(8)
print(1e308) # this is 1 * 10^308

# float
print(0.2)

#boolean
print(True)

#string
print('hello')

# complex
print(5+9j)

# c ka array same as python ka list
print([1,2,3,4,5])

# tuple
print((1,2,3))

#set 
print({1,2,3})

#dictionary
print({'name':'harsh' , 'sem':'4'}) # {'key': 'value'} form

# variable
# create var in python
name = 'nitish'
print(name)

a = 2
b=4
print(a+b)

# var never declared they are created when needed

# Dynamic typing
a = 5 # not telling data type of var

#static typing
# int a = 3

# Dynamic Binding
a =5 
print(a) # data type is not fixed
a = 'hello'
print(a)
# static binding
# int z = 5 // data type of integer will be fixed

a=2
b=3
c=4
print(a,b,c , sep='\n\n\n')

a,b,c=2,3,4
print(a,b,c)
# 1:04:24 {start from here}

# keywords and identifiers
a = int(input('Enter a:'))
b = int(input('enter b:'))

c =a + b
print(c)