#Program(7)Using Titanic dataset, to do the following:
import pandas as pd
df = pd.read_csv('/content/Titanic.csv')
#print(df)
#(a)Find total number of passengers with age less than 30

data = df.loc[df['Age']<30]


print("\n Find total number of passengers with age less than 30 \n")
print(len(data))


#(b)Find total fare paid by passengers of first class
print("\n Find total fare paid by passengers of first class \n")
Passanger = df.loc[df['Pclass']==1]

print(Passanger['Fare'].sum())

#(c) Compare number of survivors of each passenger
print("\n Compare number of survivors of each passenger class \n")
Passenger1 = df.loc[df['Pclass']==1 ]
Survivors = df.loc[df['Survived']==1 ]
Passenger2 = df.loc[df['Pclass']==2]
Passenger3 = df.loc[df['Pclass']==3]
print("Passenger of 1st class, Total: ", len(Passenger1), ", Survived: ", len(Passenger1[Passenger1["Survived"] == 1]))
print("Passenger of 2nd class, Total: ", len(Passenger2), ", Survived: ", len(Passenger2[Passenger2["Survived"] == 1]))
print("Passenger of 3rd class, Total: ", len(Passenger3), ", Survived: ", len(Passenger3[Passenger3["Survived"] == 1]))



#(d)Compute descriptive statistics for any numeric attribute genderwise
print("\n Compute descriptive statistics for any numeric attribute genderwise(male) \n")


df2 = df.loc[df['Sex']=='male']
df3 = df.loc[df['Sex']== 'female']
print(df2.describe())
print("\n Compute descriptive statistics for any numeric attribute genderwise(female) \n")
print(df3.describe())