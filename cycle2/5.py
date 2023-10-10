import numpy as np
print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("*************************************************")
import numpy as np

even_numbers = np.arange(2, 31, 2)

subset_a = even_numbers[2:9:2]
subset_a_slice = even_numbers[2:9:2]
print("a. Elements from index 2 to 8 with step 2:")
print(subset_a)
print("Slice Function Equivalent:")
print(subset_a_slice)

last_three = even_numbers[-3:]
print("\nb. Last 3 elements of the array using negative index:")
print(last_three)

alternate_elements = even_numbers[::2]
print("\nc. Alternate elements of the array:")
print(alternate_elements)

last_three_alternate = even_numbers[-3::2]
print("\nd. Last 3 alternate elements:")
print(last_three_alternate)

