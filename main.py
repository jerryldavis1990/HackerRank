if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(N):
        values = input().split()
        if 'append' in values:
            li.append(int(values[1]))
        elif 'insert' in values:
            li.insert(int(values[1]),int(values[2]))
        elif 'reverse' in values:
            li.reverse()
        elif 'sort' in values:
            li.sort()
        elif 'print' in values:
            print(li)
        elif 'remove' in values:
            li.remove(int(values[1]))

