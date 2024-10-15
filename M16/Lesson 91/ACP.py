from google.colab import files
uploaded = files.upload()
import pandas as pd
import numpy as np
import statistics as stats
data = pd.read_csv('bestsellers with categories.csv')
data.head()
data.info()
mean_rating = np.mean(data['User Rating'])
mean_rating
median_rating = np.median(data['User Rating'])
median_rating
mode_rating = stats.mode(data['User Rating'])
mode_rating
mean_reviews = np.mean(data['Reviews'])
mean_reviews
median_reviews = np.median(data['Reviews'])
median_reviews
mode_reviews = stats.mode(data['Reviews'])
mode_reviews
mean_price = np.mean(data['Price'])
mean_price
mode_price = stats.mode(data['Price'])
mode_price