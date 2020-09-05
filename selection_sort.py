# Selection Sort Algorithm
# Time Complexity ==> Best Case O(N^2), Worst Case O(N^2), Swaps O(N)
# Space Complexity ==> O(1)

def selectionSort(array):

    for i in range(0,len(array)-1):

        min_index = i

        for j in range(i+1,len(array)):

            if array[min_index]<array[j]:

                pass

            else:
                min_index=j

        temp = array[i]
        array[i] = array[min_index]
        array[min_index]= temp

    return array

if __name__ == "__main__":

    array = [5,3,4,21,4,5,-1,56987,-585,-900,89471425]
    sorted_array = selectionSort(array)
    print(sorted_array)