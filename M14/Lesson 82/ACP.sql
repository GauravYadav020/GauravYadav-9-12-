import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive
drive.mount('/content/drive/') 
df=pd.read_csv("/content/drive/MyDrive/tips.csv")
df.head(10)
sns.distplot(df["size"])
sns.distplot(df["tip"])
sns.distplot(df["total_bill"])
#Plot Histogram of "total_bill" with kde (kernal density estimator) parameters
sns.distplot(df["total_bill"], kde=False,)
sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", style="time")
sns.pairplot(df, hue ='sex')