#  프로그래머스 문자열 압축 문제: https://school.programmers.co.kr/learn/courses/30/lessons/60057

# 간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 
# 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다. 
# 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.
# 예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 
# 다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.
# 다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 
# 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
# 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# s의 길이는 1 이상 1,000 이하입니다.
# s는 알파벳 소문자로만 이루어져 있습니다.
# 입출력 예
# "aabbaccc"	7
# "ababcdcdababcdcd"	9
# "abcabcdede"	8
# "abcabcabcabcdededededede"	14
# "xababcdcdababcdcd"	17

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
      
