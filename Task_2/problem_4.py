list=[]
n=int(input("enter num"))
for i in range(n):
    list.append(input())
print(list)
def remove_duplicates(list):
    noduplictes=[]
    for element in list:
        if element not in noduplictes:
            noduplictes.append(element)
    return noduplictes

print(remove_duplicates(list))

