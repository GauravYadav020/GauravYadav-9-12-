# -*- coding: utf-8 -*-
"""Lesson 4 - Activity 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e6i_OD4yrEFEiHkpKSPJTRYYdEbnQ4Yx

####**Import Libraries**
"""

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

"""####**Check Null Values**"""

data.dtypes

"""#### **Nominal and Ordinal Categorical Features -**


"""

# Nominal Categorical Variables
nominal_cat = ['Name','Ticket','Cabin']

# Ordinal Categorical Variables
ordinal_cat = ['Embarked','Gender']

"""#### **Median value of feature Gender and Embarked**"""

data['Gender'].value_counts()

gender_categories = ['Female','Male']

data['Gender'] = pd.Categorical(data['Gender'], gender_categories, ordered=True)

median_index = np.median(data['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]
print(median_gender)

data['Embarked'].value_counts()

embarked_categories = ['S','C','Q']

data['Embarked'] = pd.Categorical(data['Embarked'], embarked_categories, ordered=True)

median_index = np.median(data['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index)]
print(median_embarked)

