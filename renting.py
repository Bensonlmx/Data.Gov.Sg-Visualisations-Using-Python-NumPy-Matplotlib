import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("/Users/benson/Desktop/Upskilling/SP/IT8701 Introduction to Programming for Data Science/Assignment1/active-cases-of-renting-out-of-flat.csv",
                     skip_header=1,
                     dtype=[('financial_year','i8'), ('type','U10'), ('no_active_cases','i8')], delimiter=",",
                     missing_values=['na','-'],filling_values=[0])

data_required = data[np.isin(data['type'], ['HBD flat'])]
labels = data_required['financial_year']
years = np.arange(0, len(labels))
values = data_required['no_active_cases']


plt.plot(years, values, 'o-', color = '#000067')
plt.title('Active cases of renting out of HDB flats')
plt.ylabel('No. of active cases')
plt.xlabel('Financial year from 2006 to 2018')
plt.xticks(years,labels,rotation=90)
plt.show()

