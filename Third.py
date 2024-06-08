#Program(3) Create a data frame having at least 3 columns and 50 rows to store numeric data generated using a random
#function. Replace 10% of the values by null values whose index positions are generated using random function.
# Do the following


import pandas as pd
import numpy as np
import random
df = pd.DataFrame(np.random.randint(50,size=(50,3)),columns= ['first','second','third'])
#print(df)
indx = random.sample(range(0,50),15)


# a)  Identify and count missing values in a data frame.


for i in range(len(indx)):
    c = random.sample(range(0,3),1)
    df.iloc[indx[i],c]= np.nan

nulldf= df.isnull()
print("check the nan value \n")
print(nulldf)


count=0
for i in range(0,3):
  for j in range(0,50):
      if nulldf.iloc[j,i] == True:
         count += 1
print("No of missing values are " ,count)
print(nulldf[:].sum().sum())



#(b) Drop the column having more than 5 null values.

ls = []
nullcount =0
for i in range(0,3):
  for j in range(0,50):

      if nulldf.iloc[j,i] == True:
         nullcount += 1
  ls.append(nullcount)
  nullcount =0
print(ls)

ls1=[]
for k in range(len(ls)):
    if ls[k] > 5 :
      ls1.append(k)
for l in ls1:
    df.drop(df.columns[l],axis = 1,inplace = True)
print (df)



# 2nd way of doing this;


print(df.dropna(thresh = 45,axis =1))




# #(c) Identify the row label having maximum of the sum of all values in a row and drop that row.


series1  = df.sum(axis = 1)
print(series1.idxmax())

print(df.drop(series1.idxmax()))

#(d) Sort the data frame on the basis of the first column.

print(df.sort_values('first',ascending= True))



# #(e)Remove all duplicates from the first column.

print(df.drop_duplicates('first'))



# #(f) Find the correlation between first and second column and covariance between second and third column.

print(df[df.columns[0:2]].corr()[ :-1])
print(df[df.columns[1:3]].cov()[ :-1])

# # #(g) Discretize the second column and create 5 bins.

df3 = pd.cut(df['second'],bins =[0,10,20,30,40],labels= ['very_low','low', 'medium','high'])
print(df3.head())