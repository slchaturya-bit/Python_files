import statistics 
data = list(map(float,input("Enter numbers separated by space:").split()))
print("Mean =", statistics.mean(data))
print("Median =", statistics.median(data))
print("Mode =", statistics.mode(data))
print("Variance =", statistics.variance(data))
print("Standard Deviation =", statistics.stdev(data))