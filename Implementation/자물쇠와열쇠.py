# 프로그래머스 자물쇠와 열쇠 문제 -> https://school.programmers.co.kr/learn/courses/30/lessons/60059
#                key	                          lock	                 result
# [[0, 0, 0],[1, 0, 0],[0, 1, 1]]	  [[1, 1, 1],[1, 1, 0],[1, 0, 1]]	  true
# 
# 푸는 방법: {자물쇠 배열 상하좌우 외곽에다 key-1 크기만큼의 패딩을 추가해준다.
# 따라서 원래 자물쇠배열 크기가 NxN이었다면, 패딩을 추가한 후에는 (N + 2*(key-1)) x (N + 2*(key-1))
# 확장된 자물쇠 배열 위에서, 열쇠배열이 step=1의 슬라이딩 윈도우 방식으로 한칸씩 나아간다. 
# 이때 한칸마다 90도씩 총 4번 회전하여 자물쇠에 들어맞는지 확인한다. 들어맞으면 언제라도 return True.}
import copy 

def solution(key, lock):
    pad_size = len(key)-1
    padded_lock = padding(lock, pad_size) #lock 배열에 패딩 추가
    n = len(padded_lock) 
    m = len(key)
    
    # padded_lock 칸마다 반복. 단, key가 padded_lock을 넘어서지 않게 사이즈는 (padded_lock크기 - key크기 + 1)
    for i in range(n-m+1):
        for j in range(n-m+1):
            # 한 칸마다 4번 90도 회전
            for _ in range(4):
                key = rotate90(key)
                temp_padlock = copy.deepcopy(padded_lock)
                
                # key가 padded_lock과 들어맞는 지 확인. 
                # pad_lock의 copy버전인 temp_padlock을 생성하여 들어맞는 칸마다 temp_padlock의 값을 1로 변경(원래1이면 변경없고, 0이면 1로).
                try: 
                    for key_i in range(m):
                        for key_j in range(m):
                            # padded_lock의 값이 0/1일 때, key의 값이 1/0이 아니면 바로 NoMatch exception을 일으켜 루프 탈출. rotate90()으로 넘아감.
                            if (padded_lock[i+key_i][j+key_j]!=-1) and (padded_lock[i+key_i][j+key_j]+key[key_i][key_j]!=1):
                                raise NoMatch
                            if (padded_lock[i+key_i][j+key_j]!=-1) and (padded_lock[i+key_i][j+key_j]+key[key_i][key_j]==1): 
                                temp_padlock[i+key_i][j+key_j]=1 
                except NoMatch:
                    continue
                
                # temp_padlock의 값이 모두 -1이거나 1이면 열쇠가 다 맞춰진것이므로, return True.
                try:
                    for x in range(n):
                        for y in range(n):
                            if temp_padlock[x][y]==0:
                                raise NoMatch
                    return True
                except NoMatch:
                    continue
    
    # 끝까지 한번도 맞지 않았다면 return False
    return False

class NoMatch(Exception):
    pass

# key 2차원 배열 오른쪽으로 90도 회전. (왼쪽이어도 상관없지만 여기서는 오른쪽으로 구현.)
def rotate90(key):
    n = len(key) # key 배열 크기 nxn
    new_arr = [[0]*n for _ in range(n)] # 90도 회전한배열을 담을 새배열 초기화.
    
    for i in range(n):
        for j in range(n):
            if key[i][j]==1:
                new_arr[j][n-i-1]=1

    return new_arr

# lock 2차원 배열 패딩. 
def padding(lock, pad_size):
    n = len(lock) + 2*pad_size
    new_lock = [[-1]*n for _ in range(n)] # padding 값은 -1.

    for i in range(pad_size, n-pad_size):
        for j in range(pad_size, n-pad_size):
            new_lock[i][j] = lock[i-pad_size][j-pad_size]
    
    return new_lock
