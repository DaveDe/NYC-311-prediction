import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

data_path = '/home/mllab/Desktop/defazio-311/Data/all.csv'
#data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/DEP.csv'

data = np.genfromtxt(data_path, delimiter=',')

response_times = data[1:,2]
demands = data[1:,1]

#2012 and 2016 are leap years

#Day indexes to years:
#2010 - 0:365
#2011 - 365:730
#2012 - 730:1096
#2013 - 1096:1461
#2014 - 1461:1826
#2015 - 1826:2191
#2016 - 2191:2557
#2017 - 2557:2922
#2018 - 2922:3097

#response_times = response_times[:365]


days = [x for x in range(0,3097)]

response_smoothed = savgol_filter(response_times, 51, 3) # window size 51, polynomial order 3

response_smoothed = [round(x,2) for x in response_smoothed]

fh = open("line_smoothed.txt","w")
for i in response_smoothed:
	fh.write(str(i)+',')
fh.close()
#np.savetxt('line_smoothed.txt', response_smoothed, delimiter=',')

plt.plot(days, response_smoothed)
#plt.plot(days, demands)#, color='orange'
plt.xlabel('Day')
plt.xticks([0,365,730,1096,1461,1826,2191,2557,2922], ['2010','2011','2012','2013','2014','2015','2016','2017','2018'])
plt.ylabel('Response time (in hours)')
plt.title('Median Response Time per Day from 2010 - Present')

plt.savefig('line_smoothed.eps')
plt.show()