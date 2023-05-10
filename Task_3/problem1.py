def even(list1):
    count=0
    for element in list1:
        if element %2 == 0:
            count+=1
    return count

list = [5,7,7,8,8,8,10] 
count=even(list)
printcount = lambda count : f"no of even numbers = {count}"
print(printcount(count))

