myString="abcdefghigkl"
for i in [None]+range(-1,-len(myString),-1):
    print(myString[:i])