def square(a):
    low=0
    high=a
    mid=a/2
    while abs(mid**2-a)>0.0000001:
        if mid**2<a:
            low=mid
        else:
            high=mid
        mid=(low+high)/2
    return mid

# 查找第一个值等于给定值的元素
def bsearch(arr,value):
    low=0
    high=len(arr)-1
    while low <=high:
        mid=low+(high-low)>>1
        if arr[mid]>value:
            high=mid-1
        elif arr[mid]<value:
            low =mid+1
        else:
            if (mid==0) or (arr[mid-1]!=value):
                return mid
            else:
                high=mid-1
    return -1

# 查找最后一个值等于给定值的元素
def bsearch1(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            if (mid == len(arr) - 1) or (arr[mid + 1] != value):
                return mid
            else:
                low = mid + 1
    return -1

# 查找第一个大于等于给定值的元素
def bsearch2(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] >= value:
            if (mid == 0)or(arr[mid-1]<value):
                return mid
            else:
                high = mid - 1
        else:
            low=mid+1
    return -1

# 查找最后一个小于等于给定值的元素
def bsearch3(arr,value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] <= value:
            if (mid == len(arr)-1)or(arr[mid+1]>value):
                return mid
            else:
                low = mid +1
        else:
            high=mid-1
    return -1

def binSearch(nums,target,low,high):
    while low<=high:
        mid=low+((high-low)>>2)
        if nums[mid]>target:
            high=mid-1
        elif nums[mid]<target:
            low=mid+1
        else:
            return mid
    return -1

def bsearch4(arr, value):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid]==value:
            return mid
        if arr[mid]>=arr[0]:
            if arr[mid]>value and arr[low]<value:
                return binSearch(arr,value,low,high)
            else:
                low=mid+1
        else:
            if arr[mid]<value and value<arr[high]:
                return binSearch(arr,value,low,high)
            else:
                high=mid-1
    return -1

def fib(n):
    f=1
    g=1
    while (n>0):
        n-=1
        g=g+f
        f=g-f
    return g



if __name__ == '__main__':
    print(fib(4))
    # a=[1,1,1,2,2,3,4,4,5,5,5,5,5,5,7,7,8,9]
    # a=[1,1,2]
    # a=[7,7,7,9]
    a=[4,5,6,1,2,3]
    # f=bsearch(a,1)
    # print(f)
    print(bsearch4(a,1))
