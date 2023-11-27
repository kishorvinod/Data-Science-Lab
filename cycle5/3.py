def gen_ngrams(text,WordsToCombine):
    words=text.split()
    output=[]
    for i in range(len(words)-WordsToCombine+1):
        output.append(words[i:i+WordsToCombine])
    return output
print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("*************************************************")
x=gen_ngrams(
    text='The data set given satisfies the requirement for model generation., This is used in Data Science Lab',
    WordsToCombine=3
)
print(x)