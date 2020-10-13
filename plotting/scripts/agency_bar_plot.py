import matplotlib.pyplot as plt
import numpy as np
import statistics

DEP_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/AllYearsData/DEP.csv'
DOB_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/AllYearsData/DOB.csv'
DOHMH_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/AllYearsData/DOHMH.csv'
DOT_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/AllYearsData/DOT.csv'
DPR_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/AllYearsData/DPR.csv'
DSNY_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/AllYearsData/DSNY.csv'
HPD_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/AllYearsData/HPD.csv'
NYPD_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/AllYearsData/NYPD.csv'

heights = [] #average response time of each agency
errors = []

dep_data = np.genfromtxt(DEP_path, delimiter=',')
dep_response = dep_data[1:,2]
heights.append(sum(dep_response)/len(dep_response))
errors.append(np.std(dep_response))

dob_data = np.genfromtxt(DOB_path, delimiter=',')
dob_response = dob_data[1:,2]
heights.append(sum(dob_response)/len(dob_response))
errors.append(np.std(dob_response))

dohmh_data = np.genfromtxt(DOHMH_path, delimiter=',')
dohmh_response = dohmh_data[1:,2]
heights.append(sum(dohmh_response)/len(dohmh_response))
errors.append(np.std(dohmh_response))

dot_data = np.genfromtxt(DOT_path, delimiter=',')
dot_response = dot_data[1:,2]
heights.append(sum(dot_response)/len(dot_response))
errors.append(np.std(dot_response))

dpr_data = np.genfromtxt(DPR_path, delimiter=',')
dpr_response = dpr_data[1:,2]
heights.append(sum(dpr_response)/len(dpr_response))
errors.append(np.std(dpr_response))

dsny_data = np.genfromtxt(DSNY_path, delimiter=',')
dsny_response = dsny_data[1:,2]
heights.append(sum(dsny_response)/len(dsny_response))
errors.append(np.std(dsny_response))

hpd_data = np.genfromtxt(HPD_path, delimiter=',')
hpd_response = hpd_data[1:,2]
heights.append(sum(hpd_response)/len(hpd_response))
errors.append(np.std(hpd_response))

nypd_data = np.genfromtxt(NYPD_path, delimiter=',')
nypd_response = nypd_data[1:,2]
heights.append(sum(nypd_response)/len(nypd_response))
errors.append(np.std(nypd_response))

print(heights)
print(errors)

x = [x for x in range(0,8)]
#errors = np.array([[0,0,0,0,0,0,0,0,0,0,0,0],errors_list])
plt.bar(x, heights, yerr=errors, align='center')
plt.xticks([0,1,2,3,4,5,6,7], ['DEP','DOB','DOHMH','DOT', 'DPR', 'DSNY', 'HPD', 'NYPD'])
plt.ylabel('Average Median Response Time in Hours')
plt.xlabel('Agency')
plt.title('Average Median Response Times per Agency From 2010 - Present')

plt.savefig('error_bar_agency.eps')
plt.show()
