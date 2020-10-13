from sklearn.metrics import mean_squared_error
import numpy as np

y_hat = np.array([[1,2],[3,4],[5,6]])
y = np.array([[2,4],[4,6],[6,8]])

#Method 1

#Get RMSE over each day
rmse_days = np.sqrt(mean_squared_error(y_hat, y, multioutput='raw_values'))

#Get average RMSE
avg_rmse = sum(rmse_days)/len(rmse_days)

print("Method 1:",avg_rmse)

#Method 2

#Get sum of squares per day
sum_of_squares = sum((y_hat - y)**2)

#sum over days, divide by (num_days * num_samples), take sqrt()
rmse = np.sqrt(sum(sum_of_squares)/(y_hat.shape[1]*y_hat.shape[0]))

print("Method 2:",rmse)