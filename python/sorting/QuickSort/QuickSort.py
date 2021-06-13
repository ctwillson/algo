def partition(arr,l,r):
    i = l
    j = r
    x= arr[i]
    while(i < j):
        ### 查找最右边第一个比 pivot 小的 index，注意等号
        while(i < j and arr[j] >= x):
            j -= 1
        arr[i] = arr[j]
        ### 查找最左边第一个比 pivot 大的 index，注意等号
        while(i < j and arr[i] <= x):
            i += 1
        arr[j] = arr[i]

        # if(arr[j] < x):
        #     arr[i] = arr[j]
        #     i += 1
        # else:
        #     j -= 1
    # 在做 partition 的时候，记得把 pivot 元素插回
    arr[i] = x
    return i
def QuickSort(arr,l,r):
    if(l < r):
        m = partition(arr,l,r)
        QuickSort(arr,l,m-1)
        QuickSort(arr,m+1,r)

arr = [12, 13, 11, 5, 5, 7]
QuickSort(arr,0,len(arr)-1)
print(arr)