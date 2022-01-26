# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    i = iter((Counter(participant) - Counter(completion)).keys())
    return next(i)