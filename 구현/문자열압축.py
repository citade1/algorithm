#  프로그래머스 문자열 압축 문제: https://school.programmers.co.kr/learn/courses/30/lessons/60057

# 문자열 s를 chunk_size로 자른 후, 리스트로 반환. 
# 예시) s='ababcdcdababcdcd', chunk_size=2 -> arr = ['ab','ab', 'cd', 'cd', 'ab','ab', 'cd', 'cd'] 
def str_to_chunk(s, chunk_size):
    arr = []
    for i in range(0, len(s), chunk_size):
        if len(s[i:])<chunk_size:
            arr.append(s[i:])
            break
        arr.append(s[i: i+chunk_size])
    return arr

# 일정한 크기의 문자열로 나뉜 리스트에서 압축 가능한 패턴을 찾아 압축. 다시 문자열로 반환.
# 예시) arr = ['ab','ab', 'cd', 'cd', 'ab','ab', 'cd', 'cd'] -> new_str = '2ab2cd2ab2cd'
def find_pattern(arr):
    new_str=''
    count = 1
    
    for i in range(1, len(arr)):
        if arr[i]==arr[i-1]:
            if i==len(arr)-1:
                count += 1
                new_str += str(count) + arr[i-1]
                break
            count += 1
        else:
            if count > 1:
                new_str += str(count) + arr[i-1]
            else:
                new_str += arr[i-1]
            
            if i==len(arr)-1:
                new_str += arr[i]
                break
            count = 1
    
    return new_str

# 주어진 문자열을 가능한 모든 크기로 자른 후, 각각 패턴을 찾아 압축. 그중 가장 작게 압축된 크기를 반환.
# 예시) s = 'ababcdcdababcdcd', 가장 작은 압축='2ababcdcd' -> min_len=8
def solution(s):
    n = int(len(s)/2) 
    length_arr = []
    for i in range(1, n+1):
        arr = str_to_chunk(s, i)
        new_s = find_pattern(arr)
        length_arr.append(len(new_s))
        # print(new_s)
    length_arr.append(len(s))

    min_len = length_arr[0]
    for i in length_arr:
        if i < min_len:
            min_len = i
    
    return min_len
      
