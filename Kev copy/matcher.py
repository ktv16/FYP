import pandas as pd
import tqdm as tqdm
import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/kevinvela/Desktop/Kev/Pairs_Found.csv')

sheet_1 = list(df['sheet name 1'])
sheet_2 = list(df['sheet name 2'])


#make dictionary which maps all possible combinations and their ocurrences
def matcher(array_1, array_2):
    combined = []
    matches = []
    combs = []
    set1 = set(array_1)
    set2 = set(array_2)
    combinations = [(x+y) for x in set1 for y in set2]

    for i in range(len(array_1)):
        combined.append(array_1[i] + array_2[i])

    for x in combinations:
        matches.append(combined.count(x))

    for j in range(len(combinations)):
        combs.append(combinations[j][:5]+ '&' + combinations[j][5:])

    dictionary = dict(zip(combs,matches))


    return combs, matches, dictionary


combs, matches, dictionary = matcher(sheet_1, sheet_2)

a, b = zip(*(s.split("&") for s in combs))
header = ['Sheet 1', 'Sheet 2', 'Matches']


with open('matches_new.csv', 'wt') as file:
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    wr.writerow(header)
    wr.writerows(zip(a,b,matches))


print("writing completed")

df2 = pd.read_csv('/Users/kevinvela/Desktop/Kev/matches_new.csv')
result = df2.pivot(index='Sheet 1', columns='Sheet 2', values='Matches')
result2 = result.replace(0, " ")
sns.heatmap(result, annot=result2, annot_kws={"size": 9}, fmt='', cmap='viridis')
plt.title('')
plt.show()
