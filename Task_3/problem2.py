def index(list1,target1):         
    for i in range(len(list1)):        # function to return the index of the target
        if list1[i]==target1:          # find the target,return the index
            return i
        else:                          # doesn't find the target,sort the list
            list1.sort()
            for i in range(len(list1)):
                if list1[i]<target1 and list1[i+1]>target1:  #return the index of the target if it would be inserted
                    return (i+1)
list = [4,2,3,1,7]
target=5
print(f"index = {index(list,target)}")
