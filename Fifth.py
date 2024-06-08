#Program5)Using Iris data, plot the following with proper legend and axis labels: (Download IRIS data from:
#https://archive.ics.uci.edu/ml/datasets/iris or import it from sklearn datasets)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv('/content/Iris1.csv')
# print(df)

#a)Plot bar chart to show the frequency of each class label in the data.
print("\n (a) \n")
df.plot.bar()
plt.show()

#b)Draw a scatter plot for Petal width vs sepal width and fit a regression line
print("\n (b) \n ")
df.plot.scatter(x='PetalWidthCm',y='SepalWidthCm' )
plt.show()

#c)Plot density distribution for feature petal length.
print("\n (c) \n")
df2 = sn.load_dataset('iris')
sn.displot(a=df2.petal_length, color='green',
             hist_kws={"edgecolor": 'black'})
plt.title('Density plot ')
plt.show()



#(d)Use a pair plot to show pairwise bivariate distribution in the Iris Dataset

print("\n (d) \n")
df4 = sn.load_dataset('iris')
sn.pairplot(df4, hue ='petal_length')
plt.show()


#(f)Compute mean, mode, median, standard deviation, confidence interval and standard error for each feature

print("\n (f) \n")
print(df.describe())
print(df[df.columns[1:-2]].mode(axis =1))


#e ) Draw heatmap for the four numeric attributes
print("\n (e) \n")

sn.heatmap(data = df[df.columns[1:5]])
plt.show()
#g) Compute correlation coefficients between each pair of features

print("\n (g) \n")
print(df[df.columns[1:5]].corr())
