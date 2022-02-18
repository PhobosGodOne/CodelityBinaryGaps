def solution(N):
    flag = 0
    binaryVer = format(N,"b")
    biggestGap = 0
    for i in range(0,len(binaryVer)):

        j=0
        counter = 0

        while(flag == 0 and i+j < len(binaryVer)):

            if(int(binaryVer[i+j]) == 1):
                flag = 1
                i = j
                break
            else:
                counter +=1
                j += 1
            if i+j == len(binaryVer):
                counter=0


        if counter > biggestGap:
            biggestGap = counter

        flag = 0

    return biggestGap


print(solution(9))
