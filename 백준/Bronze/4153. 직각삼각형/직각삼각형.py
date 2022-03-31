while True:
    lines = list(map(int, input().split()))
    if lines[0]==0 and lines[1]==0 and lines[2]==0:
        break;
    else:
        lines.sort()
        if lines[2]**2 == lines[0]**2 + lines[1]**2:
            print('right')
        else:
            print('wrong')