# Написать EDA для датасета про пингвинов

import pandas as pd
import seaborn as sns
penguins = sns.load_dataset("penguins")
print(penguins.head())
print(penguins.shape)
print(penguins.isnull().sum())
penguins.dropna(inplace=True)
# Использовать 2-3 точечных графика
print(sns.scatterplot(data=penguins, x='body_mass_g', y='bill_length_mm'))
print(sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm'))
# Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
print(sns.scatterplot(data=penguins, x='body_mass_g',
      y='bill_length_mm', hue='species'))
print(sns.scatterplot(data=penguins, x='body_mass_g',
      y='flipper_length_mm', hue='island'))
print(sns.scatterplot(data=penguins, x='body_mass_g',
      y='flipper_length_mm', hue='sex'))
# Использовать PairGrid с типом графика на ваш выбор
lst = ['bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g', 'sex']
g = sns.PairGrid(penguins[lst])
print(g.map_lower(sns.histplot))
print(g.map_upper(sns.scatterplot))
# Изобразить Heatmap
print(sns.heatmap(data=penguins.corr(), vmin=-1, vmax=1))
# Использовать 2-3 гистограммы
print(sns.histplot(data=penguins, x='island', hue='species'))
print(sns.histplot(data=penguins, x='species', y='island'))
# Создать новый столбец в таблице с пингвинами, который будет отвечать за
# показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)
penguins.loc[penguins['bill_length_mm'] > 42, 'height_group'] = 'high'
penguins.loc[(penguins['bill_length_mm'] <= 42) & (
    penguins['bill_length_mm'] >= 35), 'height_group'] = 'middle'
penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = 'low'
print(penguins.height_group.unique())
# Изобразить гистограмму по flipper_length_mm с оттенком height_group.
# Сделать анализ
print(sns.histplot(data=penguins, x='flipper_length_mm', hue='height_group'))
