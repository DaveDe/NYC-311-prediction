#Day indexes to years:
#2010 - 0:365
#2011 - 365:730
#2012 - 730:1096  LEAP YEAR
#2013 - 1096:1461
#2014 - 1461:1826
#2015 - 1826:2191
#2016 - 2191:2557 LEAP YEAR
#2017 - 2557:2922
#2018 - 2922:3097

import matplotlib.pyplot as plt
import numpy as np

data_path = '/home/mllab/Desktop/defazio-311/Data/all.csv'
#data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/DEP.csv'

data = np.genfromtxt(data_path, delimiter=',')

response_times = data[1:,2]
demands = data[1:,1]

months = [x for x in range(0,12)]

response_times = response_times[731:1096]

#get month heights
days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
heights = [0 for x in range(0,12)]

day = 0
for index,num_days in enumerate(days_in_months):
	for i in range(day,day+num_days):
		heights[index] += response_times[i]
	heights[index] /= num_days #height is the average
	day += num_days

print(heights)

plt.bar(months, heights, align='center')
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12], ['jan','feb','mar','apr', 'may', 'june', 
	'july', 'aug', 'sep', 'oct', 'nov', 'dec'])
plt.ylabel('Average Median Response Time')
plt.xlabel('Month')
plt.title('Average Median Response Times per Month 2017')
plt.show()
"""days = [x for x in range(0,response_times.shape[0])]
#days = [x for x in range(0,365)]

plt.plot(days, response_times)
#plt.plot(days, demands)#, color='orange'
plt.xlabel('Day')
plt.xticks([0,365,731,1086], ['2015','2016','2017','2018'])
#plt.ylabel('Demand (in number of calls)')
#plt.title('Demand per Day, for 2015')
plt.ylabel('Response time (in hours)')
plt.title('Median Response Time per Day from 2015 - Present')
#plt.legend()
plt.show()"""