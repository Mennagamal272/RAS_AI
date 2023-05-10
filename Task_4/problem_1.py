import statistics as stats
list=[]
n=int(input("enter no of numbers : "))
print("enter numbers ")
for i in range(n):
    list.append(int(input()))
print(f"mean is {stats.mean(list)}")
print(f"median is {stats.median(list)}")
print(f"mode is {stats.mode(list)}")    