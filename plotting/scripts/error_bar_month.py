import matplotlib.pyplot as plt
import numpy as np

data_path = '/home/mllab/Desktop/defazio-311/Data/all.csv'
#data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/DEP.csv'

data = np.genfromtxt(data_path, delimiter=',')

response_times = data[1:,2]
demands = data[1:,1]

months = [x for x in range(0,12)]


month_values = [[] for x in range(0,12)]

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

#2010
start_day = 0
days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
for index,num_days in enumerate(days_in_months):
	vals = []
	for i in range(start_day,start_day+num_days):
		vals.append(response_times[i])
	month_values[index].append(sum(vals)/len(vals))
	start_day += num_days

#2011
start_day = 365
days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
for index,num_days in enumerate(days_in_months):
	vals = []
	for i in range(start_day,start_day+num_days):
		vals.append(response_times[i])
	month_values[index].append(sum(vals)/len(vals))
	start_day += num_days

#2012
start_day = 730
days_in_months = [31,29,31,30,31,30,31,31,30,31,30,31]
for index,num_days in enumerate(days_in_months):
	vals = []
	for i in range(start_day,start_day+num_days):
		vals.append(response_times[i])
	month_values[index].append(sum(vals)/len(vals))
	start_day += num_days

#2013
start_day = 1096
days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
for index,num_days in enumerate(days_in_months):
	vals = []
	for i in range(start_day,start_day+num_days):
		vals.append(response_times[i])
	month_values[index].append(sum(vals)/len(vals))
	start_day += num_days

#2014
start_day = 1461
days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
for index,num_days in enumerate(days_in_months):
	vals = []
	for i in range(start_day,start_day+num_days):
		vals.append(response_times[i])
	month_values[index].append(sum(vals)/len(vals))
	start_day += num_days

#2015
start_day = 1826
days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
for index,num_days in enumerate(days_in_months):
	vals = []
	for i in range(start_day,start_day+num_days):
		vals.append(response_times[i])
	month_values[index].append(sum(vals)/len(vals))
	start_day += num_days

#2016
start_day = 2191
days_in_months = [31,29,31,30,31,30,31,31,30,31,30,31]
for index,num_days in enumerate(days_in_months):
	vals = []
	for i in range(start_day,start_day+num_days):
		vals.append(response_times[i])
	month_values[index].append(sum(vals)/len(vals))
	start_day += num_days

#2017
start_day = 2557
days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
for index,num_days in enumerate(days_in_months):
	vals = []
	for i in range(start_day,start_day+num_days):
		vals.append(response_times[i])
	month_values[index].append(sum(vals)/len(vals))
	start_day += num_days

heights = [0 for x in range(0,12)]
errors_list = [0 for x in range(0,12)]

#find average of month values as height
#find 2*std for errors
for i,month_bucket in enumerate(month_values):
	heights[i] = (sum(month_bucket)/len(month_bucket))
	errors_list[i] = 2*np.std(month_bucket)




errors = np.array([[0,0,0,0,0,0,0,0,0,0,0,0],errors_list])
plt.bar(months, heights, yerr=errors, align='center')
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12], ['jan','feb','mar','apr', 'may', 'june', 
	'july', 'aug', 'sep', 'oct', 'nov', 'dec'])
plt.ylabel('Average Median Response Time')
plt.xlabel('Month')
plt.title('Average Median Response Times per Month From 2010 - Present')

plt.savefig('error_bar_month.eps')
plt.show()
