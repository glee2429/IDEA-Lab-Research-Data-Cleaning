from numpy import genfromtxt
import csv
import pandas as pd
import random
import math

file_name5 = 'omdb_rating20.csv'
df = pd.read_csv(file_name5)

duplicateRowsNum = len(df[df.duplicated('imdbID')])
print("Examples of the tuples that break FD in noise level 5: \n", df[df.duplicated('imdbID')])
print("Number of the tuples that break FD in noise level 5: ", duplicateRowsNum)

df_1 = df.drop_duplicates('imdbID', keep=‘last’)
print("Number of the total tuples after repair on noise level 5: ", len(df_1))

export_csv = df_1.to_csv('omdb_rating5_repair.csv', encoding='utf-8', index=False, header=True)


file_name10 = 'omdb_rating20.csv'
df = pd.read_csv(file_name10)

duplicateRowsNum = len(df[df.duplicated('imdbID')])
print("Examples of the tuples that break FD in noise level 10: \n", df[df.duplicated('imdbID')])
print("Number of the tuples that break FD in noise level 10: ", duplicateRowsNum)

df_2 = df.drop_duplicates('imdbID')
print("Number of the total tuples after repair on noise level 10: ", len(df_1))

export_csv = df_2.to_csv('omdb_rating10_repair.csv', encoding='utf-8', index=False, header=True)


file_name20 = 'omdb_rating20.csv'
df = pd.read_csv(file_name20)

duplicateRowsNum = len(df[df.duplicated('imdbID')])
print("Examples of the tuples that break FD in noise level 20: \n", df[df.duplicated('imdbID')])
print("Number of the tuples that break FD in noise level 20: ", duplicateRowsNum)

df_3 = df.drop_duplicates('imdbID')
print("Number of the total tuples after repair on noise level 20: ", len(df_1))

export_csv = df_3.to_csv('omdb_rating20_repair.csv', encoding='utf-8', index=False, header=True)
