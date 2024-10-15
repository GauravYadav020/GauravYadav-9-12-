# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
uploaded = files.upload()
# Import dataset
age_q3 = np.quantile(data['Age'], 0.75)

print("Age Quartiles -")
print("Q1 -", age_q1)
print("Q2 -", age_q2)
print("Q3 -", age_q3)
plt.hist(data['Age'])
plt.ylabel("Count of Passengers")
plt.xlabel("Age")

fare_q1 = np.quantile(data['Fare'], 0.25)
fare_q2 = np.quantile(data['Fare'], 0.50)
fare_q3 = np.quantile(data['Fare'], 0.75)

print("Fare Quartiles -")
print("Q1 -", fare_q1)
print("Q2 -", fare_q2)
print("Q3 -", fare_q3)

bins =np.arange(0,250,20)
plt.hist(data['Fare'], bins=np.arange(1,250, 20))
plt.ylabel("Count of Passengers")
plt.xlabel("Fare")
plt.xticks(bins)