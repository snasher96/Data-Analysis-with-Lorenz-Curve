"""
Creater: Sheikh "Nash" Nasher
Date Created: 20 February, 2018
"""
"""
The NumPy file "Pop2010" contains the population of N=200+ countries and territories in 2010 (in mln. people).
A Lorenz curve shows the contribution to the common "wealth" (in our case, the common population) of 
the bottom x "people" (in our case, the countries). For example, y(1) is the contribution of the smallest country, 
y(2) is the contribution of the two smallest countries, and y(N) is the total contribution (which is equal to either 1.0 or 100%). 
Typically, the range of x is normalized either to 0.0-1.0 or 0%-100%, too. Using only NumPy and matplotlib, plot the Lorenz curve 
for the population data. The curve shall be normalized both in X and Y dimensions to the range from 0.0 to 1.0. The program shall 
not use any loops or non-array arithmetic operations. Make sure the plot has the axes labels and a title. 
The program shall save the plot as population-lorenz.png with the resolution of 200dpi. 
"""

import numpy as np
from matplotlib import pyplot as plt

'''
Load the NumPy file contains the population of N=200+ countries 
and territories in 2010 (in mln. people)
'''

X=np.load('C:\\Users\\Owner\\Downloads\\Computer\\Anaconda3 4.4.0\\pop2010.npy')

def G(v):
    bins = np.linspace(1,100)
    total = float(np.sum(X))
    y_values = []
    for b in bins:
        bin_vals = X[X <= np.percentile(X, b)]
        bin_fraction = (np.sum(bin_vals) / total)*100.0
        y_values.append(bin_fraction)
              
        
    # perfect equality area
    pe_area = np.trapz(bins, x=bins)
    
    # lorenz area
    lorenz_area = np.trapz(y_values, x=bins)
    gini_value = (pe_area - lorenz_area) / float(pe_area)
    return bins, y_values, gini_value


bins, result, gini_value = G(X)

# Plot the graph 
plt.figure()
plt.plot(bins, result, label="Observed")
plt.plot(bins, bins, '--', label="Perfect eq.")
plt.xlabel("Fraction of population")
plt.ylabel("Fraction of wealth")
plt.title("Lorenz Curve" )
plt.legend()
plt.savefig('Lorenz Curve.png',dpi=200)
plt.show()
