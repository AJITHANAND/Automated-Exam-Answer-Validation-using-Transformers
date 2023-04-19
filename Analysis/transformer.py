import torch
from transformers import AutoTokenizer, AutoModel

# Load pre-trained BERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
model = AutoModel.from_pretrained("bert-base-cased")

# Define the two sentences to compare
sentence_1 = "an array is a data structure that stores a collection of values, all of the same type,in contiguous memory locations. Each value in an array is identified by an index or a subscript,which is a non-negative integer that represents its position in the array. The index of the first element in an array is typically 0, and the index of the last element is usually one less than the size of the array."
sentence_2 = "Array is a collection of homogeneous data.It is continuous in memory"

# Tokenize the sentences and convert them into PyTorch tensors
inputs = tokenizer([sentence_1, sentence_2], padding=True, truncation=True, return_tensors="pt")

# Pass the inputs through the BERT model to get the embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Extract the embeddings for the two sentences
sentence_1_embedding = outputs.last_hidden_state[0][0]
sentence_2_embedding = outputs.last_hidden_state[0][1]

# Compute the cosine similarity between the two embeddings
cos_sim = torch.nn.functional.cosine_similarity(sentence_1_embedding, sentence_2_embedding)

print("Cosine similarity:", cos_sim.item())
