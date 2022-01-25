'''
Koostas: Rauno Vaher
Kursus: TAK21
'''
#Libry
from numpy import random
from datetime import datetime
import csv
import os
import os.path
import pandas as pd 

#Making random numbers
a = random.randint(1,10, size=(5))
b = random.randint(1,10, size=(5))
#Lists
a_list = list(a)
b_list = list(b)
isSquare = []
isRectangle = []
#File nime in to variable
dst = 'ristkulik.csv'
print(a, b) #Test
#Calculationg is Square or Rectangle and storing answers to new list
for a, b in zip(a, b): 
    if a == b:
        isSquare.append('Yes')
    else:
        isRectangle.append(a * b)
print(isSquare, isRectangle) #Test
#Using pandas to get dataframe
data = [a_list, b_list, isRectangle, isSquare]
#print('testiks',data) #Test
data = pd.DataFrame([a_list,b_list, isRectangle, isSquare]) #Each list would be added as a row
data = data.transpose() #To Transpose and make each rows as columns
data.columns=['a','b', 'S', 'isSquare'] #Rename the columns
data.insert(0, 'datetime', pd.to_datetime('now').strftime("%m/%d/%Y %H:%M:%S"))
data.head()
data.fillna('Null', inplace=True)
print(data) #Test

#Checking does file exists
if os.path.exists(dst): 
    filesize = os.path.getsize(dst) #Is file empty or not
    print('Your file size: ', filesize)
    with open(dst, 'a', encoding='utf-8') as fn:
        if filesize == 0:
            data.to_csv(fn, index=False, sep=';', header=True, line_terminator='\n')
        else:
            data.to_csv(fn, index=False, sep=';', header=False, line_terminator='\n')
#If we don't have a file we create it
else:
    with open(dst, 'x', encoding='utf-8') as fn:
        data.to_csv(fn, index=False, sep=';', header=True, line_terminator='\n')
    