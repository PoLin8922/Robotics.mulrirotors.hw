import xlrd
import numpy as np

data = xlrd.open_workbook('HW4-1.xls')

for n in range(len(data.sheet_names())):
    table = data.sheets()[n]

list_in = []
list_out = []
for i in range(1,51):
   list_in.append(table.row_values(i)[:2])
   list_out.append(table.row_values(i)[2:])

A_in  = np.array(list_in)
A_out = np.array(list_out)

tmp = A_in.T@A_in
result = np.linalg.inv(tmp) @ A_in.T @ A_out
print(result)
print(f'out = {result[0]}*input1 + {result[1]}*input2 ')


