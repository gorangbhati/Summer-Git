import numpy as np
import pandas as pd

'''
# Encoding ----> Transform our Categorical Data into Numerical Data.

#(1). Label Encoding ---> It will encode the data by single-single column.

df = pd.read_csv("D:\\summer-regex\\pyprogs\\Lecture\\Datasets\\covid_toy.csv")
print(df.head(3))

#df.isnull.sum()

from sklearn.impute import SimpleImputer

si = SimpleImputer()

df['fever'] = si.fit_transform(df[['fever']])

print(df.head(2))

from sklearn.preprocessing import LabelEncoder

lb  = LabelEncoder()

df['gender'] = lb.fit_transform(df['gender'])
df['cough'] = lb.fit_transform(df['cough'])
df['city'] = lb.fit_transform(df['city'])
df['has_covid'] = lb.fit_transform(df['has_covid'])

print(df.head(3))

x = df.drop(columns = ['has_covid'])    #Input Column
y = df['has_covid']    #Target Column

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)

np.round(x_train.describe(),2)

# Now we will change our data into Normal Distribution

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

x_train_sc = sc.fit_transform(x_train)
x_train_new = pd.DataFrame(x_train_sc, columns=x_train.columns)

np.round(x_train_new.describe(),2)



#(2). Ordinal Encoder ---> It is used to enocode multiple columns.

df = pd.read_csv("D:\\summer-regex\\pyprogs\\Lecture\\Datasets\\covid_toy.csv")
print(df.head(3))

df = df.dropna()

df  = df.drop(columns = ['age', 'fever'])

from sklearn.preprocessing import OrdinalEncoder

oe = OrdinalEncoder(categories = [['Female', 'Male'],
				  ['Mild', 'Strong'],
				  ['Kolkata', 'Banglore', 'Delhi', 'Mumbai'],
                                  ['No', 'Yes']])

print(oe.fit_transform(df))



#(3). get_dummies
#  => df['cough'] ---> sun-categories = 'Mild', 'Strong' ---> when we apply get_dummies it will create
#								 a new column of sub-category.
#  => df['cough'], df['cough_Mild'], df['cough_Strong']

df = pd.read_csv("D:\\summer-regex\\pyprogs\\Lecture\\Datasets\\covid_toy.csv")
print(df.head(3))

df = df.dropna()

df = pd.get_dummies(df,columns = ['gender', 'cough', 'city', 'has_covid'])

print(df.astype(int))

'''

#(4). OneHotEncoder

df = pd.read_csv("D:\\summer-regex\\pyprogs\\Lecture\\Datasets\\covid_toy.csv")
print(df.head(3))

df = df.dropna()

df = df.drop(columns = ['age', 'fever'])

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(drop = 'first', sparse_output = False,dtype = np.int32)

print(ohe.fit_transform(df))