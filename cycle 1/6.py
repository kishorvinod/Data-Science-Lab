print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("**************************************************")
for num in range(1, 1001):
    num_str = str(num)
    num_digits = len(num_str)

    digit_sum = sum(int(digit) ** num_digits for digit in num_str)

    if num == digit_sum:
        print(num)
