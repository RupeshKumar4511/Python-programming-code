# Program 6). Consider the following data frame containing a family name, gender of the family member and her/his monthly
#income in each record.
#Write a program in Python using Pandas to perform the following:
import pandas as pd
import numpy as np

import seaborn as sn
data ={'Name':['shah','vats','vats','kumar','vats','kumar','shah','shah','kumar','vats'],
       'gender':["male",'male','female','female','female','male','male','female','female','male'],
'MonthlyIncome':[114000,65000,43150,69500,155000,103000,55000,112400,81030,71900]
}
df  = pd.DataFrame(data)
#print(df)

#(A) Calculate and display familywise gross monthly income.

print("\n Calculate and display familywise gross monthly income.  ")
print(df.groupby(by =['Name'])['MonthlyIncome'].sum())

#(b)Calculate and display the member with the highest monthly income.
print("\n Calculate and display the member with the highest monthly income. \n ")
print(df.loc[df['MonthlyIncome'] == max(df['MonthlyIncome'])])

#(c) Calculate and display monthly income of all members with income greater than Rs. 60000.00.
print("\n Calculate and display monthly income of all members with income greater than Rs. 60000.00. \n ")
result = df.loc[df['MonthlyIncome']>60000]
print(result['MonthlyIncome'])

#(d)Calculate and display the average monthly income of the female members
print("\n Calculate and display the average monthly income of the female members  \n ")
result1=df.loc[df['gender'] == 'female']
print(result1 ['MonthlyIncome'].mean())
