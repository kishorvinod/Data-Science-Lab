from nltk import ngrams
sentence='I reside in Bengaluru'
n=3
print("*************************************************")
print("SJC22MCA-2035 : KISHOR VINOD")
print("MCA 2022-24")
print("*************************************************")
unigrams=ngrams(sentence.split(),n)
for grams in unigrams:
    print(grams)