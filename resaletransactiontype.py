import numpy as np
import matplotlib.pyplot as plt

fname = "/Users/benson/Desktop/Upskilling/SP/IT8701 Introduction to Programming for Data Science/Assignment1/resale-transactions-by-flat-type-based-on-registered-cases.csv"
data = np.loadtxt(fname, skiprows=1,dtype=[('financial_year','i8'),('flat_type','U64'), ('resale_transaction','i8')],delimiter=",")

print("###Resale Transactions by Flat Type based on Registered Cases###\n")
print("There are altogether " + str(len(data)) + " rows and " + str(len(data[0])) + " columns of data in the dataset") 
print()

data_years = data['financial_year']  
years = np.unique(data_years)   
print("There are " + str(len(years)) + " years of data captured in the dataset, beginning from " + str(years[0]) + " to " + str(years[len(years)-1]))

keyword = '1 room'
column_to_search = data['flat_type']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_1room = data[out]
sum_1room = data_1room[:]['resale_transaction'].sum()
print("Total number of 1 room flat resale transactions: " + str(sum_1room))

keyword = '2 room'
column_to_search = data['flat_type']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_2room = data[out]
sum_2room = data_2room[:]['resale_transaction'].sum()
print("Total number of 2 room flat resale transactions: " + str(sum_2room))

keyword = '3 room'
column_to_search = data['flat_type']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_3room = data[out]
sum_3room = data_3room[:]['resale_transaction'].sum()
print("Total number of 3 room flat resale transactions: " + str(sum_3room))

keyword = '4 room'
column_to_search = data['flat_type']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_4room = data[out]
sum_4room = data_4room[:]['resale_transaction'].sum()
print("Total number of 4 room flat resale transactions: " + str(sum_4room))

keyword = '5 room'
column_to_search = data['flat_type']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_5room = data[out]
sum_5room = data_5room[:]['resale_transaction'].sum()
print("Total number of 5 room flat resale transactions: " + str(sum_5room))

keyword = 'Executive and Multi-generation'
column_to_search = data['flat_type']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_emg = data[out]
sum_emg = data_emg[:]['resale_transaction'].sum()
print("Total number of Executive and Multi-generational flat resale transactions: " + str(sum_emg))

keyword = 'HUDC'
column_to_search = data['flat_type']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_HUDC = data[out]
sum_HUDC = data_HUDC[:]['resale_transaction'].sum()
print("Total number of HUDC flat resale transactions: " + str(sum_HUDC))

data = [sum_1room, sum_2room, sum_3room, sum_4room, sum_5room, sum_emg, sum_HUDC]
labels = ['1 room', '2 room', '3 room', '4 room', '5 room', 'Executive', 'HUDC']
plt.xticks(range(len(data)), labels)
plt.xlabel('Resale Flat Type')
plt.ylabel('Number of Transactions')
plt.title('Resale Transactions by Flat Type based on Registered Cases')
plt.bar(range(len(data)), data) 


plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.show()

