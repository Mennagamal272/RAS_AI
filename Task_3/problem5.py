from problem4 import dict
def creatfile(dict):
    file=open('busted.txt','w')
    data = str(dict)
    file.write(data)
    
l=len(dict)
list1=[]
for i  in range(l):
    for x,y in dict.items():
        x=list(dict.keys())
        y=list(dict.values())
        list1[0]=x[i]
        list1[1:]=y[j]
print(list1)
creatfile(dict)