# Randamized Quick Sort Algorithm
# Time Complexity ==> Best Case O(NlogN), Worst Case O(NlogN)
# Space Complexity ==> O(1)
import random

def partitionSort(array,p,r):

    pivot = array[p]
    i = p
    j = i+1
    while j<=r:

        if pivot<array[j]:
            j +=1
        else:
            i +=1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            j +=1

    temp = array[p]
    array[p] = array[i]
    array[i] = temp

    return i

def randomQuickSort(array,p,r):

    if p<r:
        random_num = random.randint(p+1,r)
        temp = array[p]
        array[p] = array[random_num]
        array[random_num]= temp
        pivot = partitionSort(array,p,r)
        randomQuickSort(array,0,pivot-1)
        randomQuickSort(array,pivot+1,r)

if __name__ == "__main__":

    array = [6,4,3,2,1,100,90,82,72,89,56,77,0,-8,-16,5559,-898756]
    randomQuickSort(array,0,len(array)-1)
    print(array)
    