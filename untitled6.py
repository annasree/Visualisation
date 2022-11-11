# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:09:27 2022

@author: DELL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Reading csv file using pandas
India = pd.read_csv('Demography India.csv',header=None)
print(India)

"""
BR  = Birth Rate
DR = Death Rate
LE = Life Expectancy
IMR = Infant Mortality Rate

"""

India.columns = ['Year', 'BR', 'DR', 'LE', 'IMR', 'Population']

India.head()

#Calculating average of each column

print('Avarage Birth Rate = %.2f' % India['BR'].mean())
print('Average Death Rate = %.2f' % India['DR'].mean())
print('Average Life Expectancy = %.2f' % India['LE'].mean())
print('Average Infant Mortality Rate = %.2f' % India['IMR'].mean())


plt.plot(India['Year'], India['BR'], label='BR')
plt.plot(India['Year'], India['DR'], label='DR')

plt.xlabel('YEAR')
plt.ylabel('RATE')
plt.legend()
plt.show()

















