import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\summer-regex\\pyprogs\\Lecture\\Datasets\\titanic.csv")
'''
print(df)

print(df.tail())

print(df.head())

print(df.sample(3))

print(df.shape)

print(df.columns)

print(df.loc[2:5, ['Survived','Pclass']])

print(df.iloc[2:5,[0,1,2]])

print(df.isnull().sum())

p = df.dropna()
print(p.isnull().sum())

print(df.drop(columns = ['Cabin']))

df['Fare'] = df['Fare'].fillna(5)
df['Age'] = df['Age'].fillna(10)
print(df.head())

df['Fare'] = df['Fare'].astype(int)
print(df['Fare'].dtype)

df['Survived'].value_counts()

df = df.rename(columns = {'Age' : 'Updated_Age'})

sns.countplot(x = df['Survived'])

df['Survived'].value_counts().plot(kind = 'bar')

df['Survived'].value_counts().plot(kind = 'pie', autopct = '%.2f')
'''
plt.hist(x = df['Age'])
plt.show()