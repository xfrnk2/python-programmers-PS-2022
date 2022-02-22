# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    temp = iter(Counter(participant) - Counter(completion))
    return next(temp)