num=1
def test():
    global num
    num=2
def count(arr):
    num=0
def mergeSortCounting(arr,p,r):
    if p>r : return
    q=(p+r)//2
    mergeSortCounting(arr,p,q)
    mergeSortCounting(arr,q,r)

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

if __name__ == '__main__':
 test()
 print(num)
