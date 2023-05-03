# import data.data as dt
import pandas as pd

names = ['1', '2', '3', '4', '5', '6', '7a', '7b', '8base', '8extra', '8', '9']

print("possible names:")
print(names)
print("task?")
string = input().lower().split(" ")

words = pd.DataFrame()

for x in string:
    name = x.lower()
    if name in ['8']:
        words = pd.concat([words, pd.read_csv('data/' + name + 'base.csv'),
                           pd.read_csv('data/' + name + 'extra.csv')])
    else:
        words = pd.concat([words, pd.read_csv('data/' + name + '.csv')])

words = words.sample(frac=1)

for x in range(words['0'].size):
    print(words.iloc[x]['0'])
    i = input()
    print(words.iloc[x]['1'], words.iloc[x]['2'])
    print("--------------------------------")
