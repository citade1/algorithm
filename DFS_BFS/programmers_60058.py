# 프로그래머스 괄호 변환 문제
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 
# 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
# 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
# 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
# 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
# 4-3. ')'를 다시 붙입니다. 
# 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
# 4-5. 생성된 문자열을 반환합니다.

def solution(p):
    answer = transform_bracket(p)
    print(answer)


def transform_bracket(brackets):
    if not brackets:
        return ""
    
    u, v = split_brackets(brackets)

    if is_correct(u):
        return u + transform_bracket(v)
    
    else:
        new_string = "("
        new_string += transform_bracket(v)
        new_string += ")"
        if len(u)>2:
            u = u[1:-1]
            flipped = ""
            for ch in u:
                if ch=="(":
                    flipped += ")"
                else:
                    flipped += "("
            new_string += flipped
        return new_string

                
            
                
def split_brackets(w):
    count_open, count_close = 0, 0
  
    for i in range(len(w)):
        if w[i]=="(":
            count_open += 1
        else:
            count_close += 1
        if count_open==count_close:
            if i==len(w)-1:
                return w[:i+1], ""
            return w[:i+1], w[i+1:]
        
    

def is_correct(brackets):
    stack = []
    for ch in brackets:
        if ch=="(":
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    
    return not stack



