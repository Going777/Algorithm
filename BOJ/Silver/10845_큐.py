import sys

arr = []
for _ in range(int(sys.stdin.readline())):
    commands = sys.stdin.readline().split()
    cmd = commands[0]
    if cmd == "push":
        arr.append(commands[1])
    elif cmd == "pop":
        x = arr.pop(0) if arr else -1
        print(x)
    elif cmd == "size":
        print(len(arr))
    elif cmd == "empty":
        print(1-int(bool(arr)))
    elif cmd == "front":
        print(arr[0] if arr else -1)
    elif cmd == "back":
        print(arr[-1] if arr else -1)