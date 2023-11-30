# greedy 볼링공 고르기
# (입력) 
# 8 5 볼링공의 개수, 공의 최대 무게
# 1 5 4 3 2 4 5 2 각 공의 무게
# (출력) 
# 25 두 사람이 다른 무게를 가진 공을 고를 수 있는 조합의 수
# 1 2 2 3 4 4 5 5

def select_bowling_ball():
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()

    result = 0
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]!=data[j]:
                result += 1

    print(result)
