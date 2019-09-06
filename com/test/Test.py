try:
    print(1)
    # 1/0;
except  ZeroDivisionError as e:
    print(2)
else:
    print(3)