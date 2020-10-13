import matplotlib.pyplot as plt
import numpy as np
import statistics

data_path = '/home/mllab/Desktop/defazio-311/Data/all.csv'
#data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/DEP.csv'

data = np.genfromtxt(data_path, delimiter=',')

response_times = data[1:,2]
demands = data[1:,1]

#January 1st 2010 was a Friday
#heights: [Friday, Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday]
days = [x for x in range(0,7)]
heights = [[] for x in range(0,7)]
day_index = 0
for i in range(0,response_times.size):
	heights[day_index].append(response_times[i])
	day_index += 1
	if(day_index == 7):
		day_index = 0

errors = [[] for x in range(0,7)]

#find average of day values as height
#find std for errors
for i,day_bucket in enumerate(heights):
	heights[i] = (sum(day_bucket)/len(day_bucket))
	errors[i] = np.std(day_bucket)


print(heights)
print(errors)

#errors = np.array([[0,0,0,0,0,0,0,0,0,0,0,0],errors_list])
plt.bar(days, heights, yerr=errors, align='center')
plt.xticks([0,1,2,3,4,5,6], ['Fri','Sat','Sun','Mon', 'Tues', 'Wed', 'Thur'])
plt.ylabel('Average Median Response Time in Hours')
plt.xlabel('Day')
plt.title('Average Median Response Times per Day From 2010 - Present')

plt.savefig('error_bar_day.eps')
plt.show()
