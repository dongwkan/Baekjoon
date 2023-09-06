import sys
input = sys.stdin.readline

from collections import deque

a = deque([])

def push(X):
    a.append(X)

def pop():
    if a == deque([]):
        print(-1)
    else:
        print(a.popleft())

def size():
    print(len(a))

def empty():
    if a == deque([]):
        print(1)
    else:
        print(0)

def front():
    if a == deque([]):
        print(-1)
    else:
        print(a[0])

def back():
    if a == deque([]):
        print(-1)
    else:
        print(a[-1])


N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        push(int(cmd[1]))
    elif cmd[0] == "pop":
        pop()
    elif cmd[0] == "size":
        size()
    elif cmd[0] == "empty":
        empty()
    elif cmd[0] == "front":
        front()
    else:
        back()
