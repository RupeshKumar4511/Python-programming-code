#Program1)  Write programs in Python using NumPy library to do the following:

#(a) Compute the mean, standard deviation, and variance of a two dimensional random integer array along the second axis.
import numpy as np


arr = np.random.randn(2,10)
print("mean",arr.mean(axis = 1))
print("var",arr.var(axis =1))
print("standard deviation" ,arr.std(axis = 1))

#(b)Create a 2-dimensional array of size m x n integer elements, also print the shape, type and
#data type of the array and then reshape it into an n x m array, where n and m are user inputs given at the run time.


m = int(input("enter the no of rows"))
n = int(input("enter the no of columns"))

arr1=np.random.randn(m,n)
print("shape",arr1.shape)
print("type ",type(arr1))
print("dtype of array",arr1.dtype)

#(c)Test whether the elements of a given 1D array are zero, non-zero and NaN. Record the indices of these
#elements in three separate arrays.

l1 =[]
l2 =[]
l3 =[]
arr2 = np.array([12,3,np.nan,37,np.nan,0])
for i in range(len(arr2)):
  if (np.isnan(arr2[i])):
    l1.append(i)
  if(arr2[i] != 0 and not(np.isnan(arr2[i]))):
    l2.append(i)
  if (arr2[i] ==0):
     l3.append(i)
print("array of nan index ",np.array(l1))
print("array of zero no index ",np.array(l2))
print("array of non zero no index ",np.array(l3))

#(d)Create three random arrays of the same size: Array1, Array2 and Array3. Subtract Array 2 from Array3
#and store in Array4. Create another array Array5 having two times the values in Array1. Find Covariance and Correlation of Array1 with Array4 and Array5 respectively.
array1= np.random.randn(2,2)

array2= np.random.randn(2,2)
array3= np.random.randn(2,2)
array4 = array3 - array2
array5= array1 * 2

print("covariance of arr 1 with 4",np.cov(array1,array4))
print("covariance of arr 1 with 5",np.cov(array1,array5))
print("correlation  of arr 1 with 4",np.corrcoef(array1,array4))
print("correlation  of arr 1 with 5",np.corrcoef(array1,array5))


#(e)Create two random arrays of the same size 10: Array1, and Array2. Find the sum of the first half of both
#the arrays and product of the second half of both the arrays.
arr3 = np.random.randn(10)
arr4 = np.random.randn(10)

secondhalf1 = arr3[0:len(arr3)//2]
secondhalf2 = arr4[0:len(arr4)//2]
secondhalf_result  = secondhalf1  + secondhalf2
print("addition",secondhalf_result)


secondhalf1 = arr3[len(arr3)//2:len(arr3)]
secondhalf2 = arr4[0:len(arr4)//2:len(arr4)]
secondhalf_result  = secondhalf1 * secondhalf2
print("product",secondhalf_result)