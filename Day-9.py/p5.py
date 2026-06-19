#merge two sorted list
def merge_lists(l1,l2):
    i,j=0,0
    res=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<=l2[j]:#i=0,j=0: l1[0]<l2[0],1<2
            res.append(l1[i])
            i+=1
        elif l1[i]>l2[j]:
            res.append(l2[j])
            j+=1
    res.extend(l1[i:])
    res.extend(l2[j:])
    return res
l1=[2,4,6,7,9]
l2=[1,3,5,8]
print(merge_lists(l1,l2))