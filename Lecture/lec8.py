'''
                       HOMEWORK

Q.1) What is Prompt Engineering and Different types of Prompt Engineering?
Ans. Prompt Engineering is the process where guide the AI by giving best prompts to get best solution for the desired problem.

     There are 8 Types of Prompting:

  1) Zero-Shot Prompting ---> In this type you give direct prompt to the AI.
             Ex --> Translate 'Hello' in French

  2) One-Shot Prompting ---> In this type you give the prompt with an example to AI.
             Ex --> Given a job description, "Now write a similar one for a Data Analyst position.

  3) Few-Shot Prompting ---> In this type you give few examples along with your prompt for the AI to get better results.
             Ex --> Foundation Models such as GPT-3 are used for natural language processing, while models like DALL-E are used for image 		    generation. How are Foundation Models used in the field of robotics?

  4) Chain-of-Thought Prompting ---> In this type you ask the AI to give Step by step guide for your solution.
             Ex --> Describe the process of developing a Foundation Model in AI, from data collection to model training.

  5) Iterative Prompting ---> In this type you refine your prompt according the output you get from the AI to get the desired solution.
 	     Ex --> Tell me about the latest developments in Foundation Models in AI.
                    Refined Prompt: “Can you provide more details about these improvements in multi-modal learning within Foundation 			    Models?”

  6) Negetive Prompting ---> In this Type, you tell the AI what not to do. For instance, you might specify that you don’t want a certain 			     type of content in the response.
 	     Ex --> Explain the concept of Foundation Models in AI without mentioning natural language processing or NLP.

  7) Hybrid Prompting ---> Combining different methods, like few-shot with chain-of-thought, to get more precise or creative outputs.
             Ex --> Like GPT-3, which is a versatile model used in various language tasks, explain how Foundation Models are applied in 		    other domains of AI, such as computer vision.
  
  8) Prompt Chaining ---> Breaking down a complex task into smaller prompts and then chaining the outputs together to form a final 				  response.
             Ex --> List some examples of Foundation Models in AI.
                    Second Prompt: “Choose one of these models and explain its foundational role in AI development.”

'''

import numpy as np
import pandas as pd
'''
df = pd.read_csv("D:\\summer-regex\\pyprogs\\Lecture\\Datasets\\mall.csv")
df.head()

df = df.drop(columns = ['CustomerID','Genre'])
df.head()

x = df.iloc[:,[0,1]].values

from sklearn.cluster import KMeans

import matplotlib.pyplot as plt

a = []

for i in range(1,11):
 b = KMeans(n_clusters = i,init = 'k-means++',random_state = 42)
 b.fit(x)
 a.append(b.inertia_)

plt.plot(range(1,11),a)

plt.title('The Elbow Method Graph')
plt.xlabel('Number of Clusters(k)')
plt.ylabel('wcss_list')
plt.show()


#From the above plot, we can see the elbow point is at 4. So the number of clusters here will be 4.

b = KMeans(n_clusters = 4,init = 'k-means++',random_state = 42)
y_predict = b.fit_predict(x)

#visualizing the clusters
plt.scatter(x[y_predict == 0,0], x[y_predict == 0,1], s = 100, c = 'blue', label = 'Cluster 1') #for first cluster
plt.scatter(x[y_predict == 1,0], x[y_predict == 1,1], s = 100, c = 'green', label = 'Cluster 2') #for second cluster
plt.scatter(x[y_predict == 2,0], x[y_predict == 2,1], s = 100, c = 'red', label = 'Cluster 3') #for third cluster
plt.scatter(x[y_predict == 3,0], x[y_predict == 3,1], s = 100, c = 'cyan', label = 'Cluster 4') #for fourth cluster

plt.scatter(b.cluster_centers_[:,0], b.cluster_centers_[:,1], s = 300, c = 'yellow', label = 'Centroid')

plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()



from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("D:\\summer-regex\\pyprogs\\Lecture\\Datasets\\Social_Network_Ads.csv")
df.head()

df = df.drop(columns = ['User ID', 'Gender'])

x = df.drop(columns = ['Purchased'], axis = 1)
y = df['Purchased']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)

pipe = Pipeline([
         ('scaler', StandardScaler()),
         ('pca', PCA(n_components = 2)),
         ('classifier', RandomForestClassifier(n_estimators = 100, random_state = 42))
])

pipe

Pipeline(steps = [('scaler', StandardScaler()),('pca',PCA(n_components = 2)),('classifier',RandomForestClassifier(random_state = 42))])

pipe.fit(x_train, y_train)

Pipeline(steps = [('scaler', StandardScaler()),('pca',PCA(n_components = 2)),('classifier',RandomForestClassifier(random_state = 42))])

y_pred = pipe.predict(x_test)

acc = accuracy_score(y_test, y_pred)
print(acc)

'''


