#Program2) Do the following using PANDAS Series:
#(A)Create a series with 5 elements. Display the series sorted on index and also sorted on values seperately

import numpy as np
import pandas as pd
series1 = pd.Series([1,3,23,44,5,44,7,5,np.nan])
print("sort index ",series1.sort_index())
print("sort values" ,series1.sort_values())

# (b)  Create a series with N elements with some duplicate values. Find the minimum and maximum ranks
# assigned to the values using ‘first’ and ‘max’ methods


print("rank with first ",series1.rank(method="first"))
print("rank with max ",series1.rank(method ="max"))

#(c) Display the index value of the minimum and maximum element of a Series

print("max index ",series1.idxmax())
print("min index " ,series1.idxmin())