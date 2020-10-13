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

def subtractDates(start,end):
	format = '%m/%d/%Y %I:%M:%S %p'
	start_date = datetime.strptime(start, format)
	end_date = datetime.strptime(end, format)
	difference = (end_date-start_date).total_seconds()
	return int(difference)

#366 days in 2012 and 2016, 365 days in 2010, 2011, 2013, 2014, 2015, and 2017. Also using 175 days of 2018
start_day = 1 # 1 bc getting day num starts at 1
total_num_days = (366*2)+(365*6)+175

#top_agencies = ['DOHMH','NYPD','DSNY','DEP','DPR','DOB','DOT','HPD']
boroughs = ['MANHATTAN', 'STATEN ISLAND', 'QUEENS', 'BRONX', 'BROOKLYN']

location_demand = {location:0 for location in boroughs}


file_generator = read_csv('/home/mllab/Desktop/defazio-311/Data/new_311.csv')

print("Finding Response Times...")

#Search through all data points
for line in file_generator:
	if(line[1] != 'Created Date'):

		#extract relevant info from data point
		created_date = line[1]
		closed_date = line[2]
		borough = line[25]
		year = int(created_date.split()[0].split('/')[2])

		#ensure none of the required values is missing
		#and year is >= 2015
		if(closed_date != '' and 
			borough in boroughs and
			year >= 2015):

			month = int(created_date.split()[0].split('/')[0])
			day = int(created_date.split()[0].split('/')[1])

			response_time = int(subtractDates(created_date,closed_date)/3600) #in hours

			if(response_time >= 0):

				location_demand[borough] += 1

sorted_locations = []
sorted_values = []

#for key, value in sorted(complaint_demand.iteritems(), key=lambda (k,v): (v,k)):
location_demand = [(k, location_demand[k]) for k in sorted(location_demand, key=location_demand.get, reverse=True)]
for key,value in location_demand:
    sorted_locations.append(key)
    sorted_values.append(value)

#write all complaint names/values to file
with open("/home/mllab/Desktop/defazio-311/Data/ordered_locations.csv",'w') as f:
	wr = csv.writer(f)
	wr.writerow(["Location","Demand"])
	for i in range(0,len(sorted_values)):
		wr.writerow([sorted_locations[i],sorted_values[i]])
