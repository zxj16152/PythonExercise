result=[0 for x in range(8)]


def printQueens(result): # 打印8*8结果
    for row in range(8):
        for col in range(8):
            if result[row] == col:
                print('Q', end=' ')
            else:
                print('*', end=' ')
        print() # 换行


def isOk(row, col):
    leftup,rightup=col-1,col+1
    for r in range(row-1,-1,-1):
        if result[r] in [leftup,rightup,col]:
            return False
        leftup-=1
        rightup+=1
    return True



# def isOk(row, col):
#     leftup, rightup = col-1, col+1
#     for r in range(row-1,-1,-1): # 遍历[row-1，-1)行
#         if result[r] in [leftup,rightup,col]:
#             return False
#         leftup -= 1
#         rightup += 1
#     return True

def cal8queens(row):
    if row==8:
        printQueens(result)
        print('-'*20)
        return
    for col in range(8):
        if isOk(row,col):
            result[row]=col
            cal8queens(row+1)

if __name__ == '__main__':
    cal8queens(0)