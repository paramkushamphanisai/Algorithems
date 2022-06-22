import copy

class Puzzle:# Define the class named puzzile

    def __init__(self,start,final):# Define the constructor which takes the start and final as input
        self.final =[]
        self.start =[]
        
        self.blankLocation = 0,0#Store the location of the empty state
        #[0,1,...,8]
        k=0
        for i in range(3):# convert the final state to computer readable form
            row=[]
            for j in range(3):
                row.append(final[k])
                k +=1
            self.final.append(row)
        k=0
        for i in range(3):# convert the start state to computer readable form
            row=[]
            for j in range(3):
                row.append(start[k])
                if start[k]==0:
                    self.blankLocation= i, j
                k +=1
            self.start.append(row)


    def isFinal(self):# check if the final state is reached 
        for i in range(3):
            for j in range(3):
                if self.final[i][j] != self.start[i][j]:
                    return False
        return True

    def legalMoves(self):# Check the moves are correct and legal left right and up down
        row,col = self.blankLocation
        legalMoves=[]
        if col!=0:
            legalMoves.append("L")
        if col!=2:
            legalMoves.append("R")
        if row !=0:
            legalMoves.append("U")
        if row!=2:
            legalMoves.append("D")

        return legalMoves

    def resultState(self,move):# retrun the optimal resutl states
        row,col = self.blankLocation
        if move == "U":
            newrow = row-1
            newcol = col
        elif move == "D":
            newrow = row +1
            newcol = col
        elif move == "L":
            newrow = row
            newcol = col-1
        elif move == "R":
            newrow = row
            newcol = col+1
        else:
            raise "illegal move"
        
        tmpPuzzel = Puzzle([0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0])
        tmpPuzzel.start=[value[:] for value in self.start]

        tmpPuzzel.start[row][col]= self.start[newrow][newcol]
        tmpPuzzel.start[newrow][newcol]=self.start[row][col]
        tmpPuzzel.final=[value[:] for value in self.final]

        tmpPuzzel.final=self.final

        tmpPuzzel.blankLocation = newrow, newcol

        return tmpPuzzel

    def __eq__(self, other):
        for row in range(3):
            if self.start[row]!= other.start[row]:
                return False
        return True

class Queue:
    def __init__(self):
        self.list =[]
    def enque(self, item):
        self.list.insert(0,item)
    def deque(self):
        return self.list.pop()
    def isEmpty(self):
        return len(self.list)==0

class SearchProblem:# create the class to retrive the data while BFS
    def __init__(self,state):
        self.puzzel = state

    def getStartState(self):#return the stastics
        return self.puzzel

    def getSuccessors(self,state):# get the leagel successors nodes
        succes=[]
        for move in state.legalMoves():
            currentState = state.resultState(move)
            succes.append((currentState,move))
        return succes

    def isFinalState(self, state):
        return state.isFinal()

def PathBFS(problem):#perform the BFS
    count=0
    action = ""
    fPath =[]
    visited=[]
    state = problem.getStartState()
    queue = Queue()
    queue.enque(((state,action),fPath))#insert the element into the queue


    while ~queue.isEmpty() and count<1000:# run the while condition until the que is empty or count reaches to 1000
        count=count+1
        current = queue.deque()
        currentStatewithAction = current[0]
        currentPath = current[1]
        currentState = currentStatewithAction[0]

        if currentState in visited:# continue if the currentState is present in the visited list
            continue
        else:
            visited.append(currentState)

        if problem.isFinalState(currentState):
            return currentPath
        else:
            succs = problem.getSuccessors(currentState)
            for succ in succs:
                sPath = copy.deepcopy(currentPath)
                if succ[0] in visited:
                    continue
                else:
                    sPath.append(succ[1])
                    queue.enque((succ,sPath))
    return currentPath



def ShortestPath(start,goal):# find the shortest path to reach the goal node
    solution=[]
    length=len(goal)#find the length of the goal node
    for i in range(length):
        if len(start)==len(goal[i]):# perform the initial evaluation
            puzzle=Puzzle(start,goal[i])
            p=SearchProblem(puzzle)
            path = PathBFS(p)#call the BFS to retrive the path
            solution.append(len(path))
    return(solution)