import statistics as stats
from math import sqrt
list=[]
sum=0
n=int(input("enter no of numbers : "))
print("enter numbers ")
for i in range(n):
    list.append(int(input()))
    
list.sort()                    #sort list to get min and max
mean = stats.mean(list)        #get mean for variance
for element in list:
    sum+=pow((element-mean),2)     #for variance

variance = sum/n                        #get variance
standard_deviation = sqrt(variance)   #get standard_deviation ,it is equal sqrt of variance 
if n %2 ==0 :                               #to take Q1 and Q3 ,we have to know if no of element odd or even
    Q1=stats.median(list[0:(int)(n/2)-1])          #get Q1
    Q3=stats.median(list[(int)(n/2):n])            #get Q2
else: 
    Q1=stats.median(list[0:(int)(n/2)-1])
    Q3=stats.median(list[(int)(n/2)+1:n])
#print all requ
print(f"min is {list[0]}")
print(f"Q1 is {Q1}")
print(f"Q2 is {stats.median(list)}")
print(f"Q3 is {Q3}")
print(f"max is {list[n-1]}")

print(f"Range is {list[n-1]-list[0]}")
print(f"IQR is {Q3 - Q1}")

print(f"variance is {variance}")    
print(f"Standard deviation is {standard_deviation}") 