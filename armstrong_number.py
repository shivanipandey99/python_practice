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

write a program to print hello world.
