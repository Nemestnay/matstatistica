import pandas as pd
import matplotlib.pyplot as plt
from statistics import variance, mean, median
import numpy as np


file = open('babyboom_dat.txt', 'r')
zagolovok = ['Time of birth', 'Sex', 'Birth weight in grams', 'Number of minutes after midnight of each birth']
time = []
sex=[]
weight = []
numer_of_minutes = []
data = []
for line in file:
    tek = list(map(str, line.split()))
    data.append([int(tek[-4]), int(tek[-3]), float(tek[-2]), float(tek[-1])])
    time.append(int(tek[-4]))
    sex.append(int(tek[-3]))
    weight.append(int(tek[-2]))
    numer_of_minutes.append(float(tek[-1]))
file.close()

print("Выборочные средние:")
print(zagolovok[2], '%.2f' % mean(weight), sep=': ')
print(zagolovok[3], '%.2f' % mean(numer_of_minutes), sep=': ')

print("\nВыборочныая дисперсия:")
print(zagolovok[2], '%.2f' % variance(weight), sep=': ')
print(zagolovok[3], '%.2f' % variance(numer_of_minutes), sep=': ')

print("\nСтандратное отклонение:")
print(zagolovok[2], '%.2f' % np.std(weight), sep=': ')
print(zagolovok[3], '%.2f' % np.std(numer_of_minutes), sep=': ')

print("\n1-квартиль, Медиана, 3-ий квартиль:")
print(zagolovok[2],': ', '%.2f' % np.percentile(weight, 25), ', ', '%.2f' % median(weight), ', ', '%.2f' % np.percentile(weight, 75), sep='')
print(zagolovok[3],': ', '%.2f' % np.percentile(numer_of_minutes, 25), ', ', '%.2f' % median(numer_of_minutes), ', ', '%.2f' % np.percentile(numer_of_minutes, 75), sep='')
print("\nПопарные коэффициенты корреляции между переменными:")

mas = pd.DataFrame(np.column_stack([weight, numer_of_minutes]), columns=['Birth weight in grams', 'Number of minutes after midnight of each birth'])
print(mas.corr())

f, ax = plt.subplots(2, 4)
ax[0, 0].boxplot(time)
ax[0, 1].boxplot(sex)
ax[0, 2].boxplot(weight)
ax[0, 3].boxplot(numer_of_minutes)

ax[1, 0].hist(time)
ax[1, 1].hist(sex)
ax[1, 2].hist(weight)
ax[1, 3].hist(numer_of_minutes)


ax[0, 0].set_title(zagolovok[0])
ax[0, 1].set_title(zagolovok[1])
ax[0, 2].set_title(zagolovok[2])
ax[0, 3].set_title(zagolovok[3])
plt.show()
