# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 18:28:52 2022

@author: DELL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Reading csv file using pandas
# The demographic data of four different countries from 1990 to 2020

India = pd.read_csv('India Demography.csv', header=None)
print(India)
China = pd.read_csv('China Demography.csv', header=None)
print(China)
USA = pd.read_csv('USA Demography.csv', header=None)
print(USA)
France = pd.read_csv('France Demography.csv', header=None)
print(France)

# Birth Rate = Birth Rate (per 1000)
# Death Rate = Death Rate (per 1000)

India.columns = ['Year', 'Birth Rate', 'Death Rate', 'Population']
India.head()
China.columns = ['Year', 'Birth Rate', 'Death Rate', 'Population']
China.head()
USA.columns = ['Year', 'Birth Rate', 'Death Rate', 'Population']
USA.head()
France.columns = ['Year', 'Birth Rate', 'Death Rate', 'Population']
France.head()

# Defining a function called average and find out the average of every data
# Calculating average birth rate of each country


def Average1():
    print('Avarage Birth Rate of India = %.2f' % India['Birth Rate'].mean())
    print('Average Birth Rate of China  = %.2f' % China['Birth Rate'].mean())
    print('Average Birth Rate of USA = %.2f' % USA['Birth Rate'].mean())
    print('Average Birth Rate of France = %.2f' % France['Birth Rate'].mean())
Average1()

# ploting lineplot with respect to the birth rate of each country

plt.plot(India['Year'], India['Birth Rate'], label='India')
plt.plot(China['Year'], China['Birth Rate'], label='China')
plt.plot(USA['Year'], USA['Birth Rate'], label='USA')
plt.plot(France['Year'], France['Birth Rate'], label='France')


plt.xlabel('YEAR')
plt.ylabel('BIRTH RATE')
plt.legend()
plt.title('LINE PLOT', size=20, weight='bold')
plt.savefig('LineBR.png')
plt.show()

# Calculating average death rate of each country

def Average2():
    print('Avarage Death Rate  of India = %.2f' % India['Death Rate'].mean())
    print('Average Death Rate of China  = %.2f' % China['Death Rate'].mean())
    print('Average Death Rate of USA = %.2f' % USA['Death Rate'].mean())
    print('Average Death Rate of  France = %.2f' % France['Death Rate'].mean())
Average2()


# Creating a list of the four countries

Countries = ['INDIA', 'CHINA', 'USA', 'FRANCE']
ret = [India['Death Rate'], China['Death Rate'], USA['Death Rate'], France['Death Rate']]

# Ploting boxplot with respect to the Death Rate of each country 

plt.figure()
plt.boxplot(ret, labels=Countries)
plt.xlabel('COUNTRIES')
plt.ylabel('DEATH RATE')
plt.title('BOX PLOT', size=20, weight='bold')
plt.savefig('BoxDR.png')
plt.show()

# Finding average population of each country to plot a pie chart

def Average3():
    print('Avarage Population of India = %.2f' % India['Population'].mean())
    print('Average Population of China  = %.2f' % China['Population'].mean())
    print('Average Population of USA = %.2f' % USA['Population'].mean())
    print('Average Population of France = %.2f' % France['Population'].mean())
Average3() 


# used average population of each country to form np array to aid normalisation

Country = ['INDIA', 'CHINA', 'USA', 'FRANCE']
Average = np.array([ 1145915838.26, 1292726645.16, 293995995.94, 61071548.39])

# Ploting pie chart with respect to average population of each country

plt.figure()
plt.pie(Average, labels=Country)
plt.title('POPULATION', size=20, weight='bold')
plt.savefig('PiPopulation.png')
plt.show()




















