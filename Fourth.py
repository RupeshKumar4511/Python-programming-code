#Program (4) Consider two excel files having attendance of two workshos. Each file has three fields ‘Name’, ‘Date, duration
#(in minutes) where names are unique within a file. Note that duration may take one of three values (30, 40, 50)
#only. Import the data into two data frames and do the following:

import pandas as pd
df = pd.read_excel('/content/first.xlsx')
df1 = pd.read_excel('/content/Second.xlsx')
#print(df)

#(a)Perform merging of the two data frames to find the names of students who had attended both workshops.


result = pd.merge(df,df1, how = 'inner' , on ='Name')     #default how = 'inner'
print("names of students who had attended both workshops",result)

#(b) Find names of all students who have attended a single workshop only.


result1 = pd.merge(df,df1 ,how ='outer')
print("names of all students who have attended a single workshop",result1['Name'].unique())

#(c)Merge two data frames row-wise and find the total number of records in the data frame.

result1 = pd.merge(df,df1 ,how ='outer')
print("total number of records in the data frame :",len(result1))


#(d)Merge two data frames row-wise and use two columns viz. names and dates as multi-row indexes.
#Generate descriptive statistics for this hierarchical data frame.

result2 = pd.merge(df,df1 ,how ='outer',on=['Name','Date'])
print("descriptive statistics",result2.describe())


