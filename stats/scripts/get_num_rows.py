import pandas as pd
import csv


#return a generator, so we dont have to load the whole file in memory
def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            yield row

top_agencies = ['DOHMH','NYPD','DSNY','DEP','DPR','DOB','DOT','HPD']
boroughs = ['MANHATTAN', 'STATEN ISLAND', 'QUEENS', 'BRONX', 'BROOKLYN']
complaints = pd.read_csv('/home/mllab/Desktop/defazio-311/Data/top_complaints.csv')
complaints_list = complaints['Complaint Type'].tolist()

file_generator = read_csv('/home/mllab/Desktop/defazio-311/Data/new_311.csv')

num_rows = 0
num_rows_considered = 0
num_rows_agency = 0
num_rows_complaint = 0
num_rows_after_2015 = 0
no_closed_date_after_2015 = 0
for line in file_generator:
	if(line[1] != 'Created Date'):
		num_rows += 1
		#extract relevant info from data point
		created_date = line[1]
		closed_date = line[2]
		agency = line[3]
		complaint_type = line[5]
		#descriptor = line[6]
		borough = line[25]
		year = int(created_date.split()[0].split('/')[2])

		if(closed_date != '' and 
			agency in top_agencies):
			num_rows_agency += 1

		if(closed_date != '' and 
			complaint_type in complaints_list):
			num_rows_complaint += 1

		if(closed_date == '' and
			year >= 2015):
			no_closed_date_after_2015 += 1

		#ensure none of the required values is missing
		#and year is >= 2015
		if(closed_date != '' and 
			agency in top_agencies and
			complaint_type in complaints_list and
			borough in boroughs and
			year >= 2015):
			num_rows_considered += 1

		if(closed_date != '' and 
			borough in boroughs and
			year >= 2015):
			num_rows_after_2015 += 1


			
stats_path = '/home/mllab/Desktop/defazio-311/stats/num_rows.txt'

fh = open(stats_path,"w") #write statistics here

fh.write("Total number of rows: " + str(num_rows)+'\n')
fh.write("Total number of rows after 2015: " + str(num_rows_after_2015)+'\n')
fh.write("No closed date after 2015: " + str(no_closed_date_after_2015)+'\n')
fh.write("Total number of rows considered: " + str(num_rows_considered)+'\n')
fh.write("Total number of rows in top agency: " + str(num_rows_agency)+'\n')
fh.write("Total number of rows in top complaint: " + str(num_rows_complaint)+'\n')

fh.close()