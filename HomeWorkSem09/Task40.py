# Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 
# (population)

import pandas as pd

file_path = 'C:/Users/User/Desktop/Cristin_GB/Projects_Python/HomeWorkSem09/california_housing_train.csv'
df = pd.read_csv(file_path, sep=',')

print(df[
    (df['population'] <= 500) & (df['population'] >= 0)
].median_house_value.mean())