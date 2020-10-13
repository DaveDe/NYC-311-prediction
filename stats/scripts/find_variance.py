import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

complaints = pd.read_csv('/home/mllab/Desktop/defazio-311/Data/top_complaints.csv')
top_complaints = complaints['Complaint Type'].tolist()
for i in range(0,len(top_complaints)):
	top_complaints[i] = top_complaints[i].replace('/','_')

data_path = '/home/mllab/Desktop/defazio-311/Data/SameDatapoints/Agency/'

top_agencies = ['DOHMH','NYPD','DSNY','DEP','DPR','DOB','DOT','HPD']
for agency in top_agencies:

	filename = data_path + agency + '.csv'

	data = np.genfromtxt(filename, delimiter=',')

	response_times = data[1:,2]
	#demands = data[1:,1]

	response_times = [x/sum(response_times) for x in response_times]

	variance = np.var(response_times)
	print(agency,variance)


"""
NORMALIZED VARIANCE

HEAT_HOT WATER 6.63609598480929e-08
Noise - Residential 4.3534931260253567e-08
Illegal Parking 3.44338155863819e-08
Blocked Driveway 2.8848948780925922e-08
Street Condition 2.8708329071847243e-07
UNSANITARY CONDITION 7.299306734973239e-08
Water System 3.584400016254488e-07
Street Light Condition 1.6749950639092929e-06
Noise - Street_Sidewalk 8.650267695989676e-08
PAINT_PLASTER 5.740206849753482e-08

VARIANCE

HEAT_HOT WATER 517.7255749358844
Noise - Residential 0.3251749831779681
Illegal Parking 0.3318703685247558
Blocked Driveway 0.33683712373277636
Street Condition 1354.2342149914484
UNSANITARY CONDITION 13134.319769029014
Water System 57.79002916231543
Street Light Condition 1924.2397497030222
Noise - Street_Sidewalk 0.3771295268598482
PAINT_PLASTER 6582.349965427397
Noise 2203.301690374331
PLUMBING 7001.27798291612
Noise - Commercial 0.2883054843847594
Traffic Signal Condition 3.780385975099059
DOOR_WINDOW 11229.793437829048
Sanitation Condition 143.55107119356262
Dirty Conditions 1079.01463934616
WATER LEAK 10847.766132591658
Sewer 78.02949318483313
Missed Collection (All Materials) 432.45091247529314
General Construction_Plumbing 79583.04450456561
Derelict Vehicle 1.604305573524505
Derelict Vehicles 0.1472582409385425
Building_Use 566118.125510619
Sidewalk Condition 14419.963773050209
ELECTRIC 8546.298578840082
GENERAL 14745.847039910463
Noise - Vehicle 0.4263368331000637
FLOORING_STAIRS 14725.889225604647
Rodent 5311.149533780558
Damaged Tree 287086.64994852804
"""