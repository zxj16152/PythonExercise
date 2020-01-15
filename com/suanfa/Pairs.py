class pairs:
    def __init__(self,first,second):
        self.first=first
        self.second=second

def findPairs(arr):
    sumPair=dict()
    n=len(arr)
    i=0
    while i<n:
        j=i+1
        while j<n:
            sums=arr[i]+arr[j]
            if sums not in sumPair:
                sumPair[sums]=pairs(arr[i],arr[j])
            else:
                p=sumPair[sums]
                print(str(p.first)+" "+str(p.second),str(arr[i])+" "+str(arr[j]))
                return True
            j+=1
        i+=1
    return False

if __name__ == '__main__':
    arr=[3,4,7,10,20,9,8]
    findPairs(arr)