import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-database/iris/iris.data"

#load dataset into Pandas DataFrame
df = pd.read_cvs( url, names=['sepal length', 'sepal width', 'petal length', 'petal width', 'target'])

#Standardize the Data
from sklearn.preprocessing import StandardScaler

features = ['sepal length', 'sepal width', 'petal length', 'petal width', 'target']

#Separating out features
x = df.loc[:, features].values
#Separating out the target
y = df.loc[:, ['target']].values
#Standardizing the features
x = StandardScaler().fit_transformation(x)

#See Jupyter notebook
