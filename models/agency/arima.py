import numpy as np
import sys
sys.path.append("/home/mllab/Desktop/defazio-311/relevant_models")
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import getSamples as gs
#from statsmodels.tsa.arima_model import ARIMA
from pyramid.arima import auto_arima

x_length = 14
y_length = 7

top_agencies = ['DOHMH','NYPD','DSNY','DEP','DPR','DOB','DOT','HPD']

data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/'

fh = open("/home/mllab/Desktop/defazio-311/Results/agency/arima.txt","w")

fh.write("x_length: " + str(x_length) + " y_length: " + str(y_length) + "\n")

fh.write("Agency, MSE, MAE, Missed Predictions\n")

#make a best fit line on each test sample (dont even use training data)
for agency in top_agencies:

	filename = data_path + agency + '.csv'

	print("Running for:",agency)
	_, __, ___, X_test, Y_test = gs.getSamples(filename, x_length, y_length)


	all_mse = []
	all_mae = []


	missed_predictions = 0

	for i in range(0, X_test.shape[0]):

		model = auto_arima(X_test[i,:], start_p=5, max_p = 14, error_action="ignore")
		prediction = model.predict(n_periods=3)

		#Arima prediction failed, predict the mean instead
		if(np.isnan(prediction).any()):
			prediction = [X_test[i,:].mean(), X_test[i,:].mean(), X_test[i,:].mean()]
			missed_predictions += 1

		mse = mean_squared_error(prediction, Y_test[i,:].reshape((-1,1)))
		mae = mean_absolute_error(prediction, Y_test[i,:].reshape((-1,1)))
		all_mse.append(mse)
		all_mae.append(mae)


	avg_mse = sum(all_mse)/len(all_mse)
	avg_mae = sum(all_mae)/len(all_mae)

	#round to hundreth
	avg_mse = round(avg_mse,2)
	avg_mae = round(avg_mae,2)

	fh.write(agency + ', ' + str(avg_mse) + ', ' + str(avg_mae) + ', ' + str(missed_predictions) + '\n')

fh.close()