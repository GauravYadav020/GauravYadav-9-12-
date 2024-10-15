# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

data = pd.read_csv('Titanic Dataset.csv')

plt.boxplot(data['Age'])
plt.title('Age distribution')
plt.show()

plt.boxplot(data['Pclass'])
plt.title('Passenger Class distribution')
plt.show()
