from sklearn.preprocessing import KBinsDiscretizer
import pandas as pd
import numpy as np

csv = "~/datasets/iris.data"

df = pd.read_csv(csv,sep=",")
#print(df.values[:,0:-1])
columns = df.columns

#Obesity
#target_columns = ["Age","Weight","Height"]
#target_bins =[10,10,10]

#iris
target_columns = ["sepal length in cm","sepal width in cm","petal length in cm","petal width in cm"]
target_bins =[10,10,10,10]
target_index =[]
for index,column in enumerate(columns):
	if column in target_columns:
		target_index.append(index)

target = df.values[:,target_index]
#to_discretize = [target[:,i] for i in range(len(target[0,:]))]
#print(to_discretize)
# strategies: uniform,quantile,kmeans
est = KBinsDiscretizer(n_bins=np.array(target_bins),encode="ordinal",strategy="quantile")

est.fit(target)
Xt = est.transform(target)
print(Xt)


for no,ind in enumerate(target_index):
	df.iloc[:,ind] = Xt[:,no]

df.to_csv(f"{csv}.disc",index=False)
print(df)