import collections
import pandas as pd
import matplotlib.pyplot as plt
file = open('corpus.txt', encoding="utf8")
corpus = file.read()
wordcount = {}
for word in corpus.split(' '):
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
file.close()
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')
plt.show()