# -*- coding: utf-8 -*-
"""Lab 1 TSV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O9VAcnfqGmoLi30sLy7tUR-akFB5BI4b
"""

with open('/content/data.tsv', 'r', encoding='latin-1') as file:
    lines = file.readlines()
print(lines)

length=len(lines)
print(length)

import pandas
data=pandas.read_csv('/content/data.tsv',sep='\t',encoding='latin-1')
instances=data.shape[0]
print(instances)
rows=data.shape[1]
print(rows)