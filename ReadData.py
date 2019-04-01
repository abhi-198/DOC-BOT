# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:35:12 2019

@author: Abhishek
"""

import csv

filename = "dataset.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    
    for row in csvreader:
        rows.append(row)
    print("total no. of rows : %d"%(csvreader.line_num))

print('Field names are:' + ', '.join(field for field in fields)) 

print("Data set")
for row in rows:
    for col in row:
        print(col)
    print()