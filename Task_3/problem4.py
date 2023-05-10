file=open('dummy_grades.txt','r')
list1=[]
dict={}
for line in file:
    line_strip=line.strip()
    line_split=line.split()
    list1.append(line_split)
file.close()
list2=[]
for i,j in enumerate(list1):
        list2=j
        for i in list2:
              dict[list2[0]]={"name":list2[1],"score":list2[2],"birthday":list2[4],"sex":list2[6]}
print(dict)        
