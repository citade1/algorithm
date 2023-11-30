# greedy 만들 수 없는 금액 중 최솟값 찾기
# 입력 1 3 5 7 9 출력 2
def never_ever():
    n = int(input())
    data = list(map(int, input().split()))
    data.sort() # 오름차순으로 정렬

    target = 1
    for x in data: 
        if target < x: # 자신보다 작은 수를 더해 만들어질 수도 없고, 그 다음 수보다도 작으면, 절대 만들어질 수 없는 수가 됨.
            break # 따라서 루프 빠져나옴.
        target += x 

    print(target)
