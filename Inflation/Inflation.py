from ast import Lambda
import matplotlib.pyplot as plt
import csv
import pandas as pd

# Specify the path to your CSV file
csv_file_path = 'inflation_data.csv'
global_csv_reader = None

base = 100000

devaluation_ger = []

def get_csv_column_data(column_name:str):
    global global_csv_reader
    column_values = []
    if global_csv_reader is not None:
        for row in global_csv_reader:
            # Process the data as needed
            column_values.append(row[column_name])
    else:
        print("csv_reader is not initialized")

    return column_values


def read_csv_data():
    
    global global_csv_reader

    column_values = []

    # Open the CSV file
    with open(csv_file_path, 'r') as file:
        # Create a CSV DictReader object
        global_csv_reader = csv.DictReader(file)

        for row in global_csv_reader:
            # Process the data as needed
            column_values.append(row["inflation rate germany"])

def calc(base,rate_list : list):

    if len(rate_list) == 0:
        return base
    return (1+rate_list.pop())*calc(base,rate_list)


def devide_list(divisor):
    return divisor / 100


data = pd.read_csv('inflation_data.csv')
years = data["year"]

rate_ger = data["inflation rate germany"]
rate_us = data["inflation rate us"]
rate_swiss = data["inflation rate switzerland"]


# Calculate elegant the devaluation for Germany
rate_ger = list(map(devide_list,rate_ger))
inflation_rate_ger =  [round(x,3) for x in rate_ger] 
retVal = calc(base,rate_ger)

print(retVal)
print("####")

# Calculate elegant the devaluation for US
rate_us = list(map(devide_list,rate_us))
inflation_rate_us =  [round(x,3) for x in rate_us] 
retVal = calc(base,rate_us)

print(retVal)
print("####")

# Calculate elegant the devaluation for Swiss
rate_swiss = list(map(devide_list,rate_swiss))
inflation_rate_swiss =  [round(x,3) for x in rate_swiss] 
retVal = calc(base,rate_swiss)

print(retVal)
print("####")

#Create a list for rate_list year instead of one final value which was done with calc:
length = len(inflation_rate_ger)
devaluation_ger = []

i = 0
while (length>=0):
    
    if length ==0:
        x_list = inflation_rate_ger
    else:
        x_list = inflation_rate_ger[:(-length)]
    retVal = calc(base,x_list)
    devaluation_ger.append(retVal)
    length -=1
    i+=1

#US 
#Create a list for rate_list year instead of one final value which was done with calc:
length = len(inflation_rate_us)
devaluation_us = []

i = 0
while (length>=0):
    
    if length ==0:
        x_list = inflation_rate_us
    else:
        x_list = inflation_rate_us[:(-length)]
    retVal = calc(base,x_list)
    devaluation_us.append(retVal)
    length -=1
    i+=1

print(devaluation_us)


#Swiss
#Create a list for rate_list year instead of one final value which was done with calc:
length = len(inflation_rate_swiss)
devaluation_swiss = []

i = 0
while (length>=0):
    
    if length ==0:
        x_list = inflation_rate_swiss
    else:
        x_list = inflation_rate_swiss[:(-length)]
    retVal = calc(base,x_list)
    devaluation_swiss.append(retVal)
    length -=1
    i+=1

# Appending last element
years = years.append(pd.Series([2024]))

# Plotting the line
fig, ax = plt.subplots()

ax.plot(years, devaluation_ger,color="yellow",label="Euro Ger)")
ax.plot(years, devaluation_us,color="darkblue",label="USD")
ax.plot(years, devaluation_swiss,color="red",label="Swiss franc")

# Plotting the data points
ax.scatter(years, devaluation_ger, color='yellow')
ax.scatter(years, devaluation_us, color='darkblue')
ax.scatter(years, devaluation_swiss, color='red')

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Inflation in Eurozone [Euro] / US [USDollar]')

ax.set_title('Devaluation Impact on 1 Euro / 1 USD Since 2002')

# Adding a legend
ax.legend()

ax.grid(True)  # This adds a grid to the plot

# Reduce the font size of x-axis tick labels
ax.tick_params(axis='x', labelsize=10)  # Adjust the font size as needed

# Rotate x-axis tick labels vertically

# Set the desired number of ticks
desired_ticks = 10
ax.set_xticks(range(min(years), max(years) + 1),rotation=90)


ax.set_xticklabels(years,rotation=90, ha='right')

ax.locator_params(axis='y', nbins=desired_ticks)

fig.savefig('devaluation_euro.svg',format='svg')
plt.show()



#### Buying power of basis 
# Lets say 2002 is 100% - how is it after 22 years

# Calculate elegant the devaluation for Swiss 
# multiply with 100 to convert in %
deval_ger_perc = list(map(lambda x: 100*base/x,devaluation_ger)) 
deval_us_perc  = list(map(lambda x: 100*base/x,devaluation_us))
deval_swiss_perc = list(map(lambda x: 100*base/x,devaluation_swiss))


# Plotting the line
fig, ax = plt.subplots()

ax.plot(years, deval_ger_perc,color="yellow",label="Euro Ger)")
ax.plot(years, deval_us_perc,color="darkblue",label="USD")
ax.plot(years, deval_swiss_perc,color="red",label="Swiss franc")

# Plotting the data points
ax.scatter(years, deval_ger_perc, color='yellow')
ax.scatter(years, deval_us_perc, color='darkblue')
ax.scatter(years, deval_swiss_perc, color='red')

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('%')

ax.set_title('Devaluation Impact since 2002')

# Adding a legend
ax.legend()

ax.grid(True)  # This adds a grid to the plot

# Reduce the font size of x-axis tick labels
ax.tick_params(axis='x', labelsize=10)  # Adjust the font size as needed

# Rotate x-axis tick labels vertically

# Set the desired number of ticks
desired_ticks = 10
ax.set_xticks(range(min(years), max(years) + 1),rotation=90)


ax.set_xticklabels(years,rotation=90, ha='right')

ax.locator_params(axis='y', nbins=desired_ticks)

fig.savefig('devaluation_relative.svg',format='svg')
plt.show()



#### Buying power of basis 
# What is the equivalent value in year x to 1000€ in 2002

# Calculate elegant the devaluation for Swiss 
deval_ger = list(map(lambda x: base*base/x,devaluation_ger)) 
deval_us  = list(map(lambda x: base*base/x,devaluation_us))
deval_swiss = list(map(lambda x: base*base/x,devaluation_swiss))


# Plotting the line
fig, ax = plt.subplots()

ax.plot(years, deval_ger,color="yellow",label="Euro Ger)")
ax.plot(years, deval_us,color="darkblue",label="USD")
ax.plot(years, deval_swiss,color="red",label="Swiss franc")

# Plotting the data points
ax.scatter(years, deval_ger, color='yellow')
ax.scatter(years, deval_us, color='darkblue')
ax.scatter(years, deval_swiss, color='red')

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('€ / $ / SF')

ax.set_title('Devaluation Impact since 2002')

# Adding a legend
ax.legend()

ax.grid(True)  # This adds a grid to the plot

# Reduce the font size of x-axis tick labels
ax.tick_params(axis='x', labelsize=10)  # Adjust the font size as needed

# Rotate x-axis tick labels vertically

# Set the desired number of ticks
desired_ticks = 10
ax.set_xticks(range(min(years), max(years) + 1),rotation=90)


ax.set_xticklabels(years,rotation=90, ha='right')

ax.locator_params(axis='y', nbins=desired_ticks)

fig.savefig('devaluation_absolute.svg',format='svg')
plt.show()