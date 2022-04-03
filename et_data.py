# -*- coding: utf-8 -*-
"""et_data

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10vK13qtznIQLIXG81Aqjamx9Be7UqQGp
"""

import csv
from xlsxwriter.workbook import Workbook
  
tsv_file = 'WEEKLY_DATA.tsv'
xlsx_file = 'output.xlsx'

workbook = Workbook(xlsx_file)
worksheet = workbook.add_worksheet()
  
read_tsv = csv.reader(open(tsv_file, 'r', encoding='utf-8'), delimiter='\t')
  
for row, data in enumerate(read_tsv):
    worksheet.write_row(row, 0, data)
  
workbook.close()

import pandas as pd

df = pd.read_xlsx("output_data.xlsx")
df.count()

df.dropna(axis=0,how='any',inplace=True)
df.count()