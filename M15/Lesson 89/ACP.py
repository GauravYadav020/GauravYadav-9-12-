import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
HouseDF=pd.read_csv('C:/Users/Karan/Downloads/USA_Housing.csv')
HouseDF.head()
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(x_train,y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
coeff_df=pd.DataFrame(lm.coef_,x.columns,columns=['Coefficient'])
coeff_df
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))