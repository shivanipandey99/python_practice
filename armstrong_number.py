n = int(input("enter any number:"))
n2 =n
t_digit = len(str(n))
sum = 0
while n>0:
    last_digit = n%10
    sum = sum+(last_digit**t_digit)
    n= n//10
if sum==n2:
    print(f"{n2} in a armstrong number.")
else:
    print(f"{n2} in a armstrong number.")
    
    1. Write a program to input basic salary of an employee and calculate
its Gross salary according to following:
Basic Salary &lt;= 10000 : HRA = 20%, DA = 80%
Basic Salary &lt;= 20000 : HRA = 25%, DA = 90%
Basic Salary &gt; 20000 : HRA = 30%, DA = 95%

salary = float(input("Enter basic salary: "))

if salary <= 10000:
    hra = 0.20 * salary
    da = 0.80 * salary
elif salary <= 20000:
    hra = 0.25 * salary
    da = 0.90 * salary
else:
    hra = 0.30 * salary
    da = 0.95 * salary

gross = salary + hra + da
print("Gross Salary is:", gross)

1.write a program to print hello world.
s = "Hello World"
print(s)

2.write a python program to do aritimetic operations and divition 
#addition
num1=float(input("enter the first number of addtion"))
num2=float(input("enter the second number of addtion"))
sum_result = num1+num2
print(f"sum+{num1}+{num2}={sum_result}")

#division
num3=float(input("enter the divident number of division"))
num4=float(input("enter the divisor number of division"))
if num 4==0:
    print("error":division by zero is not allowed")
else:
 div_resulte =num3 / num4
 print(f"additin+{num1}+{num2}={sum_result}")
 
 3.wap to find the area of circle 
 base = float(input("enter the lenght of the base of the tiriangle:"))
 height = float(input("enter the height of the tiriangle:"))
 #calculate the thriangle of area
 area = 0.5* base*height
 print(f"the area of triangle is:{area}")
 11.Write a Python Program to Check if a Number is Positive, Negative or Zero
 num1 = int(input("enter a number"))
 if num1 > 0 :
 print("positive number")
 
 3.wap to find the area of circle 
 base = float(input("enter the lenght of the base of the tiriangle:"))
 height = float(input("enter the height of the tiriangle:"))
 #calculate the thriangle of area
 area = 0.5* base*height
 print(f"the area of triangle is:{area}")
 11.Write a Python Program to Check if a Number is Positive, Negative or Zero
 num1 = int(input("enter a number"))
 if num1 > 0 :
 print("positive number")
 
 # break 4 ke bad break ho jayega 
arr = np.array([1,2,3,4,5])
print(arr)

# concat along the 
n=int(input("enter any no"))
fact=5
i=1
while i<=n:
     fact=fact*i
     i=i+1
     print(f'factorial of {n} is ={fact}')
     
     arr = [0,1,2]
print(np.tile(arr,(2,2)))

#pass current block ko skip kar deta hai 
n=int(input("enter any number"))
i=1
while i<=n:
    if i==7:
        pass
    else:
       print(i)
    i=i+1
    
    # wap to python print random function 
    import random
      print(random.random())
  
  
  import random
print(random.randint(1, 100))