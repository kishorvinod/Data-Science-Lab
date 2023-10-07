import math

print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("**************************************************")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


gcd = math.gcd(num1, num2)

if gcd == 1:
    print(f"{num1} and {num2} are coprime.")
else:
    print(f"{num1} and {num2} are not coprime. Their GCD is {gcd}.")
