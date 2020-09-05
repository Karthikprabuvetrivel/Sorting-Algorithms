# Insertion Sort Algorithm
# Time complexity ==> Best case O(N) and Worsr Case O(N^2) 
# Space Complexity ==> O(1)

def insertionSort(array):

    for current in range(1,len(array)):
        
        while current>0 and array[current-1]>array[current]:

            if array[current-1]<array[current]:
                pass
            else:
                temp = array[current-1]
                array[current-1] = array[current]
                array[current] = temp

            current -=1

    return array
    
if __name__ =="__main__":

    array = [6,4,3,2,1,100,90]

    sorted_array = insertionSort(array)

    print(array)

