import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

#UNSANITARY CONDITION
#HEAT_HOT WATER
#Blocked Driveway
#Street Light Condition --  very correlated
#data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Complaint/Water System.csv'
#data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/DEP.csv'
data_path = '/home/mllab/Desktop/defazio-311/Results/complaint/predicted_data_water.csv'
data = np.genfromtxt(data_path, delimiter=',')

#response_times = data[1:,2]
#demands = data[1:,1]

predicted1 = data[1:,0]
real1 = data[1:,1]

#response_times = [x/sum(response_times) for x in response_times]
#demands = [x/sum(demands) for x in demands]

#cor = np.corrcoef(response_times,demands)
#print(cor)

days = [x for x in range(0,298)]
#days = [x for x in range(0,57)]

plt.plot(days, real1)
plt.plot(days, predicted1)#, color='orange'
plt.xlabel('Day')
#plt.xticks([0,365,730,1096,1461,1826,2191,2557,2922], ['2010','2011','2012','2013','2014','2015','2016','2017','2018'])
#plt.ylabel('Response time (in hours)')
#plt.title('Median Response Time per Day from 2010 - Present')

#plt.savefig('line_smoothed.eps')
plt.show()