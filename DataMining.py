import numpy as np
import csv
from keras.layers im

def vectorize(samples):
  token_index = {}
  for sample in samples:
    for word in sample.split():
      if word not in token_index:
        token_index[word] = len(token_index) + 1

  max_length = 10
  results = np.zeros(shape=(len(samples),max_length,max(token_index.values()) + 1))

  for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
      index = token_index.get(word)
      results[i, j, index] = 1.
      
  return results


filename = 'Dataset.csv'
data = dict()

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for disease,symtoms in reader:
        
        if disease in data:
            data[disease].append(symtoms)
        else:
            data[disease] = [symtoms]
        


for disease, symtoms in data.items():
    data[disease]= " ".join(symtoms)

x_train = vectorize(data.values())
x_label = vectorize(data.keys())

print(x_train,x_label)
