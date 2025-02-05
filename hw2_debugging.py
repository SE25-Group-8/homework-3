import rand

def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = []
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])
            rightIndex += 1

    while leftIndex < len(leftArr): 
        mergeArr.append(leftArr[leftIndex])
        leftIndex += 1

    while rightIndex < len(rightArr): 
        mergeArr.append(rightArr[rightIndex])
        rightIndex += 1
    
    return mergeArr

arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)


def insertionSort(arr): 
    for i in range (1, len(arr)): 
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key): 
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key 
    
    return arr

arr_2 = rand.random_array([None] * 20) 
arr_2_out = insertionSort(arr)

print(arr_2_out)

