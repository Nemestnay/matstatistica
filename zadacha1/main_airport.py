import pandas as pd
import matplotlib.pyplot as plt
from statistics import variance, mean, median
import numpy as np


file = open('airportdat.txt', 'r')
zagolovok = ['Scheduled departures','Performed departures','Enplaned passangers',
             'Enplaned revenue tons of freight','Enplaned revenue tons of mail']
scheduled = []
performed=[]
passengers = []
freight = []
mail = []
data = []
for line in file:
    tek = list(map(str, line.split()))
    data.append([int(tek[-5]), int(tek[-4]), int(tek[-3]), float(tek[-2]), float(tek[-1])])
    scheduled.append(int(tek[-5]))
    performed.append(int(tek[-4]))
    passengers.append(int(tek[-3]))
    freight.append(float(tek[-2]))
    mail.append(float(tek[-1]))
file.close()

print("Выборочные средние:")
print(zagolovok[0], '%.2f' % mean(scheduled), sep=': ')
print(zagolovok[1], '%.2f' % mean(performed), sep=': ')
print(zagolovok[2], '%.2f' % mean(passengers), sep=': ')
print(zagolovok[3], '%.2f' % mean(freight), sep=': ')
print(zagolovok[4], '%.2f' % mean(mail), sep=': ')

print("\nВыборочныая дисперсия:")
print(zagolovok[0], '%.2f' % variance(scheduled), sep=': ')
print(zagolovok[1], '%.2f' % variance(performed), sep=': ')
print(zagolovok[2], '%.2f' % variance(passengers), sep=': ')
print(zagolovok[3], '%.2f' % variance(freight), sep=': ')
print(zagolovok[4], '%.2f' % variance(mail), sep=': ')

print("\nСтандратное отклонение:")
print(zagolovok[0], '%.2f' % np.std(scheduled), sep=': ')
print(zagolovok[1], '%.2f' % np.std(performed), sep=': ')
print(zagolovok[2], '%.2f' % np.std(passengers), sep=': ')
print(zagolovok[3], '%.2f' % np.std(freight), sep=': ')
print(zagolovok[4], '%.2f' % np.std(mail), sep=': ')

print("\n1-квартиль, Медиана, 3-ий квартиль:")
print(zagolovok[0],': ', '%.2f' % np.percentile(scheduled, 25), ', ', '%.2f' % median(scheduled),', ', '%.2f' % np.percentile(scheduled, 75), sep='')
print(zagolovok[1],': ', '%.2f' % np.percentile(performed, 25), ', ', '%.2f' % median(performed),', ', '%.2f' % np.percentile(performed, 75), sep='')
print(zagolovok[2],': ', '%.2f' % np.percentile(passengers, 25), ', ', '%.2f' % median(passengers),', ', '%.2f' % np.percentile(passengers, 75), sep='')
print(zagolovok[3],': ', '%.2f' % np.percentile(freight, 25), ', ', '%.2f' % median(freight),', ', '%.2f' % np.percentile(freight, 75), sep='')
print(zagolovok[4],': ', '%.2f' % np.percentile(mail, 25), ', ', '%.2f' % median(mail),', ', '%.2f' % np.percentile(mail, 75), sep='')

print("\nПопарные коэффициенты корреляции между переменными:")
mas = pd.DataFrame(data, columns=['p1','p2','p3','p4','p5'])
print(mas.corr())

f, ax = plt.subplots(2, 5)
ax[0, 0].boxplot(scheduled)
ax[0, 1].boxplot(performed)
ax[0, 2].boxplot(passengers)
ax[0, 3].boxplot(freight)
ax[0, 4].boxplot(mail)

ax[1, 0].hist(scheduled)
ax[1, 1].hist(performed)
ax[1, 2].hist(passengers)
ax[1, 3].hist(freight)
ax[1, 4].hist(mail)

ax[0, 0].set_title(zagolovok[0])
ax[0, 1].set_title(zagolovok[1])
ax[0, 2].set_title(zagolovok[2])
ax[0, 3].set_title(zagolovok[3])
ax[0, 4].set_title(zagolovok[4])

plt.show()

