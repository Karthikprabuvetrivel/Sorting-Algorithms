# Counting Sort Algorithm (Positive Integers only )
# Time Complexity ==> Worst Case  if k =n O(N), else O(N+K)
# Space Complexity ==> if B is given in the input O(K), else O(N+K)

def countingSort(A):

    max_ = max(A)
    B = [0]*len(A)
    C = [0]*(max_+1)

    # Fillling auxillary array C
    for i in range(0,len(A)):

        C[A[i]] = C[A[i]]+1

    # Cumulative sum of auxillary array C
    for i in range(1,max_+1):

        C[i] = C[i]+C[i-1]

    for i in range(len(A)-1,0,-1):

        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]]-1

    return B

if __name__ == "__main__":

    A = [0,4,5,2,3,89,8,2,3,88,87]
    sorted_array = countingSort(A)
    print(sorted_array)
