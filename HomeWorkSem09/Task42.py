# Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

file_path = 'C:/Users/User/Desktop/Cristin_GB/Projects_Python/HomeWorkSem09/california_housing_train.csv'
df = pd.read_csv(file_path, sep=',')

print(df[df['population'] == df['population'].min()].households.max())