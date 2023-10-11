from random import shuffle
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# # My first solution. Здесь присваивает float, не найс
# data.loc[data['whoAmI'] == 'robot', 'robot'] = int(1)
# data.loc[data['whoAmI'] == 'robot', 'human'] = int(0)
# data.loc[data['whoAmI'] == 'human', 'human'] = int(1)
# data.loc[data['whoAmI'] == 'human', 'robot'] = int(0)
# del data['whoAmI']
# print(data)

# # Another my solution
# data['robot'] = 0 # заранее присваиваем int значения в эти столбцы
# data['human'] = 0

# data.loc[data['whoAmI'] == 'robot', 'robot'] = 1
# data.loc[data['whoAmI'] == 'human', 'human'] = 1
# del data['whoAmI']
# print(data)


# 3-rd solution
data['robot'] = (data['whoAmI'] == 'robot').astype(int) # преобразовываем True/False в int
data['human'] = (data['whoAmI'] == 'human').astype(int)

del data['whoAmI']
print(data)