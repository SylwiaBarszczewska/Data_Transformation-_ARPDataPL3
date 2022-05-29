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
    "col1": [1, 2, 3],
    "col2": ['A', 'B', 'C'],
    "col3": [1.1, 2.2, 3.3]
}

numpy_data = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

df = pd.DataFrame(data=data1, index=['Aa', 'Bb', 'Cc'], columns=['New_col1', 'New_col2', 'New_col3'])
print(df)


# Wyswietlanie danych

# Dodawanie kolumn

# Usuwanie kolumn

# Filtrowanie danych

# Operacje na Series i DataFrames

# Łączenie DataFrames

# Grupowanie

# Sortowanie

# Brakujące wartości
