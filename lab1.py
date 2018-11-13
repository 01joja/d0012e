import random
import time
from math import ceil as roof

Unsorted = [random.randint(0,1000) for i in range(1000)]
Counter = 0

def SortWithFirstNumberAsPivot(List):
    if len(List) <= 1:
        return List
    global Counter
    Pivot = List[0]
    FirstList = []
    SecondList = []
    for i in range(1,len(List)):
        Counter += 1
        if List[i] <= Pivot:
            FirstList.append(List[i])
        else:
            SecondList.append(List[i])
    FirstList = SortWithFirstNumberAsPivot(FirstList)
    SecondList = SortWithFirstNumberAsPivot(SecondList)
    FirstList.append(Pivot)
    return FirstList + SecondList

start = time.time()
print("Sort with first number as pivot ",SortWithFirstNumberAsPivot(Unsorted),"\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")
Counter = 0

def SortWithRandomPivot(List):
    if len(List) <= 1:
        return List
    global Counter
    Pivot = List[random.randint(0,len(List)-1)]
    FirstList = []
    SecondList = []
    for i in range(0,len(List)):
        Counter += 1
        if List[i] <= Pivot:
            FirstList.append(List[i])
        else:
            SecondList.append(List[i])
    FirstList = SortWithRandomPivot(FirstList)
    SecondList = SortWithRandomPivot(SecondList)
    FirstList.append(Pivot)
    return FirstList + SecondList

start = time.time()
print("Sort with random number as pivot ",SortWithRandomPivot(Unsorted),"\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")
Counter = 0


def SortWithMedianPivot(List):
    if len(List) <= 1:
        return List
    FirstPivot=List[0]
    LastPivot=List[len(List) - 1]
    MiddlePivot=List[roof(len(List)/2)]
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
    FirstList = []
    SecondList = []
    for i in range(0,len(List)):
    Counter += 1
        if List[i] <= Pivot:
            FirstList.append(List[i])
        else:
            SecondList.append(List[i])
    FirstList = SortWithMedianPivot(FirstList)
    SecondList = SortWithMedianPivot(SecondList)
    FirstList.append(Pivot)
    return FirstList + SecondList

start = time.time()
print("Sort with random number as pivot ",SortWithMedianPivot(Unsorted),"\nNumber of runns",Counter,"\n")
end = time.time()
print("Time passed: ", end-start,"\n\n")
