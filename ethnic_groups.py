import numpy as np
import matplotlib.pyplot as plt
import csv

outfile = open("/Users/benson/Desktop/Upskilling/SP/IT8701 Introduction to Programming for Data Science/Assignment1/hdb-resident-population-by-ethnic-group.csv","r")

file=csv.reader(outfile)
#skip the headers
next(file, None)

shs_year = []
ethnic_group = []
resident_population = []

# for row in file:
#     shs_year = row[0]
#     ethnic_group = row[1]
#     resident_population = row[2]
    
for row in file:
    shs_year.append(row[0])
    ethnic_group.append(row[1])
    resident_population.append(row[2])

plt.pie(resident_population, labels=ethnic_group, autopct='%1.1f%%')
plt.axis('equal') # make the pie chart circular
plt.title('From Sample Household Survey: HDB Resident Population, by Ethnic Group (2013)')
plt.show()
