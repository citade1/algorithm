# greedy 문자열 뒤집기
# 입력 0001100 출력 1
def string_flip():
    data = input()
    count0 = 0 #전부 0으로 뒤집힐 때 필요한 횟수
    count1 = 0 # 전부 1로 뒤집힐 때 필요한 횟수

    if data[0]=="1":
        count0 += 1
    else:
        count1 += 1
    
    for i in range(1, len(data)):
        if data[i]=="1": #0에서 1로 바뀔때 count0 +1
            if data[i-1]=="0":
                count0 += 1
        else: #1에서 0으로 바뀔때 count1 +1
            if data[i-1]=="1":
                count1 += 1
        
    return min(count0, count1)  
