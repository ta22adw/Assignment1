#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23  2 13:31:44 2023

@author:  Timothy Atoyebi
"""

# Assignment 1: Visualisation
# Data source:https://www.who.int/data/gho/data/themes/topics/topic-details/GHO/malaria-cases-deaths
# Import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Load the dataset into a Pandas dataframe
url = 'Data source:https://www.who.int/data/gho/data/themes/topics/topic-details/GHO/malaria-cases-deaths'
data = pd.read_csv('MALARIA_TOTAL_CASES.csv')
print(data)

# Filter the data to include only the countries of interest
countries = ["BEN", "GMB", "GHA", "BDI", "NGA", "SEN"]

# filter data for some Countries
benin = data[data.SpatialDimensionValueCode == 'BEN']
gambia = data[data.SpatialDimensionValueCode == 'GMB']
ghana = data[data.SpatialDimensionValueCode == 'GHA']
burundi = data[data.SpatialDimensionValueCode == 'BDI']
nigeria = data[data.SpatialDimensionValueCode == 'NGA']
senegal = data[data.SpatialDimensionValueCode == 'SEN']


# create line graph for Countries
plt.plot(benin['TimeDim'], benin['NumericValue']/10**5)
plt.plot(gambia['TimeDim'], gambia['NumericValue']/10**5)
plt.plot(ghana['TimeDim'],ghana['NumericValue']/10**5)
plt.plot(burundi['TimeDim'], burundi['NumericValue']/10**5)
plt.plot(nigeria['TimeDim'], nigeria['NumericValue']/10**5)
plt.plot(senegal['TimeDim'], senegal['NumericValue']/10**5)


# adding the title and legend of the countries
plt.title('Reported Malaria Cases in Some Countries')
plt.xlabel('Year')
plt.ylabel('Number of Reported Cases In Millions')
plt.legend(countries)
plt.show()


# creating the bar graph for the Assignment
# Filter the data to include only the countries of interest and the MALARIA_TOTAL_CASES indicator
filtered_data = data.loc[(data["IndicatorCode"] == "MALARIA_TOTAL_CASES") & (data["SpatialDimensionValueCode"].isin(countries))]

# Aggregate the data by country, summing the NumericValue for each year
grouped_data = filtered_data.groupby("SpatialDimensionValueCode")["NumericValue"].sum().reset_index()

# Creating bar chart with the country names
plt.bar(grouped_data["SpatialDimensionValueCode"], grouped_data["NumericValue"]/10**5)
plt.title("Reported Malaria Cases in Some Countries")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.show()


# creating the pie graph for the Assignment
# picking the year 2020
first_data = data[data['TimeDimensionValue'] == 2018]

# filter data for some countries
benin_cases = first_data[first_data['SpatialDimensionValueCode'] == 'BEN']['NumericValue'].values[0]
gambia_cases = first_data[first_data['SpatialDimensionValueCode'] == 'GMB']['NumericValue'].values[0]
ghana_cases = first_data[first_data['SpatialDimensionValueCode'] == 'GHA']['NumericValue'].values[0]
burundi_cases = first_data[first_data['SpatialDimensionValueCode'] == 'BDI']['NumericValue'].values[0]
nigeria_cases = first_data[first_data['SpatialDimensionValueCode'] == 'NGA']['NumericValue'].values[0]
senegal_cases = first_data[first_data['SpatialDimensionValueCode'] == 'SEN']['NumericValue'].values[0]

#ploting the pie and adding the title and label
plt.pie([benin_cases, gambia_cases, ghana_cases, burundi_cases, nigeria_cases, senegal_cases], 
        labels=['BEN', 'GMB', 'GHA', 'BDI', 'NGA', 'SEN'], autopct='%1.1f%%')
plt.title('Proportion of malaria cases in some countries in 2018')
plt.show()

# creating another year for the pie graph to compare
# picking the year 2021
second_data = data[data['TimeDimensionValue'] == 2020]

# filter data for some countries
benin_cases = second_data[second_data['SpatialDimensionValueCode'] == 'BEN']['NumericValue'].values[0]
gambia_cases = second_data[second_data['SpatialDimensionValueCode'] == 'GMB']['NumericValue'].values[0]
ghana_cases = second_data[second_data['SpatialDimensionValueCode'] == 'GHA']['NumericValue'].values[0]
burundi_cases = second_data[second_data['SpatialDimensionValueCode'] == 'BDI']['NumericValue'].values[0]
nigeria_cases = second_data[second_data['SpatialDimensionValueCode'] == 'NGA']['NumericValue'].values[0]
senegal_cases = second_data[second_data['SpatialDimensionValueCode'] == 'SEN']['NumericValue'].values[0]

#ploting the pie and adding the title and label
plt.pie([benin_cases, gambia_cases, ghana_cases, burundi_cases, nigeria_cases, senegal_cases], 
        labels=['BEN', 'GMB', 'GHA', 'BDI', 'NGA', 'SEN'], autopct='%1.1f%%')
plt.title('Proportion of malaria cases in some countries in 2020')
plt.show()











