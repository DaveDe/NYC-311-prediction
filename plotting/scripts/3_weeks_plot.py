import matplotlib.pyplot as plt
import numpy as np

#data_path = '/home/mllab/Desktop/defazio-311/Data/2015_all.csv'
data_path = '/home/mllab/Desktop/defazio-311/Data/2015_all.csv'

data = np.genfromtxt(data_path, delimiter=',')

response_times = data[1:,2]

response_times = response_times[:21]

print(response_times)

days = [x for x in range(0,21)]

plt.figure(figsize=(9,4))
plt.plot(days, response_times)
#plt.plot(days, demands)#, color='orange'
plt.xlabel('Day')
plt.xticks(days)
plt.ylabel('Response time (in hours)')
plt.title('Median Response Time per Day From Jan 1st 2015 - Jan 21st 2015')
plt.savefig('3_weeks.eps')
plt.show()