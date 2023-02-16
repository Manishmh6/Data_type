#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q 1 } Given two strings the task is to check whether the given string are anagrams of each other an anagram of a string is 
# listen
# silent


# In[1]:


L = "listen"
L1 = "silent"

print(sorted(L))
print(sorted(L1))

if sorted(L)==sorted(L1):
    print("Anagrams")
else:
    print("This is No Anagram")


# In[2]:


# questions 1 
L = "listen"
L1 = "silent"
if len(L)==len(L1):
    L_sorted=''.join(sorted(L))
    L1_sorted=''.join(sorted(L1))
    if sorted(L)==sorted(L1):
        print("Anagram")
    else:
        print("not")
else:
    print("n")


# In[ ]:


# [questions 2 ] find a maximum and minimum in arraye
W = []
size= int(input("Enter the value = "))
for i in range(size):
    va= int(input("Enter the value = "))
    W.append(va)
a = max(W)
b= min(W)
print("Max value = ",a)
print("Min value = ", b)


# In[ ]:


# 2 Questions second Method 
u = []
d = int(input("enter the value = "))
for i in range(d):
    val=int(input("enter the value= "))
    u.append(val)
print("Origanle List =",u)

max=u[0]
for i in range(d):
    if (u[i]>max):
        max=u[i]
print("Max value = ",max)

min=u[0]
for i in range(d):
    if (u[i]<min):
        min=u[i]
print("Min value = ",min)


# In[ ]:


# Questions 3] Write a python program to collect all consecutive number from index 0 into list input [2,9,3,1,2,3,5,7,8,0,2,3,4,5,1,0,7,6,7,9,8,7,3,2,1,2,3,5,6,7]


# In[ ]:


l = [2,9,3,1,2,3,5,7,8,0,2,3,4,5,1,0,7,6,7,9,8,7,3,2,1,2,3,5,6,7]
x=l.index(0)
print(x)


# In[ ]:





# In[ ]:


num= [1,2,3,4,5,6]
val=num.index(2)
print(val)


# In[ ]:





# In[ ]:


# 4 Questions write program to transpose a matrix
L = [[1,2,3],
    [4,5,6],
     [7,8,9]]

for i in range(3):
    
    for j in range(3):
         
        print(L[i][j],end='  ')
    print("")


# In[ ]:


# Q 4
A = [[1,2,3],
    [4,5,6]]
    
T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
for i in T:
    print(i)


# In[ ]:


L = [[1,2,3],
     [4,5,6]]
T = [[0,0,],
    [0,0],
    [0,0]]
     

for i in range(len(A)):
    
    for j in range(len(A[0])):
        
        T[j][i]=A[i][j]
for i in T:
    print(i)


# In[ ]:


# Questions 4
def matrix_sum(matrix):
    
    total = 0
    for row in matrix:
        
        for element in row:
            
            total += element
            
        return total
    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = matrix_sum(matrix)
print("Matrix")
print(matrix)

print()
    


# In[41]:


# Q  5 Sum

a = []
sum=0
m = int(input("Enter the m value="))
for i in range(m):
    v=int(input("Enter the value="))
    a.append(v)
print(a)
#sum=0
for i in range(m):
    sum=sum+a[i]
    
print(sum)


# In[ ]:


# Questions 7
def find(arr1, arr2, arr3):
    print("Common elements between all three array: ", end="")
    for i in arr1:
        if i in arr2 and i in arr3:
            print(i, end=" ")


array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]
array3 = [3, 5, 6, 7]

print("Array1 = ", array1)
print("Array2 = ", array2)
print("Array3 = ", array3)

find(array1, array2, array3)


# In[ ]:


# Questions  10
AB = []

AC = int(input("Enter the value= "))

for i in range(AC):
    
    value=int(input("Enter the value= "))
    
    AB.append(value)
    
print("Original list = ",AB)

Left = AB[0]

for i in range(1,AC):
    
    AB[i-1]= AB[i]
    
AB[AC-1]=Left
print("Rotate list= ",AB)


# In[ ]:





# # Part 2 Exampal no 1

# In[44]:


# 1 Given an integer x return true if x is a palindrome and false otherwise 

I = int(input("Enter the Number = "))
REV=0
X = I 
while 0<I:
    REV=(REV*10)+I%10
    I=I//10
if (X==REV):
    print("Plindrome number True = ",X)
else:
    print("False")
    


# In[ ]:


I = int(input("Enter the Number = "))
REV=0
X = I 
while 0<I:
    REV=(REV*10)+I%10
    I=I//10
if (X==REV):
    print("Plindrome number True = ",REV)
else:
    print("False")
print(I)


# In[ ]:


I = int(input("Enter the Number = "))
REV=0
X = I 
while 0<I:
    REV=(REV*10)+I%10
    I=I//10
if (X==REV):
    print("Plindrome number True = ",X)
else:
    print("False")
print(X)   


# # part 3 

# In[ ]:


# q 1 write a program to print the pattern below


# In[ ]:


# 1 
for i in range(5, 0, -1):
    
    for j in range(i, 0, -1):
        
        print(j,end=' ')
    print()


# In[ ]:


# Q 2
for i in range(4, -1, -1):
    
    print('_ '*i, end=' ')
    
    for j in range(i+1, 6):
        
        print(j, end=' ')
        
    print( )


# In[46]:


# Q 3 
A = 1
B = 6
C = 5
D = int(input("Enter the value = "))
print("Series Numbers  ")

while A<=D:
    print(B,end=' ')
    B=B+C
    C=C+5
    A=A+1


# In[ ]:


# Q 4
numbers = [5,13,56,91,33,79,29,81,67,45]
sum = 0
for num in numbers:
    prime = True
    if num <= 1:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
    if prime:
        sum += num**2
