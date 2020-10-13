#use same filtering as filter_all_same.py

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

complaints = pd.read_csv('/home/mllab/Desktop/defazio-311/Data/311_Complaint_Types.csv')
complaints_list = complaints['Complaint Type'].tolist()

#top_agencies = ['DOHMH','NYPD','DSNY','DEP','DPR','DOB','DOT','HPD']
boroughs = ['MANHATTAN', 'STATEN ISLAND', 'QUEENS', 'BRONX', 'BROOKLYN']

complaint_demand = {complaint:0 for complaint in complaints_list}

file_generator = read_csv('/home/mllab/Desktop/defazio-311/Data/new_311.csv')

print("Finding Demand per complaint...")

#Search through all data points
for line in file_generator:
	if(line[1] != 'Created Date'):

		#extract relevant info from data point
		created_date = line[1]
		closed_date = line[2]
		#agency = line[3]
		complaint_type = line[5]
		#descriptor = line[6]
		borough = line[25]
		year = int(created_date.split()[0].split('/')[2])

		#ensure none of the required values is missing
		#and year is >= 2015
		if(closed_date != '' and 
			#agency in top_agencies and
			complaint_type in complaints_list and
			#descriptor in descriptors_list and
			borough in boroughs and 
			year >= 2015):

			#Data point is valid, find response time
			response_time = int(subtractDates(created_date,closed_date)/3600) #in hours

			#Check if response time is valid
			if(response_time >= 0):

				#Add call to data structure
				complaint_demand[complaint_type] += 1

sorted_complaints = []
sorted_values = []

#for key, value in sorted(complaint_demand.iteritems(), key=lambda (k,v): (v,k)):
complaint_demand = [(k, complaint_demand[k]) for k in sorted(complaint_demand, key=complaint_demand.get, reverse=True)]
for key,value in complaint_demand:
    sorted_complaints.append(key)
    sorted_values.append(value)

#write all complaint names/values to file
with open("/home/mllab/Desktop/defazio-311/Data/ordered_complaints.csv",'w') as f:
	wr = csv.writer(f)
	wr.writerow(["Complaint Type","Demand"])
	for i in range(0,len(sorted_values)):
		wr.writerow([sorted_complaints[i],sorted_values[i]])