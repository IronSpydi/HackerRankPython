def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    ti = [string[i:i+k] for i in range(0,n,k) ]
    print(ti)
    ui = []
    for i in ti:
        u = []
        for j in i: 
            if j not in u:
                u.append(j)
        ui.append(u)
    for sstring in ui:
        print(''.join(sstring))
if __name__ == '__main__':
    merge_the_tools('AABCAAADA', 3)