'''
combination 스크래치 구현
input
- arr: 전체 배열. e.g. [1,2,3]
- r: 선택 개수. 전체 중에 r개를 선택함.
- curr_comb: 현재까지의 조합
- all_comb: 최종 조합 결과를 저장하는 리스트

code
재귀적으로 리스트를 순회하면서 각 단계에서 원소를 선택하거나 선택하지 않는 두 가지 경우로 나눠서 조합을 만듭니다. 

output 예시
[1,2,3]배열에서 2개를 선택하는 조합은 [[1,2],[1,3],[2,3]]
'''
def combination(arr, r, curr_comb, all_comb):
    if r==0:
        all_comb.append(curr_comb)
        return
    if len(arr)==0:
        return
  
    combination(arr[1:], r-1, curr_comb+[arr[0]], all_comb)
    combination(arr[1:], r, curr_comb, all_comb)

