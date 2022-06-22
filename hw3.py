
import sys
sys.setrecursionlimit(1500)
def MaxHeap(array,length,index):
    #initilize the maxi value index
    maxi=index
    # Compute the values for left and right child elements
    left=2*index+1
    right=2*index+2
    # check the max element of left and right element
    if left < length:
        if array[left]>array[maxi]:
            maxi=left
    if right < length:
        if array[right]>array[maxi]:
            maxi=right
    # Swap the max element and element at the current index of the array if index is not with max element
    if maxi!=index:
        tmp=array[maxi]
        array[maxi]=array[index]
        array[index]=tmp
        MaxHeap(array,length,maxi)

def BuildMaxHeap(array,length):
    #construct the max heap first max element
    n=length//2-1
    for index in range(n,-1,-1):
        MaxHeap(array,length,index)
    m=length-1
    #construct the max heap for the second max elements
    for indexi in range(m,0,-1):
        tmp=array[0]
        array[0]=array[indexi]
        array[indexi]=tmp
        MaxHeap(array,indexi,0)
    return array

def HeapSort(array):
    #Calculate the lengeth of the array
    length=len(array)
    #this function will build the heap and remove the max element for all elements in the array and return sorted array
    array=BuildMaxHeap(array,length)
    return array

