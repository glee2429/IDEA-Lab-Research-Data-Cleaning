from numpy import genfromtxt
import csv
import pandas as pd
import random
import math
import statistics
import numpy as np

# Part I. Load the csv files into data frames
file_name0 = 'omdb_poster20_repair.csv'
df_0 = pd.read_csv(file_name0)

file_name1 = 'omdb_rating5_repair.csv'
df_1 = pd.read_csv(file_name1)

file_name2 = 'omdb_rating10_repair.csv'
df_2 = pd.read_csv(file_name2)

file_name3 = 'omdb_rating20_repair.csv'
df_3 = pd.read_csv(file_name3)

file_name4 = 'omdb_movie5_repair.csv'
df_4 = pd.read_csv(file_name4)

file_name5 = 'omdb_movie10_repair.csv'
df_5 = pd.read_csv(file_name5)

file_name6 = 'omdb_movie20_repair.csv'
df_6 = pd.read_csv(file_name6)

file_name7 = 'omdb_poster5_repair.csv'
df_7 = pd.read_csv(file_name7)

file_name8 = 'omdb_poster10_repair.csv'
df_8 = pd.read_csv(file_name8)


# Part II. Randomly Sample DB
# Assumption: Normal distribution (Gaussian) of the DB indexes
DB_Index = [0, 1, 2, 3, 4, 5, 6, 7, 8]
mu = statistics.mean(DB_Index) # Mean
sigma = statistics.pstdev(DB_Index) # Standard Deviation

k = int(input ("Enter the number of DB you'd like to sample: "))
sample = np.random.normal(mu, sigma, k).round(0)

print("The indexes of sampled DB : ", sample)

# Part III. Retrieve the sampled databases and save them in a separate folder
compression_opts = dict(method='zip',
                        archive_name='out.csv')
df_"int(sample[0])".to_csv('out.zip', index=False,
          compression=compression_opts)
