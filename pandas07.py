# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:30:44 2024

@author: Admin
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)
print(file.info())
print(file.describe())

import pandas

file = pandas.read_csv("iris.csv")

print(file)

import pandas
file = pandas.read_csv("diab_data.csv")
print(file)

import pandas
file = pandas.read_csv("housing_data.csv")
print(file)
print(file.info())

