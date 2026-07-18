# mean
marks = [10,20,30,40,50,20,20,30]
mean = sum(marks)/len(marks)
print("Mean =",mean)

# meadian
marks.sort()
n = len(marks)
if (n%2==0):
   median =( marks[n//2-1] + marks[n//2])
else:
  median = marks[n//2]
    
print("median=",median)

#mode
mode = max(set(marks),key=marks.count)
print("Mode =",mode)

# variance
variance = sum((x-mean)**2 for x in marks)/len(marks)
print("Variance =",variance)

# standard deviation
standard_deviation = variance*0.5
print("Standard deviation = ",standard_deviation)


# mean ,median, mode, using statistics library
import statistics
data = list(map(float, input("Enter numbers separated by space : ").split()))
Mean = statistics.mean(data)
Median = statistics.median(data)
try:
    mode = statistics.mode(data)
except statistics.StatisticsError:
    mode = "No unique mode"

Variance = statistics.pvariance(data)
Std_dev = statistics.pstdev(data)

print(Mean)
print(Median)
print(mode)
print(Variance)
print(Std_dev)
