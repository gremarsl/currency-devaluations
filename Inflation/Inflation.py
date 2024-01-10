import matplotlib.pyplot as plt

years = [2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
        ]


inflation_rate_germany = [1.4,#2002
                          1.0,#2003
                          1.6,#2004
                          1.6,#2005
                          1.6,#2006
                          2.3,#2007
                          2.6,#2008
                          0.3,#2009
                          1.0,#2010
                          2.2,#2011
                          1.9,#2012
                          1.5,#2013
                          1.0,#2014
                          0.5,#2015
                          0.5,#2016
                          1.5,#2017
                          1.8,#2018
                          1.4,#2019
                          0.5,#2020
                          3.1,#2021
                          6.9,#2022
                          5.9,#2023
                          ]

base = 1

inflation_result_list = []

def calc(base,rate_list : list):

    if len(rate_list) == 0:
        return base
    return (1+rate_list.pop())*calc(base,rate_list)


def devide_list(divisor):
    return divisor / 100

rate_list = inflation_rate_germany
print(rate_list)

rate_list = list(map(devide_list,rate_list))
inflation_rate_list =  [round(x,3) for x in rate_list] 
retVal = calc(base,rate_list)

print(retVal)
print("####")

#Create a list for rate_list year instead of one final value which was done with calc:
length = len(inflation_rate_list)
inflation_result_list = []

i = 0
while (length>=0):
    
    if length ==0:
        x_list = inflation_rate_list
    else:
        x_list = inflation_rate_list[:(-length)]
    retVal = calc(base,x_list)
    inflation_result_list.append(retVal)
    length -=1
    print(i)
    i+=1

# Appending last element
years.append(2024)

# Plotting the line
fig, ax = plt.subplots()

ax.plot(years, inflation_result_list,color="darkblue")

# Plotting the data points
ax.scatter(years, inflation_result_list, color='darkgreen')

# Adding labels and title
ax.set_xlabel('Inflation in Eurozone [Euro]')
ax.set_ylabel('Year')
ax.set_title('Annual Inflation Impact on 1Euro Since 2002')

# Adding a legend
ax.legend()

ax.grid(True)  # This adds a grid to the plot

# Set the desired number of ticks
desired_ticks = 10
ax.set_xticks(range(min(years), max(years) + 1))

ax.locator_params(axis='y', nbins=desired_ticks)

fig.savefig('devaluation_euro.svg',format='svg')
plt.show()