#PRINTING 2nd LARGEST NUMBER AFTER SOME OPERATIONS ON SET

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=set()
    for i in arr:
        l.add(i)
    l=sorted(l)
    print(l[-2])
