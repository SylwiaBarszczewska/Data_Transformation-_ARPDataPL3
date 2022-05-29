# import
import pandas as pd
import numpy as np

# Tworzenie Series
list_values = [1, 2, 3]
array_values = np.array([1, 2.3, 3])
s1 = pd.Series(data=list_values, index=['A', 'B', 'C'], dtype=int)
# print(s1)

# Tworzenie DataFrame
# data1 = {
#     "col1": [1, 2, 3, 4, 5, 6],
#     "col2": ['A', 'B', 'C', 'Unknown', 'D', 'E'],
#     "col3": [1.1, 2.2, 3.3, 0, 1, 2]
# }

# numpy_data = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
# df1 = pd.DataFrame(data=data1, index=['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff'])
# df2 = pd.DataFrame(data=numpy_data, index=['Aa', 'Bb', 'Cc'], columns=['col1', 'col2', 'col3'])
# print(df1)

# Wyswietlanie danych
# print(df1.shape)  # zwraca wymiar tabeli
# print(df1.columns)
# print(df1.index)

# sample_data_iloc = df1.iloc[0]
# sample_data_loc = df1.loc['Aa']
# sample_data_iloc_first3 = df1.iloc[:3, :-1]
# sample_data_loc_one_col = df1.loc['Aa', ['col1', 'col2']]
#
# first_col_series = df1['col1']
# first_col_df = df1[['col1', 'col2']]
# print(first_col_df)
# print(type(first_col_df))

# operacje matematyczne - funkcje agregacyjne
# print(f'Min value: {df1["col1"].min()}, Max value: {df1["col1"].max()}, Mean value: {df1["col1"].mean()}')
# print(df1[df1['col1'] == df1["col1"].max()])

# Dodawanie kolumn
# print('Initial shape', df1.shape)
# df1['new_col_constant'] = 1
# df1['new_col_values'] = [3, 4, 5, 6, 7, 8]
# df1['new_col_sum'] = df1['col1'] + 1
# print('Added 3 columns', df1.shape)

# Usuwanie kolumn
# del df1['new_col_sum']  # usuwanie kolumn
# df1 = df1.drop(['Aa', 'Bb'], axis=0)  # usuwanie wierszy
# # df1 = df1.drop(['col1'], axis=1)  # usuwanie kolumn
# df1 = df1.drop(columns=['col1'])  # usuwanie kolumn
# df1 = df1.drop(index=['Cc'])  # usuwanie index
# print('Removed column', df1.shape)
#
# print(df1)

# Filtrowanie danych
# print(df1)
# sample_data = df1[(df1['col1'] <= 4) & (df1['col2'] != 'Unknown')]
# less_than_4 = df1['col1'] < 4
# print(df1[less_than_4])
# print(sample_data)
# print(df1)

# df1['new index'] = range(len(df1))
# print(df1.index)
# df1 = df1.reset_index()
#
# sample_data = df1[df1['col1'] <= 4]
# filtered_column = df1['col1'][df1['col1'] <= 4]
# print(filtered_column)

# Operacje na Series i DataFrames
# df_1 = pd.DataFrame(
#     {
#         "A": [1, 2, 3],
#         "B": [1.1, 2.2, 3.3]
#     }
# )
# df_2 = pd.DataFrame(
#     {
#         "A": [4, 5, 6],
#         "B": [4.1, 5.2, 6.3]
#     }
# )
# print(df_1 + df_2)
#
# df_1 = pd.DataFrame(
#     {
#         "A": [1, 2, 3, 4],
#         "B": [1.1, 2.2, 3.3, 4.4]
#     }
# )
# df_2 = pd.DataFrame(
#     {
#         "A": [4, 5, 6],
#         "B": [4.1, 5.2, 6.3]
#     }
# )
# print(df_1 + df_2)
#
# df_1 = pd.DataFrame(
#     {
#         "A": [1, 2, 3, 4],
#         "B": [1.1, 2.2, 3.3, 4.4]
#     }
# )
# df_2 = pd.DataFrame(
#     {
#         "A": [4, 5, 6],
#         "C": [4.1, 5.2, 6.3]
#     }
# )
# df_1['C'] = 0
# df_2['B'] = 0
#
# print(df_1)
# print(df_1 - df_2)

# print(df_1 + 5)  # skalarna wartosc

# Łączenie DataFrames

# df1 = pd.DataFrame({
#     "Id": ['X01', 'X02', 'X03', 'X04'],
#     "Name": ["Ania", "Ola", "Adam", "Tomek"],
#     "Score": [30, 49, 13, 41]
# })
#
# df2 = pd.DataFrame(
#     {
#         "id_student": ['X01', 'X02', 'X06'],
#         "City": ['Wroclaw', 'Gdansk', "Katowice"],
#     }
# )
# merged_data = df1.merge(right=df2, how='left', left_on="Id", right_on="id_student")
# merged_data_2 = df2.merge(right=df1, how='right', left_on="id_student", right_on="Id")
# print(merged_data)
# print(merged_data_2)

df1 = pd.DataFrame({
    "Id": ['X01', 'X02', 'X03', 'X04'],
    "Name": ["Ania", "Ola", "Adam", "Tomek"],
    "Score": [30, 49, 13, 41]
})

df2 = pd.DataFrame({
    "Id": ['X05', 'X06', 'X07', 'X08'],
    "Name": ["Ala", "Jagoda", "Adrian", "Damian"],
    "Score": [40, 59, 13, 41]
})

# append_dfs = df1.append(df2)
# append_dfs.reset_index(inplace=True)  # nie tworzy nowego obiektu tylko nadpisuje istniejacy
# print(append_dfs)

concat_data_rows = pd.concat([df1, df2], axis=0)
concat_data_columns = pd.concat([df1, df2], axis=1)
print(concat_data_columns)

# Grupowanie

# Sortowanie

# Brakujące wartości

# funckja apply
