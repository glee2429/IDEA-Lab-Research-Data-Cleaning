from numpy import genfromtxt
import csv
import pandas as pd
import random
import math

file_name = 'googlescholar_venue.csv'
df = pd.read_csv(file_name)

print(df.shape)
print(df)

counter5 = 0
len = len(df.index)

for i in range(0, len-1):
    value = random.randint(0,len-1)
    threshold = math.floor(len*0.05)
    if value < threshold:
        df.iloc[i,0] = df.iloc[i+1, 0]
        counter5 += 1

ratio5 = counter5/len

print(df)
print("The number of updated values with 5% noise: ", counter5)
print("The ratio of updated values with 5% noise: ", ratio5)

export_csv = df.to_csv('googlescholar_venue5.csv', encoding='utf-8', index=False, header=True)


counter10 = 0

for i in range(0, len-1):
    value = random.randint(0,len-1)
    threshold = math.floor(len*0.1)
    if value < threshold:
        df.iloc[i,0] = df.iloc[i+1, 0]
        counter10 += 1

ratio10 = counter10/len

print(df)
print("The number of updated values with 10% noise: ", counter10)
print("The ratio of updated values with 10% noise: ", ratio10)

export_csv = df.to_csv('googlescholar_venue10.csv', encoding='utf-8', index=False, header=True)

counter20 = 0

for i in range(0, len-1):
    value = random.randint(0,len-1)
    threshold = math.floor(len*0.2)
    if value < threshold:
        df.iloc[i,0] = df.iloc[i+1, 0]
        counter20 += 1

ratio20 = counter20/len

print(df)
print("The number of updated values with 20% noise: ", counter20)
print("The ratio of updated values with 20% noise: ", ratio20)

export_csv = df.to_csv('googlescholar_venue20.csv', encoding='utf-8', index=False, header=True)
