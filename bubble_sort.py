# Bubble Sort Algorithm

# Time Complexity ==> Best Case 0(N), Worse Case O(N^2)
# Space Comnplecity ==> O(1)


def bubbleSort(array):

    for i in range(0,len(array)):

        for j in range(0,len(array)-i-1):

            if array[j]<array[j+1]:
                pass
            else:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return array

if __name__ == "__main__":

    array=[6,4,3,2,1,100,90,82,72,89,56]
    sorted_array = bubbleSort(array)
    print(sorted_array)
