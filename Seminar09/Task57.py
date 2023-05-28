# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

import pandas as pd

file_path = 'C:/Users/User/Desktop/Cristin_GB/Projects_Python/Seminar09/california_housing_test.csv'
df = pd.read_csv(file_path, sep=',')

print(df.shape)

print(df.dtypes)

# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000

print(df.isnull().sum())

print(df[
    df['median_income'] < 2
   ].median_house_value)

print(df.iloc[:, :2])

print(df[
    (df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)
])

# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value

print(max(df['median_house_value']))

print(min(df['median_house_value']))

print(max(df[df['median_income'] == 3.1250].median_house_value))

print(df[df['median_house_value'] == df['median_house_value'].min()]
      .population.max())