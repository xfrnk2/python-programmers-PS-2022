from collections import Counter

def solution(clothes):
    answer = 1
    data = Counter([x[1] for x in clothes])
    for v in data.values():
        answer *= v + 1
    return answer - 1