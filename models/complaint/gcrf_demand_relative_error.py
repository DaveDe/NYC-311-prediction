import numpy as np
import sys
sys.path.append("/home/mllab/Desktop/defazio-311/sgcrfpy-master")
sys.path.append("/home/mllab/Desktop/defazio-311/relevant_models")
from sgcrf import SparseGaussianCRF
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import getSamples as gs
import pandas as pd

historical_weeks = 2
predicted_weeks = 1

x_length = historical_weeks*7
y_length = predicted_weeks*7
iterations = 3 #number of GCRF models


data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Complaint/'
results_path = "/home/mllab/Desktop/defazio-311/Results/complaint/predicted_data2_demand.csv"

fh = open(results_path,"w")

#fh.write("Predicted1,Real1,Predicted7,Real7\n")

complaints = pd.read_csv('/home/mllab/Desktop/defazio-311/Data/top_complaints.csv')
top_complaints = complaints['Complaint Type'].tolist()
top_complaints = top_complaints[:10]

for i in range(0,len(top_complaints)):
	top_complaints[i] = top_complaints[i].replace('/','_')

for complaint in top_complaints:

	filename = data_path + complaint +'.csv'

	response_times, X_train, Y_train, X_test, Y_test = gs.getSamplesWithDemand(filename, x_length, y_length)

	#remove demand from Y_train and Y_test (only predict response time)
	Y_train = Y_train[:,0::2]
	Y_test = Y_test[:,0::2]

	model = SparseGaussianCRF(lamL=0.1, lamT=0.1, n_iter=10000) #lamL and lamT are regularization parameters

	predictions = []

	#run the model a few times and store predictions
	for i in range(0,iterations):

		model.fit(X_train, Y_train)
		prediction = model.predict(X_test)
		predictions.append(prediction)

	predictions = np.array(predictions)

	#average different GCRF's predictions
	predictions = np.mean(predictions, axis=0)


	diff = [[] for x in range(0,y_length)]

	#predictions is predicted, Y_test is real
	#find % differences for each day
	for i in range(0,predictions.shape[0]):
		for j in range(0,predictions.shape[1]):
			if(Y_test[i,j] != 0):
				temp = np.abs(predictions[i,j] - Y_test[i,j])/Y_test[i,j]
			#temp = 2*(predictions[i,j] - Y_test[i,j])/(np.abs(predictions[i,j]) + np.abs(Y_test[i,j]))
				diff[j].append(temp)

	final = 0
	#Average the % differences
	fh.write(complaint+': ')
	for lst in diff:
		final = np.mean(lst)
		final = round(final,2)
		fh.write(str(final) + ', ')
	fh.write('\n')

fh.close()