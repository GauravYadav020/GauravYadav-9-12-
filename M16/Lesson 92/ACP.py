# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
uploaded = files.upload()
# Import dataset
data = pd.read_csv('IMDB Dataset.csv')
data.head(5)
plt.hist(data['Runtime'])
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.hist(data['User Rating'])
plt.xlabel('User Rating')
plt.ylabel('Number of Books')
plt.show()

bins_rating = np.arange(3,5,0.1)
plt.hist(data['User Rating'], edgecolor='black', color='teal', bins=bins_rating)
plt.xlabel('User Rating')
plt.ylabel('Number of Books')
plt.show()
bins_price = np.arange(0,110,5)
plt.hist(data['Price'], edgecolor='black', color='darkred', bins=bins_price)
plt.xlabel('Price')
plt.ylabel('Number of Books')
plt.show()