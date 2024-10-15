# -*- coding: utf-8 -*-
"""Statistics for Categorical Variables and Data Transformation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oZmd1A92ZtxUk5emQiIqxv9z97zT--hq
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('bestsellers with categories.csv')

data.head()

data.info()

data.isnull().any()

print("Frequency of Categories of Genre :")
data['Genre'].value_counts()

categories = ['Fiction','Non-Fiction']
data['genre_num'] = pd.Categorical(data['Genre'], categories, ordered=True)
median_value = np.median(data['genre_num'].cat.codes)
median_cat = categories[int(median_value)]
print("Median Value of Genre is :", median_cat)

sns.countplot(data['Genre'], palette='winter')

data.groupby('Genre').size().plot(kind='pie', autopct='%.2f')

labels = ['User Rating','Reviews','Price','Year']
for l in labels:
  plt.boxplot(data[l])
  plt.show()

num_data = data.drop(['Name','Author','Genre','genre_num'], axis=1)
num_data.shape

num_data.head()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_num_data = scaler.fit_transform(num_data)
