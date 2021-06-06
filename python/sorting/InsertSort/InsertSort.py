'''
插入排序
动画来源：https://visualgo.net/en/sorting?slide=9
'''
import numpy as np
LENGTH = 10
a = np.random.randint(10,size=LENGTH)
print(a)
# print(list(range(10,0,-1)))
#后面的元素往前插入
def InsertSort_demo(arr):
    '''
    i 控制从第几个元素开始比较，j控制第几个元素往前比较
    '''
    for i in range(1,LENGTH):
        for j in range(i,0,-1):
            if(arr[j-1] < arr[j]):
                break
            else:
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr

print(InsertSort_demo(a))