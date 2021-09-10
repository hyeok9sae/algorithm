# 부분 문자열
def boyer_moore(S, P):
    S_size, P_size = len(S), len(P)
    i = 0
    while i <= S_size-P_size:
        j = P_size-1
        while j >= 0:
            if P[j] != S[i+j]:
                move = find(P, S[i+P_size-1])
                break
            j -= 1
        if j == -1:
            global count
            count += 1
            answer.append(i+1)
            i += 1
        else:
            i += move

def find(pattern, char):
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] == char:
            return len(pattern)-i-1
    return len(pattern)

S, P = input(), input()
count = 0
answer = []
boyer_moore(S, P)
print(count)
print(*answer)