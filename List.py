#Empty List
emptyList = []
print("Empty List:" ,emptyList)

#Numerical List
numericalList = [9,12,7,4,11,3,8,5,6,10]
print("Numerical List: ", numericalList)

#Mixed Value list
mixedList =["Lily", 14 , "Rossy" , 5.06, False]
print("Mixed List: " ,mixedList)

#Built In functions

#append(val) function
numericalList.append(19)
print("Append List:" ,numericalList)
 
#insert(idx, val) function
numericalList.insert(2, 35)
print("Inserted List: " ,numericalList)

#len(listName) function
numericalList.sort()
print("Sorted List: " ,numericalList)


print("Length of the List: ", len(numericalList))

#Algorith to find Smallest number in the list
def findSmallestNum(numList):
    smallest = numList[0]
    if(len(numList) == 0):
        print("List is empty")
    if(len(numList) == 1):
        return numList[0]
    else:
        for i in range(1, len(numList)):
            if(numList[i] < smallest):
                smallest = numList[i]
    return smallest
print("Smallest number in the list is: ", findSmallestNum(numericalList))

def findLargestNum(numList):
    largest = numList[0]
    if(len(numList) == 0):
        print("List is empty")
    if(len(numList) == 1):
        return numList[0]
    else:
        for i in range(1, len(numList)):
            if(numList[i] > largest):
                largest = numList[i]
    return largest
    return smallest

print("Largest number in the list is:", findLargestNum(numericalList))