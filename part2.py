import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# odczytywanie danych
data = pd.read_csv('Datasets/titanic.csv', sep=';')
# print(data)
# print(data.info())
# print(data.describe())  # opis dla numerycznych kolumns
categorical_data = data.select_dtypes(object)
# print(categorical_data.describe())

print(data.head(n=10))  # pierwsze 10 rekordow
print(data.tail(n=10))  # ostatnie 10 rekordow
print(data.sample(n=10))  # randomowa probka danych - 10 rekordow

# usuwanie danych

# Usuwanie nan

# standaryzacja danych

# duplikaty

# dyskretyzacja

# one hot encoding

# usuwanie szumów - outliers

# praca z datami

# normalizacja, standaryzacja

# transformacja logarytmiczna
