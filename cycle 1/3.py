print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("**************************************************")
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("It is an equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("It is an isosceles triangle.")
    else:
        print("It is a scalene triangle.")
else:
    print("It is not a valid triangle.")
