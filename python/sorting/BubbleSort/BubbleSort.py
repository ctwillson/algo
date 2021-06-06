'''
动画来源：https://visualgo.net/en/sorting?slide=7
时间复杂度：O(N*N)
不管冒泡排序的时间复杂度如何，需要比较的次数为 0+1+2+......+(n-1)
'''
import numpy as np
LENGTH = 10
a = np.random.randint(10,size=LENGTH)
print(a)
length = LENGTH - 1
def bubblesort_demo(arr):
    while True:
        for index in range(0,length - 1):
            if index == LENGTH:
                break
            if arr[index] > arr[index+1]:
                arr[index + 1],arr[index] = arr[index],arr[index + 1]

        # print(a)
        length = length - 1
        if length == 0:
            break
    return arr

def bubblesort(arr):

    for i in range(0,LENGTH):
        for j in range(0,LENGTH-i-1):
            if arr[j] > arr[j+1]:
                arr[j + 1],arr[j] = arr[j],arr[j + 1]
    return arr
print(bubblesort(a))