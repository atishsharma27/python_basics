num1 = int(input("Enter first number=\n"))
num2 = int(input("Enter second number=\n"))

if num1>num2:
    mn = num2
else:
    mn = num1
for i in range(1,mn+1):
    if num1%i==0 and num2%i==0:
        hcf=i


lcm = (num1 * num2) // hcf

print(f"The HCF of {num1} and {num2} is {hcf}")
print(f"The LCM of {num1} and {num2} is {lcm}")
