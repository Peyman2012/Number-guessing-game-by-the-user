list_2=[]
n = int(input())
list_1 = list(map(int, input().split()))
count=0
if len(list_1)==6:
    for k in list_1:
        if k <= 5:
            list_2.append(k)
    for j in list_2:
        if j <= 3:
            count += 1
    count_a = 0
    if count == 3 or count == 4 or count == 5:
        count_a = 1
        print(count_a)
    elif count == 6:
        count_a = 2
        print(count_a)





