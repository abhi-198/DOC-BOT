# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:46:34 2019

@author: Abhishek
"""
import pickle
import csv
import numpy as np
from sklearn.neural_network import MLPClassifier

filename = 'Dataset.csv'
data = dict()

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for disease,symtoms in reader:
        
        if disease in data:
            data[disease].append(symtoms)
        else:
            data[disease] = [symtoms]
        
symtoms = set()
for x in data.values():
  for y in x:
    symtoms.add(y)
    
symtoms = sorted(symtoms)


matrix = np.zeros((len(data.keys()),len(symtoms)))

i=0
for y in data.values():
  for x in y:
    matrix[i][symtoms.index(x)] = 1
  i+=1


disease = np.array([x for x in range(133)])

Disease_classifier = MLPClassifier(solver = 'lbfgs', alpha =1e-5, hidden_layer_sizes=(200,200), random_state = 1)
Disease_classifier.fit(matrix,disease)

filename = 'DOC-BOT_model.sav'
pickle.dump(Disease_classifier, open(filename, 'wb'))
 
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(matrix, disease)

print(result)
