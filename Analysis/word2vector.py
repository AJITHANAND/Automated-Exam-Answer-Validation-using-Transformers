import pandas as pd
import re
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import string
import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from nltk import word_tokenize
from gensim.models import Word2Vec as w2v
from sklearn.decomposition import PCA

PATH = 'data/shakespeare.txt'
sw = stopwords.words('english')
plt.style.use('ggplot')

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

correct_answer = "an array is a data structure that stores a collection of values, all of the same type, " \
                 "in contiguous memory locations. Each value in an array is identified by an index or a subscript, " \
                 "which is a non-negative integer that represents its position in the array. The index of the first " \
                 "element in an array is typically 0, and the index of the last element is usually one less than the " \
                 "size of the array."
# import data
lines = []
for i in re.split(r'[,.]', correct_answer.strip()):
    lines.append(i.strip())
print(lines)

# ************************************************ process data ****************************************************


# remove new lines
lines = [line.rstrip('\n') for line in lines]

# make all characters lower
lines = [line.lower() for line in lines]

# remove punctuations from each line
lines = [line.translate(str.maketrans('', '', string.punctuation)) for line in lines]

# tokenize
lines = [word_tokenize(line) for line in lines]


def remove_stopwords(lines, sw=sw):
    '''
    The purpose of this function is to remove stopwords from a given array of
    lines.

    params:
        lines (Array / List) : The list of lines you want to remove the stopwords from
        sw (Set) : The set of stopwords you want to remove

    example:
        lines = remove_stopwords(lines = lines, sw = sw)
    '''

    res = []
    for line in lines:
        original = line
        line = [w for w in line if w not in sw]
        if len(line) < 1:
            line = original
        res.append(line)
    return res


filtered_lines = remove_stopwords(lines=lines, sw=sw)

print(filtered_lines)

# ----------------------------- embed word2vec ----------------------------------------------------


w = w2v(
    filtered_lines,
    min_count=3,
    sg=1,
    window=7
)

print(w.wv.most_similar('array'))

emb_df = (
    pd.DataFrame(
        [w.wv.get_vector(str(n)) for n in w.wv.key_to_index],
        index=w.wv.key_to_index
    )
)
print(emb_df.shape)
emb_df.head()

pca = PCA(n_components=2, random_state=7)
pca_mdl = pca.fit_transform(emb_df)

emb_df_PCA = (
    pd.DataFrame(
        pca_mdl,
        columns=['x', 'y'],
        index=emb_df.index
    )
)

plt.clf()
fig = plt.figure(figsize=(6, 4))

plt.scatter(
    x=emb_df_PCA['x'],
    y=emb_df_PCA['y'],
    s=0.4,
    color='maroon',
    alpha=0.5
)

plt.xlabel('PCA-1')
plt.ylabel('PCA-2')
plt.title('PCA Visualization')
plt.plot()
