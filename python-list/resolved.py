if __name__ == '__main__':
    N = int(input())
    output = []
    for i in range(N):
        uinput = input()
        data = uinput.split()
        if data[0] == 'insert':
            output.insert(int(data[1]),int(data[2]))
        if data[0] == 'print':
            print(output)
        if data[0] == 'remove':
            output.remove(int(data[1]))
        if data[0] == 'append':
            output.append(int(data[1]))
        if data[0] == 'pop':
            output.pop()
        if data[0] == 'sort':
            output.sort()
        if data[0] == 'reverse':
            output.reverse()


# refered code
# list1 = []
# n = int(input())
# for i in range(n):
#     s, *d = input().split()
#     d = list(map(int, d))
#     if s == "print":
#         print(list1)
#     else:
#         getattr(list1, s)(*d)
