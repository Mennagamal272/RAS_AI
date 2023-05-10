def target(list,target1):
    intgers=[]
    for i in range(len(list)):
        for j in range(i,len(list)):
            for k in range(j,len(list)):
                 for f in range(k,len(list)):
                        if list[i]!= list[j]!= list[k] != list[f] and (list[i]+list[j]+list[k]+list[f] == target1 or list[i]+list[j]+list[k]+list[f] > int(.9*target1)):
                                    intgers.append(list[i])
                                    intgers.append(list[j])
                                    intgers.append(list[k])
                                    intgers.append(list[f]) 
                                    return print(intgers)
list=[4,2,3,1,7,7,12]
target1=28
target(list,target1)


          



                