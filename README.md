# **ECE2112 - Programming Assignment 3**
# **Experiment 3: Python Data Analysis (Pandas)**

## Getting Started
In this repository, you will find my codes for Experiment 3 containing two problems:
1. Problem 1 (loading a dataframe)
2. Problem 2 (performing operations on a dataframe)
<br>
The following tools were used in the completion of this experiment: <br>
- Anaconda Navigator 2.6.0<br>
- Jupyter Notebook 7.0.8

## File Inclusions
1. **Dayao_Pandas-P1.py** - Problem 1 code
2. **Dayao_Pandas-P2.py** - Problem 2 code
3. **PA3 - Dayao.ipynb** - Jupyter Notebook containing Problem 1 and 2
4. **cars.csv** - Dataframe

## Problem 1
This problem involves loading a dataset provided in .csv format into a Pandas dataframe, named ***cars***, using the ***pd.read_csv('cars.csv')*** operation. Then, the first five and last five rows of the dataframe were displayed using the operation ***cars.head()*** and ***cars.tail()***.

## Problem 2
In this problem, advanced data manipulation techniques such as subsetting, slicing, and indexing were applied to extract specific information from the ***cars*** dataframe created in Problem 1.
<br>

a. The first five rows with odd-numbered columns were identified using the operation ***cars.iloc[1::2].head()***, wherein ***iloc*** is an operation used to find location using indexes and ***[1::2]*** is an instruction to start at index 1 and select every second row.
<br>

b. Using ***cars.loc [cars ['Model'] == 'Mazda RX4']***, I obtained the row containing the model of Mazda RX4. ***loc*** is an operation used to identify the location of a column by its name. Then, ***== 'Mazda RX4'*** was added to identify the location of the row that contains the ***'Mazda RX4'*** data element in the column ***'Model'***.
<br>

c. Applying the same ***loc*** operation used in the previous item, I used ***cars.loc [(cars ['Model'] == 'Camaro Z28'), ['Model', 'cyl']]***. For this case, I added another parameter to my operation, ***'cyl'***, to display the data located in such column.
<br>

d. Employing the ***loc*** operation again, I used ***cars.loc [cars ['Model'].isin(['Camaro Z28', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']]*** to identify the number of cylinders and the type of gear that each car model has. The ***isin*** operation, which stands for "is in", was used to check whether values in a particular column are present within the specified dataframe.

## Authors
Sophia Nicole C. Dayao
<br>
2ECE-C
