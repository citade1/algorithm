# 문제 뱀: https://www.acmicpc.net/problem/3190
# 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 
# 뱀은 처음에 오른쪽을 향한다.
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다. 
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며. 
# 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.
# 출력
# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.
from collections import deque

## 입력받기 시작
N = int(input()) # 보드 크기
K = int(input()) # 사과 개수

# 보드의 모든 칸은 0이 디폴트, 사과가 있는 칸은 1. 
board = [[0]*N for _ in range(N)]
for i in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 처음 진행 방향은 오른쪽, 즉 동쪽 -> 1
direction = 1

def turn_direction(C):
    global direction
    if C=='L':
        direction -= 1
        if direction<0:
            direction = 3
    if C=='D':
        direction += 1
        if direction>3:
            direction = 0

# 방향이 바뀌는 [초, 바뀌는방향] 리스트  
directions = deque()
L = int(input())
for i in range(L):
    X,C = input().split()
    directions.append([X,C])

## 입력받기 완수


## 시뮬레이션 시작
    
snake_path = deque([(0,0)]) # 뱀의경로 (큐로 구현)
snake_loc = [[0]*N for _ in range(N)] # 뱀이 존재하는 위치 
tail_x, tail_y = 0,0 # 뱀꼬리 좌표
head_x, head_y = 0,0 # 뱀머리 좌표
snake_loc[head_x][head_y] = 1  

time = 0 
timeout = False # 게임이 끝났는지 아닌지 표시하는 flag
time_direction = directions.popleft() # 첫번째 방향을 바꾸어야하는 시간, 방향 받아오기
while not timeout:
    # 방향 바꾸어야 하는지 확인
    if int(time_direction[0])==time:
        turn_direction(time_direction[1]) 
        if len(directions)>0:
            time_direction = directions.popleft() # 방향을 바꾸었으니 새로운 시간, 방향 가져오기
                
    time += 1
    tempx = head_x + dx[direction]
    tempy = head_y + dy[direction]
    
    # 보드의 바깥으로 벗어나려고 한다면
    if tempx<0 or tempx>N-1 or tempy<0 or tempy>N-1:
        timeout = True
        break
    

    # 현재진행위치에 사과가 없다면
    if board[tempx][tempy]==0:
        if snake_loc[tempx][tempy]==0: # 나아갈위치가 현재 뱀의 위치와 겹치지 않는다면
            head_x, head_y = tempx, tempy
            snake_loc[head_x][head_y] = 1
            snake_path.append([head_x, head_y])

            tail_x, tail_y = snake_path.popleft() # 머리가 한 칸 나아가는 만큼 꼬리도 앞으로 간다.
            snake_loc[tail_x][tail_y] = 0
            
        else: # 뱀이 현재 있는 곳과 겹친다면
            timeout=True
            break
    # 현재진행위치에 사과가 있다면
    if board[tempx][tempy]==1:
        board[tempx][tempy] = 0 # 사과를 먹고 값을 0으로 바꿈.
        if snake_loc[tempx][tempy]==0: # 나아갈위치가 현재 뱀의 위치와 겹치지 않는다면
            head_x, head_y = tempx, tempy
            snake_loc[head_x][head_y] = 1
            snake_path.append([head_x, head_y])
        else: # 뱀이 현재 있는 곳과 겹친다면
            timeout=True
            break

## 시뮬레이션 완료
                       
print(time)    
   



    

