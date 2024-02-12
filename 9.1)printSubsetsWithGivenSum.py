answer=[]
def rec(s,target,sub,i):
    if(i==len(s)):
        if(sum(sub)==target):
            answer.append(sub) 
            return 
        else:
            return 
    rec(s,target,sub+[s[i]],i+1) 
    rec(s,target,sub,i+1)  
rec([1,2,3,4,5,6],6,[],0)  
print(answer) 
