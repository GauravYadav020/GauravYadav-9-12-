from google.colab import files
uploaded = files.upload()

import seaborn as sns
data = pd.read_csv('penguins_lter.csv')
data.head()
data.isnull().any() 
data.isnull().sum()
sns.heatmap(data.isnull())


#### **Handling Numerical Null Values**
data['Culmen Depth (mm)'] = data.fillna(data['Culmen Depth (mm)'].mean())
data['Culmen Length (mm)'] = data.fillna(data['Culmen Length (mm)'].mean())
data['Flipper Length (mm)'] = data.fillna(data['Flipper Length (mm)'].mean())
data['Body Mass (g)'] = data.fillna(data['Body Mass (g)'].mean()) 
data['Delta 13 C (o/oo)'] = data.fillna(data['Delta 13 C (o/oo)'].mean())
data['Delta 13 C (o/oo)'] = data.fillna(data['Delta 13 C (o/oo)'].mean())
data.isnull().sum()