import numpy as np
import sys
sys.path.append("/home/mllab/Desktop/defazio-311/relevant_models")
import matplotlib.pyplot as plt
import getSamples as gs
import pandas as pd

historical_weeks = 2
predicted_weeks = 1

x_length = historical_weeks*7
y_length = predicted_weeks*7

#results_path = "/home/mllab/Desktop/defazio-311/Results/agency/predicted_data2.csv"

#fh = open(results_path,"w")

#fh.write("Predicted1,Real1,Predicted7,Real7\n")
top_agencies = ['DOHMH','NYPD','DSNY','DEP','DPR','DOB','DOT','HPD']

complaints = pd.read_csv('/home/mllab/Desktop/defazio-311/Data/top_complaints.csv')
top_complaints = complaints['Complaint Type'].tolist()
top_complaints = top_complaints[:10]

for i in range(0,len(top_complaints)):
	top_complaints[i] = top_complaints[i].replace('/','_')


locations = ['MANHATTAN', 'STATEN ISLAND', 'QUEENS', 'BRONX', 'BROOKLYN']

for agency in top_agencies:
	data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/'

	filename = data_path + agency +'.csv'

	response_times, X_train, Y_train, X_test, Y_test = gs.getSamples(filename, x_length, y_length)

	num_zeroes = 0
	for i in response_times:
		if(i == 0):
			num_zeroes += 1
	print(agency+':',num_zeroes)
		
for complaint in top_complaints:
	data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Complaint/'

	filename = data_path + complaint +'.csv'

	response_times, X_train, Y_train, X_test, Y_test = gs.getSamples(filename, x_length, y_length)

	num_zeroes = 0
	for i in response_times:
		if(i == 0):
			num_zeroes += 1
	print(complaint+':',num_zeroes)

for location in locations:
	data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Location/'

	filename = data_path + location +'.csv'

	response_times, X_train, Y_train, X_test, Y_test = gs.getSamples(filename, x_length, y_length)

	num_zeroes = 0
	for i in response_times:
		if(i == 0):
			num_zeroes += 1
	print(location+':',num_zeroes)