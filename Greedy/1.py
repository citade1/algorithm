# greedy 모험가 길드
# 입력 2 3 1 2 2 출력 2
# 1 2 2 2 3
def adv_guild():
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    
    pointer = n-1 # 시작점에서 포인터가 가리키는 인덱스 위치(제일 큰 공포도부터 시작)
    result = 0 # 총 그룹 수

    while pointer>=0: # 포인터가 0이상일 동안 반복
        temp = data[pointer]  
        if temp<=pointer+1: # 현재 공포도가 현재의 인덱스+1(즉 남아있는 모험가의 수)보다 작거나 같을 때 그룹 결성
            result += 1 # 그룹 수 +1
            pointer -= temp # 그룹에 포함된 인원만큼 포인터를 아래로 내림
        else:
            break

    return result
