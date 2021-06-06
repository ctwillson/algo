'''
选择排序
动画来源：https://visualgo.net/en/sorting?slide=8
时间复杂度：O(N*N)
空间复杂度：O(1)
'''
import numpy as np
LENGTH = 10
a = np.random.randint(10,size=LENGTH)
print(a)

def SelSort_demo(arr):
    for L in range(0,LENGTH-1):
        tmp = arr[L]
        pos = L
        for j in range(L,LENGTH):
            if(arr[j] < tmp):
                tmp = arr[j]
                pos = j
        arr[L],arr[pos] = arr[pos],arr[L]
    return arr

def SelSort(arr):
    for L in range(0,LENGTH-1):
        # tmp = arr[L]
        pos = L
        for j in range(L,LENGTH):
            if(arr[j] < arr[pos]):
                # tmp = arr[j]
                pos = j
        if(L != pos):
            arr[L],arr[pos] = arr[pos],arr[L]
    return arr

print(SelSort(a))