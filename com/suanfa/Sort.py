import copy
import datetime
import random

def myInsertSort(a):
    n=len(a)
    if n<=1:
        return a
    for i in range(1,n):
        j=i;
        while j>0 and a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
            j=j-1

def InsertSort2(lst):
    n=len(lst)
    if n<=1:
        return lst
    for i in range(1,n):
        j=i
        target=lst[i]            #每次循环的一个待插入的数
        while j>0 and target<lst[j-1]:       #比较、后移，给target腾位置
            lst[j]=lst[j-1]
            j=j-1
        lst[j]=target            #把target插到空位

def insertSort3(arr):
    if len(arr)<=1:
        return
    for i in range(1,len(arr)):
        j=i
        for j in range(j,0,-1):
            if arr[j]<arr[j-1]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break


def insertSort(arr):
    if len(arr)<=1 :
        return
    for j in range(1,len(arr)):
        for i in  range(j,0,-1):
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
            else:
                break

def insertSort1(arr):
    length = len(arr)
    for i in range(1,length):
        x = arr[i]
        for j in range(i,-1,-1):
            # j为当前位置，试探j-1位置
            if x < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                # 位置确定为j
                break
        arr[j] = x


def insert_sort(alist):
    n = len(alist)
    for j in range(0, n):
        for i in range(j, 0, -1):
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break
    return alist


def merge(left, right):
    c=[]
    h=j=0
    while j<len(left) and h<len(right):
        if left[j]<right[h]:
            c.append(left[j])
            j+=1
        else:
            c.append(right[h])
            h+=1
    if j==len(left):
        c.extend(right[h:])
    else:
        c.extend(left[j:])
    return c


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    middle=len(arr)//2
    left=merge_sort(arr[:middle])
    right=merge_sort(arr[middle:])
    return merge(left,right)


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    less=[]
    greater=[]
    base=arr.pop()
    for x in arr:
        if x<base:
            less.append(x)
        else:
            greater.append(x)
    return quick_sort(less)+[base]+quick_sort(greater)


def quick_sort2(arr):
    if len(arr)<=1:
        return arr
    base=arr[0]
    left=[x for x in arr[1:] if x<=base]
    right=[x for x in arr[1:] if x >base]
    return quick_sort2(left)+[base]+quick_sort2(right)



#快速排序，原地排序
def quick_sort3(L):
    return q_sort(L,0,len(L)-1)
def q_sort(L,left,right):
    if left<right:
        pivot=partition(L,left,right)
        q_sort(L,left,pivot-1)
        q_sort(L,pivot+1,right)
    return L


def partition(L,left,right):
    pivotKey=L[left]
    while left<right:
        while left<right and L[right]>=pivotKey:
            right-=1;
        L[left]=L[right]
        while left<right and L[left]<pivotKey:
            left+=1
        L[right]=L[left]
    L[left]=pivotKey
    return left

def shellSort(arr):
    d=len(arr)
    while d>1:
        d=d//2
        for i in range(d):
            for j in range(i+d,len(arr),d):
                for k in range(j-d,-1,-d):
                    if arr[k]>arr[j]:
                       arr[k],arr[j]=arr[j],arr[k]
                       print(arr)





def insertI(arr,n,i):
    pass


def main():
    # print()
    a=[2,1,5,2,0,5,3,4,2,3,7]
    # b = merge_sort(a)
    # myInsertSort(a)
    # insertSort3(a)
    # print(b)
    # c=quick_sort(a)
    # print(c)
    # quick_sort3(a,0,len(a)-1)
    shellSort(a)
    print(a)
    # for i in range(5000000):
    #     a.append(random.randint(1, 5000000))
    # b = copy.deepcopy(a)
    #
    # start = datetime.datetime.now()
    # insertSort(a)
    # end = datetime.datetime.now()
    # print('time1=%d'%(end-start))
    #
    # start1 = datetime.datetime.now()
    # insert_sort(b)
    # end1 = datetime.datetime.now()
    # print('time2=%d'%(end1 - start1))




if __name__ == '__main__':
    main()
