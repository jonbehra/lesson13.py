import numpy as np
import pandas as pd

print(np.__version__)

array_2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array_2d)

element = array_2d[0,3]
print(element)

dimension = array_2d.ndim
print(dimension)

size = array_2d.size
print(size)

#shuma e komplet listes
total_sum = np.sum(array_2d)
print(total_sum)

sum_columns = np.sum(array_2d, axis = 0)
print(sum_columns)

sum_rows = np.sum(array_2d, axis = 1)
print(sum_rows)


#PANDAS

products = ['apples','bananas','orange','grapes']
sales = [150,200,180,90]

sales_series = pd.Series(sales,index=products)
print(sales_series)

print(sales_series['grapes'])

total_sales = sales_series.sum()
print(total_sales)

data = {
    'Name' : ['aliance','bob','leon'],
    'Age' : [13,12,17],
    'City' : ['New York','London','Prishtina'],
}

# df= pd.DataFrame(data)
# print(df)

# df =  pd.read_csv('cs.csv')

# df.to_csv('dion.csv', index = False)

best_selling_product = sales_series.idxmax()
print(f"Best selling product:{best_selling_product}")