class FooError(ValueError):
    pass

def testException(a):
    try:
        print('try...')
        r=10/int(a)
        print('result:',r)
    except ValueError as e:
        print('ValueError:',e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError:",e)
    else:
        print("else....")
    finally:
        print('finally...')
    print('end')
def foo(s):
    n=int(s)
    if n==0:
        # raise FooError("Error")
        raise ValueError("Error")
    return 10/n

def main():
    testException('a')
    foo(0)

if __name__ == '__main__':
    main()