str="abcbbac"
longest=""
for i in range(len(str)):
    current="" 
    for j in range(i,len(str)):
        if str[j] in current:
            break
        current=current+str[j]
    if len(current)>len(longest):
        longest=current
print(longest)            






    

       

