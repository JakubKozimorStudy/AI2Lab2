print([x+x+1 for x in [0,1,2,3]])
print([x%3==0 for x in [3,5,9,8]])
print([x[3:-1]+x[-1] for x in ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"] if x[0]=="T" and x[1]=="A"])
print([x[0].upper() for x in ['apple', 'orange', 'pear']])
print([x for x in ['apple', 'orange', 'pear'] if x[0]=="a"or x[0]=="p"])
print([[x,x.__len__()] for x in ['apple', 'orange', 'pear']])

arr={}
for x in ['apple', 'orange', 'pear']:
    arr[x]=arr.get(x,x.__len__())
print(arr)