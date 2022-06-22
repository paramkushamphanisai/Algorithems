
import time

#this function will determine weather the two queens are attacking each other
def noAttack(Chessboard,rows,columns,n):
    #check for the columns where queen is attacking 
    for icol in range(columns):
        if(Chessboard[rows][icol]):
            return 0
    
    #check the diagonals where queen is attacking
    for i,j in zip(range(rows,-1,-1),range(columns,-1,-1)):
        if Chessboard[i][j]:
            return 0
    for i,j in zip(range(rows,n,1),range(columns,-1,-1)):
        if Chessboard[i][j]:
            return 0
    return 1

#This is the backtrack function which used the dfs    
def insertNB_Queens(Chessboard,vertical,n,solution):
    #check if all n queens are placed in the chess board without attacking each other
    if(vertical==n):
        h=[]
        for i in range(0,n):
            for j in range(0,n):
                if Chessboard[i][j]==1:
                    h.append(j+1)
        solution.append(h)
        return 
    for i in range(n):
        #check if the queen at position i,vertical is attacked by other queen
        if noAttack(Chessboard,i,vertical,n)==1:
            #make location i,vertical as 1 and perform the recurssion which same as DFS
            Chessboard[i][vertical]=1
            insertNB_Queens(Chessboard,vertical+1,n,solution)
            Chessboard[i][vertical]=0
    return 
    
            
def B_Queens(n):
    #check for the initial conditions
    if n==1:
        return 1
    if n<4:
        return 0

    solution=[]
    #make the chess board by taking the nxn matrix with zeros at location
    Chessboard=[[0 for j in range(n)]
             for i in range(n)]
    insertNB_Queens(Chessboard,0,n,solution)
    # Solution contains the list of list which has the valuse of queen location.
    # Return the solution list length to get the result
    return (len(solution))


def insertNE_Queens(Chessboard,n,solution):
    #As the broutforce checks all the nodes the loop need to ne of NXN
    for l in range(n):
        i=0
        while(i < n):
            k=0
            j=0
            while(j<n):
                if(noAttack(Chessboard,i,j,n)):
                    Chessboard[i][j]=1
                else:
                    k=k+1
                j=j+1
            if k==n:
                solution.append(False)
            else:
                solution.append(True)
            i=i+1
    return solution

def E_Queens(n):
    #check for the initial conditions
    if n==1:
        return 1
    if n<4:
        return 0
    solution=[]
    Chessboard=[[0 for j in range(n)]
             for i in range(n)]

    insertNE_Queens(Chessboard,n,solution)
    # Solution contains the list of true and false at the queen location valuse of queen location.
    # Return the solution list length to get the result
    return (len(solution))


