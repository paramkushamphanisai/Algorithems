from collections import defaultdict
import sys
import math

#construct heap to get min edges 
class heap():
    def __init__(self):
        self.mapping=[]
        self.size=0
        self.location=[]
    # push the new edge
    def push(self, v, d):
        return [v, d]
    #construct min heap
    def heapefy(self,index):
        l=index*2+1
        r=index*2+2
        less=index
        if(l < self.size):
            if(self.mapping[l][1]<self.mapping[less][1]):
                less=l
        if(r<self.size):
            if(self.mapping[r][1]<self.mapping[less][1]):
                less=r
        if(less != index):
            self.location[self.mapping[less][0]]=index
            self.location[self.mapping[index][0]]=less
            self.mapping[less],self.mapping[index]=self.mapping[index],self.mapping[less]
            self.heapefy(less)

    #remove the minimum element
    def popmin(self):
        if self.size==0:
            return
        top=self.mapping[0]
        newtop=self.mapping[self.size-1]
        self.mapping[0]=self.mapping[self.size-1]
        
        self.location[newtop[0]]=0
        self.location[top[0]]=self.size-1
        self.size=self.size-1
        self.heapefy(0)
        return top

    #retrive the size
    def getSize(self):
        return self.size
    # check the arrey is free
    def isFree(self):
        if(self.size==0):
            return True
        else:
            return False
    #reduce the key from the key list
    def decreaseKeyList(self,v,dest):
        index=self.location[v]
        self.mapping[index][1]=dest
        
        while index > 0 and self.mapping[index][1] <self.mapping[int((index-1)/2)][1]:
            self.location[self.mapping[index][0]]=int((index-1)/2)
            self.location[self.mapping[int((index-1)/2)][0]]=index
            self.mapping[int((index-1)/2)],self.mapping[index]=self.mapping[index],self.mapping[int((index-1)/2)]
            index=int((index-1)/2)
    #get the position of the graph
    def getlocation(self,v):
        return(self.location[v])
# created the class to execute the prims 
class prims():
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    #insert the edges
    def insertGraph(self,incoming,outgoing,weight):
        self.graph[incoming].insert(0,[outgoing,weight])
        self.graph[outgoing].insert(0,[incoming,weight])
    #construct the minimum spanning tree
    def ConstructPrimsMST(self,g):
        #initialize the veriables 
        v=self.v
        key=[]
        array=[]
        objectMin=heap()
        #set the veriables to the defaut values
        for i in range(v):
            array.append(-1)
            key.append(99999999)
            objectMin.mapping.append(objectMin.push(i,key[i]))
            objectMin.location.append(i)

        objectMin.location[0]=0
        key[0]=0
        array[0]=0
        objectMin.decreaseKeyList(0,key[0])
        objectMin.size=v
        lis=[]
        total=0
        #run the while until the list is empty
        while objectMin.isFree()==False:
            tmp=objectMin.popmin()
            node=tmp[0]
            for move in self.graph[node] :
                vmove=move[0]
                if objectMin.getlocation(vmove) < objectMin.getSize() and move[1] < key[vmove]:
                    
                        if(key[vmove]!=(99999999)):
                            total=total-key[vmove]+move[1]
                        else:
                            total=total+move[1]
                        key[vmove]=move[1]
                        array[vmove]=node
                        lis.append([node,vmove])
                        objectMin.decreaseKeyList(vmove,key[vmove])
        t=(total,lis)
        return t
#return the number of vertex
def getVertex(g):
    V=0
    for i in range(len(g)):
        if(g[i][1]>V):
            V=g[i][1]
    return V
#main method for the prims algorithm
def MST_Prim(g):
    p = prims(len(g))
    for i in range(len(g)):
        p.insertGraph(g[i][0],g[i][1],g[i][2])
    return p.ConstructPrimsMST(g)

#implementation of class for the prims algorithm
class KruskalGraph:

    def __init__(self, v):
        self.V = v
        self.graph = []

    #insert the edge
    def push(self, l, r, w):
        self.graph.append([l, r, w])

    #search the element in the array
    def search(self, array, index):
        if array[index] == index:
            return index
        return self.search(array, array[index])

    #concanat the valuse to keep the record of the used elements
    def concat(self, array, arrrank, x, y):
        xtop = self.search(array, x)
        ytop = self.search(array, y)

        if arrrank[xtop] < arrrank[ytop]:
            array[xtop] = ytop
        elif arrrank[xtop] > arrrank[ytop]:
            array[ytop] = xtop

        else:
            array[ytop] = xtop
            arrrank[xtop] += 1
    # return the tuple which conatins the values sun and list MST_Kruskel
    def Kruskal(self):
        #initilize the veriables
        solution = []
        i = 0
        edge = 0
        self.graph = sorted(self.graph,key=lambda value: value[2])
        array = []
        arrrank = []
        sumi=0
        #assign the default values
        for node in range(self.V):
            array.append(node)
            arrrank.append(0)
        
        #iterate the loop until the vertex -1 times
        while edge < self.V - 1:
            l, r, w = self.graph[i]
            i = i + 1
            x = self.search(array, l)
            y = self.search(array, r)

            #check if the node is previsely visted 
            if x != y:
                edge = edge + 1
                solution.append([l, r])
                sumi=sumi+w
                self.concat(array, arrrank, x, y)

        t=(sumi,solution)
        return t

#main method for the kruskal algorithem 
def MST_Kruskel(g):
    v=getVertex(g)
    p = KruskalGraph(v+1)
    for i in range(len(g)):
        p.push(g[i][0],g[i][1],g[i][2])
    return(p.Kruskal())