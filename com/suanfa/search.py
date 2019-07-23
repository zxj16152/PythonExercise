#二分查找
def search_binary(list,item):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        guess=list[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid -1
        else:
            low=mid+1
    return None

#选择排序
def findSmall(arr):
    smalllest=arr[0]
    smalllest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smalllest:
            smalllest=arr[i]
            smalllest_index=i
    return smalllest_index

def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smalllest = findSmall(arr)
        newArr.append(arr.pop(smalllest))
    return newArr
#选择排序
def selectionSort2(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)-1):
            if (arr[j] < arr[i]):
              arr[i],arr[j]=arr[j],arr[i]

    return arr



##快速排序
def quickSort(arr):
   if len(arr)<2:
       return arr
   else:
       pivot=arr[0]
       less=[i for i in arr[1:] if i <=pivot]
       greater=[i for i in arr[1:] if i>pivot]
       return quickSort(less)+[pivot]+quickSort(greater)

#归并排序
def merge_sort(arr):
    if len(arr)<2:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    ll = merge_sort(left)
    rr = merge_sort(right)
    return merge2(ll,rr)


def merge2(left,right):
    result=[]
    while len(left)>0 and len(right)>0:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result+=left
    result+=right
    return result



# binary = search_binary((1, 2, 3, 4, 5, 7), 6)
# print(binary)
# print(selectionSort([5,3,6,2,10]))
# print(selectionSort2([5,3,6,2,10]))
# countdown(10)
# print(fact(5))
print(quickSort([10,5,2,3]))
a=[1,2,3,4]
a.pop(0)
print(a)
print(a+[5])
print(merge_sort([10,5,2,3,3]))
# print(mergeSort([10,5,2,3]))
