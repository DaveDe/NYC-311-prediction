import numpy as np
import sys
sys.path.append("/home/mllab/Desktop/defazio-311/sgcrfpy-master")
sys.path.append("/home/mllab/Desktop/defazio-311/relevant_models")
from sgcrf import SparseGaussianCRF
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import getSamples as gs

def rmse(y_hat,y):
	#Method 1
	#Get RMSE over each day
	rmse_days = np.sqrt(mean_squared_error(y_hat, y, multioutput='raw_values'))
	#Get average RMSE
	rmse1 = sum(rmse_days)/len(rmse_days)
	rmse1 = round(rmse1,2)
	#Method 2
	#Get sum of squares per day
	sum_of_squares = sum((y_hat - y)**2)
	#sum over days, divide by (num_days * num_samples), take sqrt()
	rmse2 = np.sqrt(sum(sum_of_squares)/(y_hat.shape[1]*y_hat.shape[0]))
	rmse2 = round(rmse2,2)

	rmse_days = rmse_days.tolist()
	rmse_days = [round(x,2) for x in rmse_days]

	return rmse_days,rmse1,rmse2

historical_weeks = 1
predicted_weeks = 1

x_length = historical_weeks*7
y_length = predicted_weeks*7
iterations = 3 #number of GCRF models

locations = ['MANHATTAN', 'STATEN ISLAND', 'QUEENS', 'BRONX', 'BROOKLYN']

data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Location/'
results_path = "/home/mllab/Desktop/defazio-311/Results/location/"+str(historical_weeks)+"_weeks_samples_response.txt"
rmse_day_path = "/home/mllab/Desktop/defazio-311/Results/location/"+str(historical_weeks)+"_weeks_days_response.txt"

fh = open(results_path,"w")
fh2 = open(rmse_day_path,"w")

fh.write("x_length: " + str(x_length) + " y_length: " + str(y_length) + 
	" iterations: " + str(iterations) + "\n")

fh.write("Location, RMSE1, RMSE2\n")
fh2.write("Location, RMSE_1, RMSE_2, RMSE_3, RMSE_4, RMSE_5, RMSE_6, RMSE_7\n")

for location in locations:

	filename = data_path+location+'.csv'
	print("Running for:",location)

	response_times, X_train, Y_train, X_test, Y_test = gs.getSamples(filename, x_length, y_length)

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

	#Get RMSE over each day, and different rmse calculations
	rmse_days,rmse1,rmse2 = rmse(predictions,Y_test)

	fh.write(location + ', ' + str(rmse1) + ', ' + str(rmse2) + '\n')

	fh2.write(location + ', ')
	for r in rmse_days:
		fh2.write(str(r) + ', ')
	fh2.write('\n')

fh.close()
fh2.close()