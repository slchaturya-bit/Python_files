n = [10,2,0,30,40,50]
mean= sum(n)/len(n)
variance = sum((x-mean)**2 for x in n)/len(n)
print("variance = ",variance)
