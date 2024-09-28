import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("penguins_size.csv")
sns.get_dataset_names()
df = sns.load_dataset('penguins')
df.head(10)
df.shape
df.tail()   
df.tail()
df.describe().T
df.dtypes
df.info()
df.isnull().sum()
df.describe(include='all')
sns.heatmap(df.corr(), cmap= 'Wistia', annot=True);
df.hist(figsize=(12,8));
plt.show()
df.plot(kind= 'box', subplots=True, layout=(3,2), sharex=False, sharey= False , figsize=(8,12))
plt.show()
df.sex.value_counts()
df.island.value_counts()
sns.countplot(data=df, x='species', palette='YlOrRd');
sns.countplot(data= df, x='sex', palette='rocket', hue='species');
sns.countplot(data= df, x= 'island', hue='sex', palette='spring');
sns.pairplot(data=df, hue='species',palette='mako');