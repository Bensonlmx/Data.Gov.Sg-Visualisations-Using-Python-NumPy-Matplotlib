import numpy as np
import matplotlib.pyplot as plt

fname = "/Users/benson/Desktop/Upskilling/SP/IT8701 Introduction to Programming for Data Science/Assignment1/land-area-and-dwelling-units-by-town4.csv"
data = np.loadtxt(fname, skiprows=1,dtype=[('financial_year','i8'),('town','U64'), ('dwelling_units_under_management','i8')],delimiter=",")

print("###Resale Transactions by Flat Type based on Registered Cases###\n")
print("There are altogether " + str(len(data)) + " rows and " + str(len(data[0])) + " columns of data in the dataset") 
print()

data_years = data['financial_year']  
years = np.unique(data_years)   
print("There are " + str(len(years)) + " years of data captured in the dataset, beginning from " + str(years[0]) + " to " + str(years[len(years)-1]))

keyword = 'Ang Mo Kio'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_AngMoKio = data[out]
sum_AngMoKio = data_AngMoKio[:]['dwelling_units_under_management'].sum()
print("Total number of Ang Mo Kio: " + str(sum_AngMoKio))

keyword = 'Bedok'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Bedok = data[out]
sum_Bedok = data_Bedok[:]['dwelling_units_under_management'].sum()
print("Total number of Bedok: " + str(sum_Bedok))

keyword = 'Bishan'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Bishan = data[out]
sum_Bishan = data_Bishan[:]['dwelling_units_under_management'].sum()
print("Total number of Bishan: " + str(sum_Bishan))

keyword = 'Bukit Batok'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_BukitBatok = data[out]
sum_BukitBatok = data_BukitBatok[:]['dwelling_units_under_management'].sum()
print("Total number of Bukit Batok: " + str(sum_BukitBatok))

keyword = 'Bukit Merah'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_BukitMerah = data[out]
sum_BukitMerah = data_BukitMerah[:]['dwelling_units_under_management'].sum()
print("Total number of Bukit Merah: " + str(sum_BukitMerah))

keyword = 'Bukit Panjang'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_BukitPanjang = data[out]
sum_BukitPanjang = data_BukitPanjang[:]['dwelling_units_under_management'].sum()
print("Total number of Bukit Panjang: " + str(sum_BukitPanjang))

keyword = 'Choa Chu Kang'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_ChoaChuKang = data[out]
sum_ChoaChuKang = data_ChoaChuKang[:]['dwelling_units_under_management'].sum()
print("Total number of Chao Chu Kang: " + str(sum_ChoaChuKang))

keyword = 'Clementi'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Clementi = data[out]
sum_Clementi = data_Clementi[:]['dwelling_units_under_management'].sum()
print("Total number of Clementi: " + str(sum_Clementi))

keyword = 'Geylang'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Geylang = data[out]
sum_Geylang = data_Geylang[:]['dwelling_units_under_management'].sum()
print("Total number of Geylang: " + str(sum_Geylang))

keyword = 'Hougang'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Hougang = data[out]
sum_Hougang = data_Hougang[:]['dwelling_units_under_management'].sum()
print("Total number of Hougang: " + str(sum_Hougang))

keyword = 'Jurong East'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_JurongEast = data[out]
sum_JurongEast = data_JurongEast[:]['dwelling_units_under_management'].sum()
print("Total number of Jurong East: " + str(sum_JurongEast))

keyword = 'Jurong West'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_JurongWest = data[out]
sum_JurongWest = data_JurongWest[:]['dwelling_units_under_management'].sum()
print("Total number of Jurong West: " + str(sum_JurongWest))

keyword = 'Kallang_Whampoa'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Kallang_Whampoa = data[out]
sum_Kallang_Whampoa = data_Kallang_Whampoa[:]['dwelling_units_under_management'].sum()
print("Total number of Kallang/Whampoa: " + str(sum_Kallang_Whampoa))

keyword = 'Pasir Ris'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_PasirRis = data[out]
sum_PasirRis = data_PasirRis[:]['dwelling_units_under_management'].sum()
print("Total number of Pasir Ris: " + str(sum_PasirRis))

keyword = 'Punggol'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Punggol = data[out]
sum_Punggol = data_Punggol[:]['dwelling_units_under_management'].sum()
print("Total number of Punggol: " + str(sum_Punggol))

keyword = 'Queenstown'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Queenstown = data[out]
sum_Queenstown = data_Queenstown[:]['dwelling_units_under_management'].sum()
print("Total number of Queenstown: " + str(sum_Queenstown))

keyword = 'Sembawang'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Sembawang = data[out]
sum_Sembawang = data_Sembawang[:]['dwelling_units_under_management'].sum()
print("Total number of Sembawang: " + str(sum_Sembawang))

keyword = 'Sengkang'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Sengkang = data[out]
sum_Sengkang = data_Sengkang[:]['dwelling_units_under_management'].sum()
print("Total number of Sengkang: " + str(sum_Sengkang))

keyword = 'Serangoon'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Serangoon = data[out]
sum_Serangoon = data_Serangoon[:]['dwelling_units_under_management'].sum()
print("Total number of Serangoon: " + str(sum_Serangoon))

keyword = 'Tampines'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Tampines = data[out]
sum_Tampines = data_Tampines[:]['dwelling_units_under_management'].sum()
print("Total number of Tampines: " + str(sum_Tampines))

keyword = 'Toa Payoh'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_ToaPayoh = data[out]
sum_ToaPayoh = data_ToaPayoh[:]['dwelling_units_under_management'].sum()
print("Total number of Toa Payoh: " + str(sum_ToaPayoh))

keyword = 'Woodlands'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Woodlands = data[out]
sum_Woodlands = data_Woodlands[:]['dwelling_units_under_management'].sum()
print("Total number of Woodlands: " + str(sum_Woodlands))

keyword = 'Yishun'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_Yishun = data[out]
sum_Yishun = data_Yishun[:]['dwelling_units_under_management'].sum()
print("Total number of Yishun: " + str(sum_Yishun))

keyword = 'Other Estates'
column_to_search = data['town']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_OtherEstates = data[out]
sum_OtherEstates = data_OtherEstates[:]['dwelling_units_under_management'].sum()
print("Total number of Other Estates: " + str(sum_OtherEstates))


data = [sum_AngMoKio, sum_Bedok, sum_Bishan, sum_BukitBatok, sum_BukitMerah, sum_BukitPanjang, sum_ChoaChuKang, sum_Clementi, sum_Geylang, sum_Hougang, sum_JurongEast, sum_JurongWest, sum_Kallang_Whampoa, sum_PasirRis, sum_Punggol, sum_Queenstown, sum_Sembawang, sum_Sengkang, sum_Serangoon, sum_Tampines, sum_ToaPayoh, sum_Woodlands, sum_Yishun, sum_OtherEstates]
labels = ['Ang Mo Kio', 'Bedok', 'Bishan', 'Bukit Batok', 'Bukit Merah', 'Bukit Panjang', 'Choa Chu Kang', 'Clement', 'Geylang', 'Hougang', 'Jurong East', 'Jurong West', 'Kallang/Whampoa', 'Pasir Ris', 'Punggol', 'Queenstown', 'Sembawang', 'Sengkang', 'Serangoon', 'Tampines', 'Toa Payoh', 'Woodlands', 'Yishun', 'Other Estates']
plt.xticks(range(len(data)), labels, rotation=90)
plt.xlabel('Town')
plt.ylabel('Number of dwelling units under management')
plt.title('Land area and dwelling units by towns in FY2018')
plt.scatter(range(len(data)), data)

plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.show()


