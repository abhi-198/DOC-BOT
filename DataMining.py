# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:00:12 2019

@author: Abhishek
"""


from keras.utils.np_utils import to_categorical
import numpy as np
import csv

def vectorize_sequence(sequences,dimension=1000):
  results = np.zeros((len(sequences),dimension))
  for sequence in enumerate(sequences):
    results[sequence] = 1
  return results

def to_one_hot(labels,dimension):
  results = np.zeros((len(labels),dimension))
  for i, label in enumerate(labels):
    results[i,label]=1
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

label = to_categorical(data.keys())
    
x_train = vectorize_sequence(data.values())
x_label = to_one_hot(data.keys(),133)