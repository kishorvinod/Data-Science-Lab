print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("**************************************************")
def count_vowels(input_string):

    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


    input_string = input_string.lower()


    for char in input_string:
        if char in vowel_counts:
            vowel_counts[char] += 1

    return vowel_counts


input_string = input("Enter a string: ")


vowel_count = count_vowels(input_string)


for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")
