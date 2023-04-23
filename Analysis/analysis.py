from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from prettytable import PrettyTable

sentences = [
    "an array is a data structure that stores a collection of values, all of the same type,in contiguous memory locations. Each value in an array is identified by an index or a subscript,which is a non-negative integer that represents its position in the array. The index of the first element in an array is typically 0, and the index of the last element is usually one less than the size of the array.",
    "Array is a collection of homogeneous data.It is continuous in memory",
    "Arrays are linear and static data structure that contains collection of similar types of elements",
    "It is a derived datatype which can hold data of same datatype",
    "Array is used to store multiple values using single variable name of same datatype",
    "Array is used to store multiple values using single variable name of same datatype. It uses [] to define an array. It can be referenced using its index. Eg int a[2]={1,2};",
    "Array is a data structure that can store homogenous data",
    "Array is a  that stores a collection of elements, such as integers, characters, or other data types, that are of the same data type and are stored contiguously in memory.The elements in an array are identified by their index or position, which starts at 0 for the first element and increments by 1 for each subsequent element.",
    "Array data structure collection of values same type contiguous index 0 non negative last element less than size"

]
answers_from = [
    "Vishnu",
    "Aswathi",
    "Shifan",
    "Amal",
    "Shifan 2",
    "Vaishnav",
    "Kesiyapriya",
    "Shifan 3"
]


def similarity_analysis(model_name,sentences):
    model = SentenceTransformer(model_name)

    sentence_embeddings = model.encode(sentences)

    # print(sentence_embeddings.shape)
    # print(sentence_embeddings)

    arr = cosine_similarity(
        [sentence_embeddings[0]],
        sentence_embeddings[1:]
    )
    return arr[0]
    # t = PrettyTable(['Name', 'Similarity'])
    # for name, similar in zip(answers_from, arr[0]):
    #     t.add_row([name, similar])
    # return t


models = ['all-mpnet-base-v2', 'multi-qa-mpnet-base-dot-v1', 'all-distilroberta-v1', 'all-MiniLM-L12-v2',
          'multi-qa-distilbert-cos-v1', 'all-MiniLM-L6-v2', 'multi-qa-MiniLM-L6-cos-v1',
          'paraphrase-multilingual-mpnet-base-v2',
          'paraphrase-albert-small-v2', 'paraphrase-multilingual-MiniLM-L12-v2', 'paraphrase-MiniLM-L3-v2',
          'distiluse-base-multilingual-cased-v1',
          'distiluse-base-multilingual-cased-v2', 'bert-base-nli-mean-tokens','bert-large-nli-mean-tokens']


def main():
    with open("output.txt", "w+") as fp:
        # print(i)
        # print(test_models(i))
        # print("\n********************************\n")
        for i in models:
            print(i)
            print(similarity_analysis(i, sentences))
            print("\n********************************\n")


            # fp.write(i)
            # fp.write("\n")
            # fp.write(str(test_models(i)))
            # fp.write("\n********************************\n")


if __name__=="__main__":
    main()