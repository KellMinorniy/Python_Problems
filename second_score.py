sec =  int(input())
l = set(input().split())
l.remove(max(l))
print(int(max(l)))