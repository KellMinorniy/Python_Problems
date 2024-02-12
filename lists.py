n = int(input())
arr = list()
for i in range(n):
    f = input().split()
    com = f.pop(0)
    m = [int(k) for k in f]
    if (com == "print"):
        print(arr)
    elif( com == "insert"):
        arr.insert(int(m[0]), m[1])
    elif(com == "remove"):
        arr.remove(m[0])
    elif(com == "append"):
        arr.append(m[0])
    elif(com == "sort" ):
        arr.sort()
    elif(com == "pop" ):
        arr.pop()
    elif(com == "reverse" ):
        arr.reverse()
    