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