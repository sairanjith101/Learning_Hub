from collections import Counter

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
sen_split = sentence.split()
print(Counter(sen_split))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

sen_dict = {}
for sen in sen_split:
    if sen not in sen_dict:
        sen_dict[sen] = 1
    else:
        sen_dict[sen] += 1

print(sen_dict)