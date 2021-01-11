# Data.Gov.Sg-Visualisations-Using-Python-NumPy-Matplotlib

## Pandas Aside
A collection of data science scripts for data analysis in Python, using publicly available .gov datasets. The algorithms are implemented in two ways: from scratch in Python and using only two libraries without resorting to Pandas. 

### Python Libraries Used 
- Numpy
- Matplotlib

## Installation
To install all of the libraries, run the commands in the "install.txt" file. These are:

- ```sudo apt-get install python-pip```
- ```sudo apt-get install python-matplotlib```

## Information
### Matplotlib Plotting
- **Scatter plot:** `scatter(x_data, y_data, s = 30, color = '#539caf', alpha = 0.75)`
- **Line plot:** `plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)`
- **Histogram:** `hist(data, n_bins, color = '#539caf')` 
- **Probability Density Function:** plot(x_data, density_est(x_data), color = '#539caf', lw = 2) Where `density_est(x_data)` computes the probability density of each data point
- **Bar plot:** `bar(x_data, y_data, color = '#539caf', align = 'center')`
- **Box plot:** `boxplot(y_data)` We set the x_data using the x-axis tick labels on the plot `set_xticklabels(x_data)`
