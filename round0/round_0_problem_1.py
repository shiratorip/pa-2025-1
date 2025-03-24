#task: https://sio2.mimuw.edu.pl/c/pa-2025-1/p/zb1/

#THOUGHTS AND PLANNING: 
# 1..i..n 
# Aj = i%j=0  -  Aj creation operation
#  n - max 
#  A1 === 1...n
#  An+1...An+m -operations
#  

#input :
# 1st line - n,m,q
# 2...m+1 - Ai creation operations
# m+2...m+q+1 - questions

#output:
# 1...q - answers
#answers have form of : u ===Ax? 

#SOLUTION:

An=[]
def solve():
    global An
    n,m,q = map(int,input().split())
    #filling A1 array - it consists of all number from 1 to n
    A1 = list(range(1, n+1))
    # preparing An array and filling it with number according to Aj creation operation
    An = [[] for _ in range(n+m+1)]
    for i in range(1,n+1):
        for j in A1:
            if j%i==0:
                An[i].append(j)

    #filling An+m array according to operations from input 
    for i in range(1,m+1):
        operation,x,y = 0 , 0 , 0
        current_input = input().split()
        if len(current_input) == 2:
            operation,x = map(int,current_input)
        elif len(current_input) == 3:
            operation,x,y = map(int,current_input)
        if operation == 1:
            An[n+i]=(aSum(x,y))
        elif operation == 2:
            An[n+i]=(aInter(x,y))
        elif operation == 3:
            An[n+i]=(aNot(x)) 
        elif operation == 0:
            print("ERROR")

    answers = []
    #checking if u is in Ax
    for i in range(1,q+1):
        x,u = map(int,input().split())
        if An[x].count(u) > 0:
            answers.append("TAK")
        else:
            answers.append("NIE")
    return "\n".join(answers)


#sum,intersection, not functions
def aSum(x,y):
    global An
    return list(set(An[x])|set(An[y]))
def aInter(x,y):
    global An
    return list(set(An[x]) & set(An[y]))
def aNot(x):
    global An
    return list(set(An[1]) - set(An[x]))
