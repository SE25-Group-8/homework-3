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

test_1_rg = [4, 1, 5, 3, 2]
test_2_rg = ["cat", "apple", "boat", "track", "rope"]
test_3_rg = [6.7, 3.2, 4.5, 0.4, 1.3]

test_1_rg_out = mergeSort(test_1_rg)
test_2_rg_out = mergeSort(test_2_rg)
test_3_rg_out= mergeSort(test_3_rg)

print("MERGESORT: ")
print(arr_out)
print(test_1_rg_out)
print(test_2_rg_out)
print(test_3_rg_out)
print("")

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

print("INSERTION SORT: ")
print(arr_2_out)

