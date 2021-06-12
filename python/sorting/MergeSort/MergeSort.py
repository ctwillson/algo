'''
归并排序
动画来源：https://visualgo.net/en/sorting?slide=11
该算法自己未完成实现
'''
# import numpy as np
# LENGTH = 10
# a = np.random.randint(10,size=LENGTH)
# print(a)

########### 递归实现 ###############
'''
网络上找的一份，看似可读性高，实则问题很大
'''

#自定义merge函数
def merge(L,R):
    n = len(L) + len(R)
    L.append(float("inf"))
    R.append(float("inf"))
    i = 0
    j = 0
    A = []
    for k in range(0,n): 
        if L[i]<=R[j]:
            A.append(L[i])
            i = i+1
        else:
            A.append(R[j])
            j = j+1
    return A

merge([1,5,6],[2,3])    

#自定义merge_sort函数
def merge_sort(A):
    l = len(A)
    if l<=1:
        return A
    else:
        mid = l//2
        # print(mid)
        # 可读性上升，但是多做了两次拷贝，要是 A 大了，得爆栈...
        left = merge_sort(A[0:mid])
        right = merge_sort(A[mid:])
        return merge(left,right)
#测试merge_sort函数
print(merge_sort([3,2,1,0,5,8,7,2,-5,9,6,11]))


#####  正常的实现方式，可读性较差  #####
'''
arr:需要排序的数组
l:
m:
r:
'''
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)
  
    # 拷贝数据到临时数组 arrays L[] 和 R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # 归并临时数组到 arr[l..r] 
    i = 0     # 初始化第一个子数组的索引
    j = 0     # 初始化第二个子数组的索引
    k = l     # 初始归并子数组的索引
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # 拷贝 L[] 的保留元素
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # 拷贝 R[] 的保留元素
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(arr,l,r): 
    if l < r: 
  
        
        m = int((l+(r-1))/2)
  
       
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r)
  
  
arr = [12, 11, 13, 5, 6, 7] 
n = len(arr) 
print ("给定的数组") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
mergeSort(arr,0,n-1) 
print ("\n\n排序后的数组") 
for i in range(n): 
    print ("%d" %arr[i]),
#############  迭代实现   ###############