import os
import tarfile
import urllib.request
import pandas as pd

df = pd.DataFrame(
{"a" : [4, 5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])
df = pd.DataFrame(
[[4, 7, 10],
[5, 8, 11],
[6, 9, 12]],
index=[1, 2, 3],
columns=['a', 'b', 'c'])

# columns are the dictionary keys in the first method(better for column-oriented data), second method uses lists of lists
# pandas is column oriented so you can access columns with square brackets or dot notation, but for rows use iloc or loc

df[df.Length > 7]
# This will return rows of the data frame where the Length column is greater than 7
df.drop_duplicates() 
# removes same rows that have the exact same value as another row, so only one row remains
df.sample(frac=0.5)
# returns 50% of the original rows randomly 
df.sample(n=10)
# returns 10 random rows
df.nlargest(n, 'value')
# returns 10 largest rows from largest to smallest
df.nsmallest(n, 'value')
# returns 10 smallest rows from smallest to largest
df.head(n)
# returns first n rows of data frame, defaults to 5 if not set
df.tail(n)
# returns last n rows of data frame, defaults to 5 if n not set

df[['width', 'length', 'species']]
# only shows the specified columns of the data frame
df['width']
# selects a column and shows it but as a series (The name and type will be at the bottom)
df.width
# same as above but has stricter rules on following valid Python identifiers
df.filter(regex='regex')
# regex='Length$'will filter only columns that end with Length
df.query('Length > 7')
# equivalent to df[df.Length > 7]
df.query('Length > 7 and Width < 8')
# combines multiple conditions and returns rows that fulfill those conditions
df.query('Name.str.startswith("ab")',engine="python")
# returns rows where column Name starts with string ab
df.column.isin(values) # Ex values = ["Red", Green] can customize to particular -> df['Color'].isin(['Red', 'Green'])
# values is a list, this returns all rows that have Red or Green in any columns
pd.isnull(obj)
# returns same size data frame but with True replacing null values and False elsewhere
pd.notnull(obj)
# returns same size data frame but with True replacing non null values and False elsewhere
# &,|,~,^, Logical operators AND, OR, NOT, XOR
df.any() # to specify to check row use axis = 1
# returns column or row with True value if there are any True or non zero values
df.all()
# returns column or row with True value if all are True or non zero values
'\.', 'Length$', '^Sepal',
'^x[1-5]$', '^(?!Species$).*' # Matches any column with a period, matches any column name with Length---, matches any column with --Sepal,
# matches any column starting with x followed by digit from 1-5, matches any column name that is not exactly Species

df.iloc[10:20] # selects rows 10 -19
df.iloc[:, [1, 2, 5]] # selects all rows and only columns 1, 2, and 5
df.loc[:, 'x2':'x4'] # selects all rows and columns starting from x2 all the way to x4 inclusive
df.loc[df['a'] > 10, ['a', 'c']] # selects rows where column a is greater than 10 and selects columns a and c

df.iat[1, 2] # selects row 1 and column 2
df.at[4, 'A'] # selects row with label 4 and column A
df.sort_values('mpg') # returns data Frame sorted by values of column mpg in ascending order
df.sort_values('mpg',ascending=False) # returns data Frame sorted by values of column mpg in descending order
df.rename(columns={'y': 'year'}) # renames columns from y to year
df.sort_index() # returns data Frame copy with order based on index labels
df.reset_index() # adds the old index as a column and adds default new index from 0 to n
df.drop(columns=['Length', 'Height']) # returns data frame without columns length and height


df['w'].value_counts() # returns a series with unique values from column w and their frequency
len(df) # returns number of rows in df
df.shape # returns dimensionality of data frame -> (3, 2) 3 rows 2 cols
df['w'].nunique() # number of unique values in dataframe
df.describe() # shows columns with only numerical values and gives details such as count, mean, std, min and so on (include parameter will allow for non-integers)

sum() # sum of values in column, for row use axis = 1 returns Series with sum of each column/row
count() # returns series with count of each non-null value of each column/row, depending on axis
median() # same as above except median
apply(function) # applies function to each element or column/row depending on axis
min() # same as sum but with min
max() # same as sum but with max
mean() # same as sum but with mean
var() # same as sum but with variance
std() # same as sum but with std deviation
df.dropna() # drop rows with axis = 0 or cols with axis = 1
df.fillna(value) # fill mssing with certain value
