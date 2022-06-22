
def getMinimum(a,b,c):
    if(a<b and a<c):
        return a
    elif (b<c):
        return b
    else:
        return c
def MakeAnArray(a,b):
    array=[[0 for x in range(b)] for y in range(a)]
    return array

def editDistance(sourceString,resutltString):
    #concad the special character to the string
    sourceString="#"+sourceString
    resutltString="#"+resutltString

    #Make the source string in to list for the easy access
    sourceString=[i for i in sourceString]
    resutltString=[i for i in resutltString]

    #get the length of the strings
    lens=len(sourceString)
    lend=len(resutltString)
    #create an 2d arreay with the size of the length source and destination strngs
    array=MakeAnArray(lens,lend)

    print(array)
    #make the first row as zeros
    array[0]=[i for i in range(lend)]
    #make the first colmon as zero
    for i in range(lens):
        array[i][0]=i
    print(array)

    for i in range(1, lend):
        for j in range(1,lens):
            #compare the source and sestination strings and update the 2d array values
            if(resutltString[i]!=sourceString[j]):
                #print(array[j-1,i],array[j,i-1],array[j-1][i-1],minimum(array[j-1][i],array[j][i-1],array[j-1][i-1]))
                array[j][i]=getMinimum(array[j-1][i],array[j][i-1],array[j-1][i-1])+1
            else:
                array[j][i]=array[j-1][i-1]
    return(array[-1][-1])


print(editDistance("BABBLE","APPLE"))
