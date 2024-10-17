'''
input
- arr: 원소들이 담긴 리스트
- r: 선택해야 할 원소의 개수
- curr_perm: 현재까지의 순열
- all_perm: 모든 순열을 저장하는 리스트

각 단계에서 가능한 원소를 하나씩 선택하고, 선택한 원소를 제외한 나머지 원소들로 재귀적으로 순열을 만든다.
'''
def permutation(arr, r, curr_perm, all_perm):
    if r==0:
        all_perm.append(curr_perm[:]) # 현재 순열의 복사본 넘겨줌
        return

    for i in range(len(arr)):
        # 현재 선택한 원소를 추가
        curr_perm.append(arr[i])

        # 선택한 원소를 제외한 나머지 원소들로 다시 순열을 생성
        new_arr = arr[:i] + arr[i+1:] # i번째 원소를 제외한 새로운 리스트
        permutation(new_arr, r-1, curr_perm, all_perm)

        # 현재 바뀐 순열 리스트가 다른 순열을 구할 때 영향을 미치지 않게 원상 복구 
        curr_perm.pop()
