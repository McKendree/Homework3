"""Problem 2 from Hwk 3 of ASTR260"""
import matplotlib.pyplot as plt
import numpy as np
import math

if __name__ == "__main__":
    path_to_data = "sensor_position_data.txt"
    oscillator_data = np.loadtxt(path_to_data, skiprows=1, delimiter=',')
    #pulls out the first column (remember things start at 0 in python)
    oscillator_time = oscillator_data[:,0]
    oscillator_pos  = oscillator_data[:,1]

#analytic derivative of oscillator function
def analyticDerivative(t):
    return 0.04*math.pi*math.cos(0.04*math.pi*t)

#computes analytic derivative over range of sensor data with step size 0.01
maxVal = oscillator_time.max()
minVal = oscillator_time.min()
t = 0
analyticDerivList = []
for i in range(int((maxVal-minVal)*100)+1):
    analyticDerivList.append(analyticDerivative(t))
    t = t + 0.01

#returns the forward difference for a value within a dataset
def forwardDifference(dataSet, i):
    return dataSet[i+1]-dataSet[i]

#returns the central difference for a value within a dataset
def centralDifference(dataSet, i):
    numerator = dataSet[i+1]-dataSet[i-1]
    denominator = 2
    return numerator/denominator

#computes forward & central differences for sensor data
fwDiffList = []
centralDiffList =[]
for i in range(len(oscillator_pos)-2):
    fwDiffList.append(forwardDifference(oscillator_pos, i+1))
    centralDiffList.append(centralDifference(oscillator_pos, i+1))

#converts lists to arrays for plotting
analyticDerivArr = np.array(analyticDerivList)
fwDiffArr = np.array(fwDiffList)
centralDiffArr = np.array(centralDiffList)

#plots analytic derivative, forward difference method, and central difference method
plt.plot(oscillator_time, analyticDerivArr, color='blue')
plt.plot(oscillator_time[1:-1], fwDiffArr, color='red', linestyle='dashed', alpha=0.5)
plt.plot(oscillator_time[1:-1], centralDiffArr, color='gold', linestyle='dashed', alpha=0.5)
plt.title('Analytic Derivative, Forward Difference Method, and Central Difference Method')
plt.xlabel('Time (s)')
plt.ylabel('velocity (m)')
plt.legend(['Analytic Derivative','Forward Diff. Method','Central Diff. Method'])
plt.savefig('problem2_2.png')
plt.show()

#returns the forward difference for a value within a dataset using every 100th data point
def forwardDifference2(dataSet, i):
    return (dataSet[i+100]-dataSet[i])/100

#returns the central difference for a value within a dataset using every 100th data point
def centralDifference2(dataSet, i):
    numerator = dataSet[i+100]-dataSet[i-100]
    denominator = 200
    return numerator/denominator

#computes forward and central differences for sensor data using every 100th data point
fwDiffList2 = []
centralDiffList2 = []
for i in range(int(len(oscillator_pos)/100-2)):
    fwDiffList2.append(forwardDifference2(oscillator_pos, 100*i))
    centralDiffList2.append(centralDifference2(oscillator_pos, 100*i))

#plots forward and central difference methods
plt.plot(np.arange(98), fwDiffList2, color='blue')
plt.plot(np.arange(98), centralDiffList2, color='red')
plt.title('Forward and Central Difference Methods')
plt.xlabel('Time (s)')
plt.ylabel('velocity (m)')
plt.legend(['Forward Diff. Method','Central Diff. Method'])
plt.savefig('problem2_4.png')
plt.show()
