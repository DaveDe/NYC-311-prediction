import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

complaints = pd.read_csv('/home/mllab/Desktop/defazio-311/Data/top_complaints.csv')
complaints_list = complaints['Complaint Type'].tolist()

#boroughs = ['MANHATTAN', 'STATEN ISLAND', 'QUEENS', 'BRONX', 'BROOKLYN']

for complaint in complaints_list:

	complaint = complaint.replace('/','_')

	data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Complaint/' + complaint + '.csv'

	data = np.genfromtxt(data_path, delimiter=',')

	response_times = data[1:,2]
	#demands = data[1:,1]

	std = np.std(response_times)
	print(complaint,std)