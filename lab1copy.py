import random
import time
from math import ceil as roof

def SortWithFirstNumberAsPivot(List):
    if len(List) <= 1:
        return List
    global Counter
    numberOfPivot = 0
    Pivot = List[0]
    FirstList = []
    SecondList = []
    for i in range(len(List)):
        Counter += 1
        if List[i] < Pivot:
            FirstList.append(List[i])
        elif List[i] > Pivot:
            SecondList.append(List[i])
        else:
            numberOfPivot +=1   #Counts the number that is same as the Pivot
    FirstList = SortWithFirstNumberAsPivot(FirstList)
    SecondList = SortWithFirstNumberAsPivot(SecondList)
    for j in range(numberOfPivot): #Adds as many Pivot as the number of pivot
        FirstList.append(Pivot)
    return FirstList + SecondList

def SortWithRandomPivot(List):
    if len(List) <= 1:
        return List
    Pivot = List[random.randint(0,len(List)-1)] #Chooses one Pivot at random
    global Counter
    numberOfPivot = 0
    FirstList = []
    SecondList = []
    for i in range(0,len(List)):
        Counter += 1
        if List[i] < Pivot:
            FirstList.append(List[i])
        elif List[i] > Pivot:
            SecondList.append(List[i])
        else:
            numberOfPivot +=1   #Counts the number that is same as the Pivot
    FirstList = SortWithRandomPivot(FirstList)
    SecondList = SortWithRandomPivot(SecondList)
    for j in range(numberOfPivot): #Adds as many Pivot as the number of pivot
        FirstList.append(Pivot)
    return FirstList + SecondList

def SortWithMedianPivot(List):
    if len(List) <= 1:
        return List
    FirstPivot=List[0]
    LastPivot=List[len(List) - 1]
    MiddlePivot=List[roof(len(List)/2)]
    #Chooses a pivot point
    if FirstPivot <= MiddlePivot:
        if MiddlePivot <= LastPivot:
            Pivot = MiddlePivot
        elif FirstPivot <= LastPivot:
            Pivot = LastPivot
        else:
            Pivot = FirstPivot
    else:
        if FirstPivot <= LastPivot:
            Pivot = FirstPivot
        elif MiddlePivot <= LastPivot:
            Pivot = LastPivot
        else:
            Pivot = MiddlePivot
    global Counter
    numberOfPivot = 0
    FirstList = []
    SecondList = []
    for i in range(0,len(List)):
        Counter += 1
        if List[i] < Pivot:
            FirstList.append(List[i])
        elif List[i] > Pivot:
            SecondList.append(List[i])
        else:
            numberOfPivot +=1   #Counts the number that is same as the Pivot
    FirstList = SortWithMedianPivot(FirstList)
    SecondList = SortWithMedianPivot(SecondList)
    for j in range(numberOfPivot): #Adds as many Pivot as the number of pivot
        FirstList.append(Pivot)
    return FirstList + SecondList

Unsorted = [random.randint(0,10) for i in range(100)]
Counter = 0

start = time.time()
print("Sort with first number as pivot ",SortWithFirstNumberAsPivot(Unsorted),"\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")
Counter = 0

start = time.time()
print("Sort with random number as pivot ",SortWithRandomPivot(Unsorted),"\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")
Counter = 0

start = time.time()
print("Sort with median number as pivot ",SortWithMedianPivot(Unsorted),"\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")


Unsorted = [random.randint(0,1000) for i in range(10000)]
start = time.time()
print("Sort with first number as pivot ")
SortWithFirstNumberAsPivot(Unsorted)
print("\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")
Counter = 0

start = time.time()
print("Sort with random as pivot ")
SortWithRandomPivot(Unsorted)
print("\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")
Counter = 0

start = time.time()
print("Sort median number as pivot")
sorted = SortWithMedianPivot(Unsorted)
print("\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")

print("---------------------------------------------------------------------------")

Unsorted = sorted + Unsorted

start = time.time()
print("Sort with random as pivot and half sorted")
SortWithRandomPivot(Unsorted)
print("\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")
Counter = 0

start = time.time()
print("Sort median number as pivot and half sorted ")
SortWithMedianPivot(Unsorted)
print("\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")

start = time.time()
print("Sort with first number as pivot and half sorted")
SortWithFirstNumberAsPivot(Unsorted)
print("\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")
Counter = 0