print("Sum of squares of prime numbers:", sum)


# In[ ]:


import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [5,13,56,91,33,79,29,81,67,45]
sum = 0
for num in numbers:
    if is_prime(num):
        sum += num**2
print("Sum of squares of prime numbers:", sum)


# In[ ]:


string1 = "Hello"
string2 = "World"

# Using arithmetic operations
string1 = string1 + string2
string2 = string1[0:len(string1)-len(string2)]
string1 = string1[len(string2):]

print("String 1: ", string1)
print("String 2: ", string2)


# In[ ]:


# Using tuple unpacking

# Q 5
str1 = "Hello"
str2 = "Learn class"

str1, str2 = str2, str1

print("String 1: ", str1)
print("String 2: ", str2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[40]:


numbers = [5,13,56,91,33,79,29,81,67,45]
sum = 0
for num in numbers:
    if is_prime(num):
        sum += num**2
print("Sum of squares of prime numbers:", sum)


# In[ ]:


A = []
size=int(input("Enter the value = "))
for i in range(size):
    val=int(input("Enter the  value = "))
    A.append(val)
print("origanl list",A)
Right = A[size-1]
for i in range(size-2,-1,-1):
    
     A[i+1]=A[i]
A[0]=Right
print(A)


# In[ ]:





# In[ ]:


# write a program to find sum of evan number 
Y =int(input("Enter tha value= "))
A =1
sum = 0
count=0
while (count<Y):
    if (A%2==0):
        print(A)
        sum=sum+A
        count=count+1
    A=A+1
print("Sum Evan number=",sum)


# In[30]:


R = []
sise= int(input("enter = "))
for i in range (sise):
    v= int(input("enter the value "))
    R.append(v)
print(R)
right=R[sise-1]
for i in range(sise-2,-1,-1):
    R[i+1]=R[i]
R[0]=right
print(R)


# In[ ]:





# In[ ]:





# In[ ]:


# 1 write a program prime number 

n  = int(input('Enter the value = '))
i = 1
count= 0
while n>=i:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print("This is Prime number")
else:
    print('no')


# In[ ]:


# 2 write a program Fatorial number

i = int(input('Enter the  value = '))
fac=1
while i>0:
    print(fac)
    fac=fac*i
    i=i-1
    #print(fac)


# In[ ]:


# 3 Fibonicce 

i = int(input('Enter thye value = '))
x= 0 
y = 1
z =0
while i>=z:
    print(z)
    x=y
    y=z
    z=x+y


# In[ ]:


# Q 4 Find LCM 

N1=int(input("N1 = "))
N2=int(input("N2 = "))
if N1>N2:
    G = N1
else:
    G = N2
while True:
    
    if G%N1==0 and G%N2==0:
        
        LCM=G
        break
    G=G+1
print("This is LCM",LCM)
        


# In[ ]:


# 5 REmove Punctuations for sting

punc= '''\][]((*><><?.,%$@!!?":?/';/'"))######'''
n = input("Anything ")
empty = ''
for i in n:
    if i not in punc:
        empty+=i
print("Orignal String : = ",empty)
        


# In[ ]:


#Q 6 calculator

A = int(input('Enter the value A = :'))
B = int(input('Enter the value B = :'))
op=input("OPE +,-,*,/,%")
if op=="+":
    print(A+B)
elif op=="-":
    print(A-B)
elif op=="*":
    print(A*B)
elif op=="/":
    print(A%B)
else:
    print("Error")


# In[ ]:


# Add two Metrics' 

A = [[1,2,3],
    [4,5,6],
    [7,8,9]]

B = [[10,11,12],
    [13,14,15],
    [16,17,18]]

Result= [[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        Result[i][j]= A[i][j] + B[i][j]

for r in Result:
    print(r)


# In[ ]:


n = int(input("Enter the value "))
rev  = 0
x=n
while n>0:
    rev=(rev * 10)+n%10
    n=n//10
    
    print(rev)
if x==rev:
    print("this pelidrom number")
else:
    print("this not ")


# In[ ]:





# In[21]:


l = [1,2,3,4,5,6,7,15]
for i in l:
    if i%2==0:
        print("evan",i)
    else:
        print("odd",i)


# In[25]:


A = []
size =  int(input("Entr the value "))
for i in range(size):
    val= eval(input("Enter the value add = "))
    A.append(val)
print("origal",A)
lef = A[0]
for i in range(1,size):
    A[i-1]=A[i]
A[i]=lef
print(A)


# In[34]:


AB=[]
b = 5 #eval(input('Enter the value = '))
for i in range(b):
    val=eval(input(" Add value = "))
    AB.append(val)
print("Original",AB)
rigt= AB[size-1]
for i in range(size-2,-1,-1):
    AB[i+1] = AB[i]
AB[0]=rigt
print('Rotede list',AB)


# In[39]:


AB=[]
b = 5 #eval(input('Enter the value = '))
for i in range(b):
    val=eval(input(" Add value = "))
    AB.append(val)
print("Original",AB)
right = AB[b-1]
for i in range(b-2,-1,-1):
    
    AB[i+1] = AB[i]
AB[0]=right
print(AB)


# In[ ]:





# In[83]:



pac = '''<>,.#@!%^&*(){1234567890}[]|\/*"";:/?`~$#@!&'''
a = input("Enter the = ")
empty = ''
for i in a:
    if i not in pac:
        empty=empty+i
print(empty)


# In[84]:


pac = '''<>,.#@!%^&*(){}[]|\/*"";:/?`~$#@!&'''
A  = input('Entrr the extension = ')
empty = ''
for i in A:
    if i not in pac:
        empty=empty+i
print('empty',empty) #


# In[ ]:




