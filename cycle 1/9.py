print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("**************************************************")

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]


if len(list1) == len(list2):

    result = []


    for i in range(len(list1)):
        sum_element = list1[i] + list2[i]
        result.append(sum_element)

    print("Resultant list after adding elements:", result)
else:
    print("Lists are of different lengths. Cannot perform element-wise addition.")
