num = [10,20,30,40,50]
mean = sum(num)/len(num)
variance = sum((x - mean) ** 2 for x in num) / len(num)
std = variance**0.5
print("Stanadard Deviation = ",std)
