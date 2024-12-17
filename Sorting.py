def BubbleSort(a_list):
    n = len(a_list)
    for k in range(1, n):
        for i in range(0, n - k):
            if a_list[i] < a_list[i+1]:
                tmp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = tmp
    return a_list

def BubbleSortA(a_list):
    n = len(a_list)
    for k in range(1, n):
        flag = 0
        for i in range(0, n - k):
            if a_list[i] > a_list[i+1]:
                tmp = a_list[i]
                a_list[i] = a_list[i]
                a_list[i+1] = tmp
                flag = 1
        if flag == 0:
            break        
    return a_list

def SelectionSort(a_list):
    n = len(a_list)

    for i in range(0, n-1):
        iMin = i

        for j in range(i+1, n):
            if a_list[j] < a_list[iMin]:
                iMin = j

        temp = a_list[i]
        a_list[i] = a_list[iMin]
        a_list[iMin] = temp

    return a_list        
                                
def InsertionSort(a_list):
    n = len(a_list)

    for i in range(1, n):

        temp = a_list[i]
        hole = i

        while hole>0 and a_list[hole-1]>temp:
            a_list[hole]  = a_list[hole-1]
            hole = hole-1

        a_list[hole] = temp

    return a_list

def MergeSort(a_list):
    n = len(a_list)

    if n < 2:
        return a_list
    
    mid = n // 2
    left = a_list[:mid]
    right = a_list[mid:]

    MergeSort(left)
    MergeSort(right)
    i = 0;   j = 0;   k = 0

    while i < len (left) and j < len(right):
        if left[i] < right [j]:
            a_list[k] = left[i]
            i = i + 1
        else:
            a_list[k] = right[j]
            j = j + 1
        k = k + 1
    
    while i < len(left):
        a_list[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        a_list[k] = right[j]
        j = j + 1
        k = k + 1
    
    return a_list

def QuickSort_partition(a_list, start, end):
    pIndex = start

    pivot = a_list[end]

    for i in range(start, end):
        if a_list[i] <= pivot:
            temp = a_list[i]
            a_list[i] = a_list[pIndex]
            a_list[pIndex] = temp
            pIndex = pIndex + 1
    temp = a_list[pIndex]
    a_list[pIndex] = a_list[end]
    a_list[end] = temp

    return pIndex

def QuickSort(a_list, start, end):
    n = len(a_list)

    if start < end:
        pIndex = QuickSort_partition(a_list, start, end)

        QuickSort(a_list, start, pIndex-1)
        QuickSort(a_list, pIndex+1, end)

    return a_list
