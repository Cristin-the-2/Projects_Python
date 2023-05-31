import pandas as pd
import seaborn as sns

file_path = 'C:/Users/User/Desktop/Cristin_GB/Projects_Python/Seminar09/california_housing_test.csv'
df = pd.read_csv(file_path, sep=',')
# 1. Изобразите отношение households к population с помощью точечного графика
print(sns.scatterplot(data=df, x='population', y='households'))
# 2. Визуализировать longitude по отношения к median_house_value, используя
# линейный график
print(sns.relplot(data=df, x='longitude',
      y='median_house_value', kind='line',  aspect=4))
# 3. Представить гистограмму по housing_median_age
print(sns.histplot(data=df, x='housing_median_age'))
# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
print(sns.histplot(data=df, x='median_house_value', hue='housing_median_age'))
