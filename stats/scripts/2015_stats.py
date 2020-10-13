"""
How I am filtering:

- Remove rows that dont have valid close date
- Remove rows that responded to by a top 8 agency
- Remove rows that has a complaint type differing from the list
- Remove rows that dont have 1 of the 5 major boroughs listed
- Remove rows before 2015
- Remove rows that have negative response times

### currently not touching outliers
- Change outliers to the median (an oulier is +-(8*median), or < 0)

The files produced has the median response times in hours, corresponding to the day

"""

import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys
from datetime import datetime
import statistics as stat

#return a generator, so we dont have to load the whole file in memory
def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            yield row

#2012 and 2016 are leap years
def getDayNumber(year, month, day):
	year = year-2010 #2010 is the first year we have data for
	days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
	day_num = (year*365)
	if((year > 2) or ((year == 2) and (month > 2))): #2012 leap year
		day_num += 1
	if((year > 6) or ((year == 6) and (month > 2))): #2016 leap year
		day_num += 1
	for i in list(range(0,month-1)):
		day_num += days_in_months[i]
	day_num += day
	return(day_num)

def subtractDates(start,end):
	format = '%m/%d/%Y %I:%M:%S %p'
	start_date = datetime.strptime(start, format)
	end_date = datetime.strptime(end, format)
	difference = (end_date-start_date).total_seconds()
	return int(difference)

#366 days in 2012 and 2016, 365 days in 2010, 2011, 2013, 2014, 2015, and 2017. Also using 175 days of 2018
start_day = (366 + 365*4)+1 #+1 bc getting day num starts at 1
total_num_days = (366*2)+(365*6)+175

top_agencies = ['DOHMH','NYPD','DSNY','DEP','DPR','DOB','DOT','HPD']
boroughs = ['MANHATTAN', 'STATEN ISLAND', 'QUEENS', 'BRONX', 'BROOKLYN']
complaints = pd.read_csv('/home/mllab/Desktop/defazio-311/Data/top_complaints.csv')
complaints_list = complaints['Complaint Type'].tolist()

response_times = {x:[] for x in range(start_day,total_num_days+1)}
demands = {x:0 for x in range(start_day,total_num_days+1)}

file_generator = read_csv('/home/mllab/Desktop/defazio-311/Data/new_311.csv')

print("Finding Response Times...")

#Search through all data points
for line in file_generator:
	if(line[1] != 'Created Date'):

		#extract relevant info from data point
		created_date = line[1]
		closed_date = line[2]
		agency = line[3]
		complaint_type = line[5]
		#descriptor = line[6]
		borough = line[25]
		year = int(created_date.split()[0].split('/')[2])

		#ensure none of the required values is missing
		#and year is >= 2015
		if(closed_date != '' and 
			agency in top_agencies and
			complaint_type in complaints_list and
			#descriptor in descriptors_list and
			borough in boroughs 
			and year >= 2015):

			#Data point is valid, find response time
			response_time = int(subtractDates(created_date,closed_date)/3600) #in hours

			#Check if response time is valid
			if(response_time >= 0):

				month = int(created_date.split()[0].split('/')[0])
				day = int(created_date.split()[0].split('/')[1])

				#find day num to populate data structures
				day_num = getDayNumber(year,month,day)
				response_times[day_num].append(response_time)
				demands[day_num] += 1



#now replace each response time list with its median value
print("Finding median response times per day...")

for i in range(start_day,total_num_days+1):
	median = 0
	if(len(response_times[i]) > 0):
		median = stat.median(response_times[i])
	response_times[i] = []
	response_times[i].append(median)



#write to csv
stats_path = '/home/mllab/Desktop/defazio-311/stats/2015_all.txt'
data_path = '/home/mllab/Desktop/defazio-311/Data/'

fh = open(stats_path,"w") #write statistics here


response_times_list = []
demands_list = []

for day_num in sorted(response_times.keys()):
	response_times_list.append(response_times[day_num][0])
	demands_list.append(demands[day_num])

median_response = stat.median(response_times_list)


fh.write("Median response time: " + str(median_response)+'\n')
fh.write("Number of total calls: " + str(sum(demands_list))+'\n')

#change outliers in response and demand to the median
"""median_demand = stat.median(demands)
num_response_outliers = 0
num_demand_outliers = 0
for k in range(0,len(response_times)):
	if((response_times[k] > 8*median_response) or (response_times[k] < 0)):
		response_times[k] = median_response
		num_response_outliers += 1
	if((demands[k] > 8*median_demand) or (demands[k] < 0)):
		demands[k] = median_demand
		num_demand_outliers += 1

fh.write("Response outliers: "+str(num_response_outliers)+'\n')
fh.write("Demand outliers: "+str(num_demand_outliers)+'\n\n')"""


data = pd.DataFrame({'Response_Time':response_times_list, 'Demand':demands_list})

data.to_csv(data_path + '2015_all.csv')

fh.close()