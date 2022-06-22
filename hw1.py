
def factors(number):
    #Initilize the list fact to store prime factorial
    fact=[]
    #Check the input number is less than 3 and return empty list 
    if(number<=3):
        return []
    #We can use the sqrt function but which is causing issues with the time complexity so, to achive this action we are performing the invers action which is square
    index=2
    while (index*index<=number):
        while(number%index==0):
            fact.append(index)
            number=int(number/index)
        index=index+1
    #As we are stoping the loop when index^2 is less than number,this would be prime factor largest prime factor
    if(number>1):
        fact.append(int(number))
    #Check if the lenght of list fact if the length is one then the number in the input number is prime number so return empty list
    if(len(fact)==1):
        return []
    #return the list of prime factors
    return fact
