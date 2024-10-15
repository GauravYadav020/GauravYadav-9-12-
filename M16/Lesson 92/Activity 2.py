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

bins_time = np.arange(80, 230, 10)
plt.hist(data['Runtime'], edgecolor="black", bins=bins_time, color='g')
plt.ylabel("Count of movies")
plt.xlabel("Runtime")

bins_rating = np.arange(8, 10, 0.20)
plt.hist(data['IMDB_Rating'], edgecolor="black", bins=bins_rating, color='g')
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.xticks(bins_rating)