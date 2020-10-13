import matplotlib.pyplot as plt
import numpy as np




days = [x for x in range(0,7)]

#top Agencies:
#HPD, DOT, NYPD

#top complaints:
#HEAT/HOT WATER, Noise - Residential, Illegal Parking

#HPD
"""gcrf_response_rmse = [33.39, 36.8, 36.78, 37.15, 38.01, 39.17, 39.44]
gcrf_demand_rmse = [32.41, 35.75, 35.93, 36.29, 37.22, 38.25, 38.4]
linear_regression_rmse = [40.61, 45.09, 45.29, 44.13, 44.02, 45.59, 48.74]"""

#DOT
"""gcrf_response_rmse = [16.09, 16.08, 15.84, 15.94, 15.97, 16.21, 16.22]
gcrf_demand_rmse = [15.18, 15.19, 15.12, 15.33, 15.5, 15.88, 15.92]
linear_regression_rmse = [22.61, 24.87, 24.65, 23.12, 20.89, 19.91, 23.26]"""

#NYPD
"""gcrf_response_rmse = [0.37, 0.37, 0.38, 0.38, 0.38, 0.39, 0.41]
gcrf_demand_rmse = [0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.44]
linear_regression_rmse = [0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.47]"""

#HEAT/HOT WATER
gcrf_response_rmse = []
gcrf_demand_rmse = []
linear_regression_rmse = []

#Noise - Residential
"""gcrf_response_rmse = []
gcrf_demand_rmse = []
linear_regression_rmse = []"""

#Illegal Parking
"""gcrf_response_rmse = []
gcrf_demand_rmse = []
linear_regression_rmse = []"""


plt.plot(days, gcrf_response_rmse)
plt.plot(days, gcrf_demand_rmse)
plt.plot(days, linear_regression_rmse)

plt.xlabel('Day')
plt.xticks(days, ['day 1','day 2','day 3','day 4','day 5','day 6','day 7'])
plt.ylabel('RMSE of predicted response times')
plt.title('NYPD RMSE of predicted response times per day')
plt.legend(['GCRF-Response','GCRF-Response/Demand','Linear Regression'])
plt.savefig('NYPD_comparison.eps')
plt.show()