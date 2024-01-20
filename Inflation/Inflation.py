from ast import Lambda
import matplotlib.pyplot as plt
import pandas as pd

# USER CONFIG 
# Base value
BASE = 1000

# Specify the path to your CSV file
csv_file_path = 'inflation_data.csv'

def calc(base,rate_list : list):

    if len(rate_list) == 0:
        return base
    return (1+rate_list.pop())*calc(base,rate_list)

def devide_list(divisor):
    return divisor / 100

def calculate_purchasing_power(inflation_rate_list):
    length = len(inflation_rate_list)
    devaluation = []

    i = 0
    while (length>=0):
    
        if length ==0:
            x_list = inflation_rate_list
        else:
            x_list = inflation_rate_list[:(-length)]
        retVal = calc(BASE,x_list)
        devaluation.append(retVal)
        length -=1
        i+=1

    return devaluation

data = pd.read_csv('inflation_data.csv')
years = data["year"]

rate_ger = data["inflation rate germany"]
rate_us = data["inflation rate us"]
rate_swiss = data["inflation rate switzerland"]

# Calculate elegant the devaluation for Germany
rate_ger = list(map(devide_list,rate_ger))
inflation_rate_ger =  [round(x,3) for x in rate_ger] 
result_ger = calc(BASE,rate_ger)

# Calculate elegant the devaluation for US
rate_us = list(map(devide_list,rate_us))
inflation_rate_us =  [round(x,3) for x in rate_us] 
result_us = calc(BASE,rate_us)

# Calculate elegant the devaluation for Swiss
rate_swiss = list(map(devide_list,rate_swiss))
inflation_rate_swiss =  [round(x,3) for x in rate_swiss] 
result_swiss = calc(BASE,rate_swiss)

print(f"CALCULATED RESULT: Germany: {result_ger}, US: {result_us}, Switzerland: {result_swiss}")

#Create a list for rate_list year instead of one final value which was done with calc:
devaluation_ger = calculate_purchasing_power(inflation_rate_ger)
devaluation_us = calculate_purchasing_power(inflation_rate_us)
devaluation_swiss = calculate_purchasing_power(inflation_rate_swiss)

# Appending last element
years = years.append(pd.Series([2024]))


#######################################################################
# PLOT 1
#######################################################################

# Plotting the line
fig, ax = plt.subplots()

ax.plot(years, devaluation_ger,color="darkblue",label="Euro Ger)")
ax.plot(years, devaluation_us,color="darkgreen",label="USD")
ax.plot(years, devaluation_swiss,color="red",label="Swiss franc")

# Plotting the data points
ax.scatter(years, devaluation_ger, color='darkblue')
ax.scatter(years, devaluation_us, color='darkgreen')
ax.scatter(years, devaluation_swiss, color='red')

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('[Euro],[USD],[SF]')

ax.set_title('Purchasing power since 2002')

# Adding a legend
ax.legend()

ax.grid(True)  # This adds a grid to the plot

# Reduce the font size of x-axis tick labels
ax.tick_params(axis='x', labelsize=10)  # Adjust the font size as needed

# Set the desired number of ticks
desired_ticks = 10
ax.set_xticks(range(min(years), max(years) + 1),rotation=90)

ax.set_xticklabels(years,rotation=90, ha='right')

ax.locator_params(axis='y', nbins=desired_ticks)

fig.savefig('devaluation_euro.svg',format='svg')
plt.show()

#######################################################################
# PLOT 2
# Buying power of basis 
# Lets say 2002 is 100% - how is it after 22 years
#######################################################################

# Calculate the devaluation for Swiss 
# multiply with 100 to convert in %
deval_ger_perc = list(map(lambda x: 100*BASE/x,devaluation_ger)) 
deval_us_perc  = list(map(lambda x: 100*BASE/x,devaluation_us))
deval_swiss_perc = list(map(lambda x: 100*BASE/x,devaluation_swiss))

# Plotting the line
fig, ax = plt.subplots()

ax.plot(years, deval_ger_perc,color="darkblue",label="Euro Ger)")
ax.plot(years, deval_us_perc,color="darkgreen",label="USD")
ax.plot(years, deval_swiss_perc,color="red",label="Swiss franc")

# Plotting the data points
ax.scatter(years, deval_ger_perc, color='darkblue')
ax.scatter(years, deval_us_perc, color='darkgreen')
ax.scatter(years, deval_swiss_perc, color='red')

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('%')

ax.set_title('Relative devaluation since 2002')

# Adding a legend
ax.legend()

ax.grid(True)  # This adds a grid to the plot

# Reduce the font size of x-axis tick labels
ax.tick_params(axis='x', labelsize=10)  # Adjust the font size as needed

# Set the desired number of ticks
desired_ticks = 10
ax.set_xticks(range(min(years), max(years) + 1),rotation=90)
ax.set_xticklabels(years,rotation=90, ha='right')
ax.locator_params(axis='y', nbins=desired_ticks)

fig.savefig('devaluation_relative.svg',format='svg')
plt.show()

#######################################################################
# PLOT 3
# Buying power of basis 
# What is the equivalent value in year x to 1000€ in 2002
#######################################################################

# Calculate elegant the devaluation for Swiss 
deval_ger = list(map(lambda x: BASE*BASE/x,devaluation_ger)) 
deval_us  = list(map(lambda x: BASE*BASE/x,devaluation_us))
deval_swiss = list(map(lambda x: BASE*BASE/x,devaluation_swiss))

# Plotting the line
fig, ax = plt.subplots()

ax.plot(years, deval_ger,color="darkblue",label="Euro Ger)")
ax.plot(years, deval_us,color="darkgreen",label="USD")
ax.plot(years, deval_swiss,color="red",label="Swiss franc")

# Plotting the data points
ax.scatter(years, deval_ger, color='darkblue')
ax.scatter(years, deval_us, color='darkgreen')
ax.scatter(years, deval_swiss, color='red')

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('[Euro],[USD],[SF]')

ax.set_title('Absolute devaluation since 2002')

# Adding a legend
ax.legend()

ax.grid(True)  # This adds a grid to the plot

# Reduce the font size of x-axis tick labels
ax.tick_params(axis='x', labelsize=10)  # Adjust the font size as needed

# Set the desired number of ticks
desired_ticks = 10
ax.set_xticks(range(min(years), max(years) + 1),rotation=90)

ax.set_xticklabels(years,rotation=90, ha='right')
ax.locator_params(axis='y', nbins=desired_ticks)

fig.savefig('devaluation_absolute.svg',format='svg')
plt.show()