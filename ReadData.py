# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:35:12 2019

@author: Abhishek
"""

import csv

filename = "dataset.csv"

data = dict()
with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for disease,symtoms in reader:
        if disease in data:
            data[disease].append(symtoms)
        else:
            data[disease] = [symtoms]

print(len(data.values()))

for dis in data.values():
    print(dis)
    
print(len(data.keys()))

for dis in data.keys():
    print(dis)