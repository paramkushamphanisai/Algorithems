def mergeSort(array):
    #check the length of the array is greater the 1
    if(len(array)>1):
        # calculate the min value which can be taken for spliting the array in two half
        mid=int(len(array)/2)
        #split the array in to two half by taking the mid as reference
        left=array[:mid]
        right=array[mid:]
        #apply the mergSort for the splited array
        mergeSort(left)
        mergeSort(right)
        
        length_left=length_right=length_array=0
        
        #merge the two splited arrays by comparing the two arrays
        while(length_left<len(left) and length_right<len(right)):
            if(left[length_left]<right[length_right]):
                array[length_array]=left[length_left]
                length_left=length_left+1
                length_array=length_array+1
            else:
                array[length_array]=right[length_right]
                length_right=length_right+1
                length_array=length_array+1

        #Add the remmaning left half elements to the array
        while(length_left<len(left)):
            array[length_array]=left[length_left]
            length_left=length_left+1
            length_array=length_array+1

        #Add the remaning right half elements to the array
        while(length_right<len(right)):
            array[length_array]=right[length_right]
            length_right=length_right+1
            length_array=length_array+1
        return array

def quickSort(array):

    #check the length of the array is greater the 2
    length=len(array)
    if(length<2):
        return array
    # take the pivot element as element at 0
    position=pivot=0
    # compare the array with the pivot element and swarp the elements in the array such that element left of it should be less than the pivot and right side greater than the pivot
    for i in range(1,length):
        if array[i]<=array[pivot]:
            position=position+1
            temp=array[i]
            array[i]=array[position]
            array[position]=temp
    #swap the pivot element to its correct location where left side elements are less and right side element are higher
    temp=array[pivot]
    array[pivot]=array[position]
    array[position]=temp
    #split the array in to two half with respective to the position of pivot element
    lsplit=quickSort(array[0:position])
    rsplit=quickSort(array[position+1:length])
    # Combine the splitted arrays
    array=lsplit+[array[position]]+rsplit
    return array
    
