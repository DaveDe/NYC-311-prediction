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
start_day = (366 + 365*4)+1 # +1 bc getting day num starts at 1
total_num_days = (366*2)+(365*6)+175
num_weeks = int((total_num_days-start_day)/7)
weeks_per_step = 1

top_agencies = ['DOHMH','NYPD','DSNY','DEP','DPR','DOB','DOT','HPD']
boroughs = ['MANHATTAN', 'STATEN ISLAND', 'QUEENS', 'BRONX', 'BROOKLYN']

#Complaints
complaints = pd.read_csv('/home/mllab/Desktop/defazio-311/Data/top_complaints.csv')
top_complaints = complaints['Complaint Type'].tolist()

#Complaints
complaints = pd.read_csv('/home/mllab/Desktop/defazio-311/Data/311_Complaint_Types.csv')
complaints_list = complaints['Complaint Type'].tolist()

complaint_occurence = {complaint:{x:0 for x in range(0,num_weeks+1,weeks_per_step)} for complaint in complaints_list}
sum_of_complaints = {x:0 for x in range(0,num_weeks+1,weeks_per_step)}

file_generator = read_csv('/home/mllab/Desktop/defazio-311/Data/new_311.csv')

print("Finding Complaints per week...")

#Search through all data points
for line in file_generator:
	if(line[1] != 'Created Date'):

		#extract relevant info from data point
		created_date = line[1]
		closed_date = line[2]
		agency = line[3]
		complaint = line[5]
		borough = line[25]
		year = int(created_date.split()[0].split('/')[2])

		#ensure none of the required values is missing
		#and year is >= 2015
		if(closed_date != '' and 
			agency in top_agencies and
			complaint in complaints_list and
			#descriptor in descriptors_list and
			borough in boroughs and 
			year >= 2015):

			#Data point is valid, find response time
			response_time = int(subtractDates(created_date,closed_date)/3600) #in hours

			#Check if response time is valid
			if(response_time >= 0):

				month = int(created_date.split()[0].split('/')[0])
				day = int(created_date.split()[0].split('/')[1])

				#Find which week this day belongs to
				day_num = getDayNumber(year,month,day)
				week_num = int((day_num-start_day)/7)
				week_index = 0
				if(week_num%weeks_per_step != 0):
					week_index = (week_num - (week_num%weeks_per_step))
				else:
					week_index = week_num

				#add complaint to appropriate bucket
				complaint_occurence[complaint][week_index] += 1
				sum_of_complaints[week_index] += 1


print("Calculating proportion of each complaint per week")
#Now find the % of each complaint type at each week index
for complaint in complaints_list:
	for i in range(0,num_weeks,weeks_per_step):
		complaint_occurence[complaint][i] = round(complaint_occurence[complaint][i]/sum_of_complaints[i],3)


print("Writing to file...")

path = "/home/mllab/Desktop/defazio-311/stats/complaint_per_week_frequency.txt"
fh = open(path,"w")
fh.write("Complaint Type")
for i in range(0,num_weeks,weeks_per_step):
	fh.write("\tWeek"+str(i))
fh.write("\tSum\n")

for complaint in complaints_list:
	if(complaint in top_complaints):
		_sum = 0
		fh.write(complaint)
		for i in range(0,num_weeks,weeks_per_step):
			_sum += complaint_occurence[complaint][i]
			fh.write("\t"+str(complaint_occurence[complaint][i]))
		_sum = round(_sum,3)
		fh.write("\t"+str(_sum)+"\n")
fh.close()


