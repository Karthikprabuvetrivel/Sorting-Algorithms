# Merge Sort Algorithm

# Time Complexity Best Case,Average Case and Worst Case ==> O(NlogN)
# Space Complexity ==> O(N)

def merge(array,left_array,right_array):

    left_index,right_index,array_index=0,0,0

    while left_index<len(left_array) and right_index<len(right_array):

        if left_array[left_index] < right_array[right_index]:

            array[array_index] = left_array[left_index]
            left_index +=1
            array_index+=1

        else:

            array[array_index] = right_array[right_index]
            right_index +=1
            array_index +=1

    while left_index<len(left_array):

        array[array_index] = left_array[left_index]
        left_index +=1
        array_index +=1

    while right_index<len(right_array):

        array[array_index] = right_array[right_index]
        right_index +=1
        array_index +=1


def mergeSort(array):

    if len(array)>1:

        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(array,left,right)

if __name__ == "__main__":

    array = [6,4,3,2,1,100,90,82,72,89,56]

    mergeSort(array)

    print(array)




