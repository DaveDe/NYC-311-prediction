import numpy as np
import sys
sys.path.append("/home/mllab/Desktop/defazio-311/relevant_models")
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import getSamples as gs
from sklearn import linear_model


historical_weeks = 1
predicted_weeks = 1

x_length = historical_weeks*7
y_length = predicted_weeks*7

top_agencies = ['DOHMH','NYPD','DSNY','DEP','DPR','DOB','DOT','HPD']


data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/'
results_path = "/home/mllab/Desktop/defazio-311/Results/agency/predicted_data2_lr.csv"

fh = open(results_path,"w")

#make a best fit line on each test sample (dont even use training data)
for agency in top_agencies:

	filename = data_path + agency + '.csv'

	print("Running for:",agency)
	_, __, ___, X_test, Y_test = gs.getSamples(filename, x_length, y_length)


	x = [i for i in range(0,x_length)]
	y = [i for i in range(x_length,x_length+y_length)]
	x_days = np.array(x)
	y_days = np.array(y)
	x_days = x_days.reshape((-1,1))
	y_days = y_days.reshape((-1,1))

	predictions = []

	#for each test sample, fit a straight line and calculate the RMSE
	model = linear_model.LinearRegression()
	for i in range(0, X_test.shape[0]):
		model.fit(x_days,X_test[i,:].reshape((-1,1)))
		prediction = model.predict(y_days)
		predictions.append(prediction)


	predictions = np.array(predictions).reshape((-1,y_length))

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
	fh.write(agency+': ')
	for lst in diff:
		final = np.mean(lst)
		final = round(final,2)
		fh.write(str(final) + ', ')
	fh.write('\n')

fh.close()