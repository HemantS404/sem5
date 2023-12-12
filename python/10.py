# import pandas as pd

# x = [1,2,3]
# s = pd.Series(x)
# print(s)
# print()
# x = [1,2,3]
# s = pd.Series(x, index  =['day1','day2','day3'])
# print(s)
# print()
# x = {"day1":1,"day2":2,"day3":3}
# s = pd.Series(x)
# print(s)
# print()
# data = {
#     'calorie':[10,20,30],
#     'nutrient':[1,2,3]
# }
# df = pd.DataFrame(data)
# print(df)
# print()
# data = {
#     'calorie':[10,20,30],
#     'nutrient':[1,2,3]
# }
# df = pd.DataFrame(data, index=['day1','day2','day3'])
# print(df)
# print()
# print(df.loc['day2'])
# df = pd.read_csv("housing_price_dataset.csv")
# print(df.head())
# print()
# print(df.tail())
# print()
# print(df['SquareFeet'].mean())
# print()
# print(df['SquareFeet'].median())
# print()
# print(df.describe())
# print()
# df_dash = df.drop(['Neighborhood'], axis =1)
# print(df_dash.corr())
# print()

# import matplotlib.pyplot as plt

# x = ["A","B","C","D"]
# y = [10, 25, 30, 39]
# plt.bar(x, y)
# plt.show()
# plt.plot(x, y)
# plt.show()
# plt.pie(y, labels=x)
# plt.show()
# x = [10, 20, 30, 40, 50]
# y = [5, 4, 3, 2, 1]
# plt.plot(x, y)
# plt.show()
# x = [10,3,4,60,7,80,4,35,6,2,8,40,56,28]
# y = [3,56,62,91,46,8,34,52,67,23,38,51,73,73]
# plt.scatter(x, y)
# plt.show()
# plt.hist(x+y)
# plt.show()

# import numpy as np
# x = np.random.normal(170,10,250)
# plt.hist(x)
# plt.show()