# import
import pandas as pd
import numpy as np

# Tworzenie Series
list_values = [1, 2, 3]
array_values = np.array([1, 2.3, 3])
s1 = pd.Series(data=list_values, index=['A', 'B', 'C'], dtype=int)
# print(s1)

# Tworzenie DataFrame
data1 = {
    "col1": [1, 2, 3, 4, 5, 6],
    "col2": ['A', 'B', 'C', 'Unknown', 'D', 'E'],
    "col3": [1.1, 2.2, 3.3, 0, 1, 2]
}

# numpy_data = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
df1 = pd.DataFrame(data=data1, index=['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff'])
# df2 = pd.DataFrame(data=numpy_data, index=['Aa', 'Bb', 'Cc'], columns=['col1', 'col2', 'col3'])
print(df1)

# Wyswietlanie danych
# print(df1.shape)  # zwraca wymiar tabeli
# print(df1.columns)
# print(df1.index)

sample_data_iloc = df1.iloc[0]
sample_data_loc = df1.loc['Aa']
print(sample_data_loc)

# operacje matematyczne

# Dodawanie kolumn

# Usuwanie kolumn

# Filtrowanie danych

# Operacje na Series i DataFrames

# Łączenie DataFrames

# Grupowanie

# Sortowanie

# Brakujące wartości
