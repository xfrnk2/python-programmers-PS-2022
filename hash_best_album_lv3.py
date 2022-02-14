# https://programmers.co.kr/learn/courses/30/lessons/42579
# from collections import defaultdict
#
#
# def solution(genres, plays):
#     d = defaultdict(list)
#     for i in range(len(genres)):
#         d[genres[i]].append((plays[i], i))
#     for i in d.keys():
#         d[i] = sorted(d[i], key=lambda x: (-x[0], x[1]))
#     nd = sorted(list(d.keys()), key=lambda c: sum(map(lambda i: i[0], d[c])), reverse=True)
#
#     return [y[1] for x in [d[g][:2] for g in nd] for y in x]

def solution(genres, plays):
    answer = []
    genreDict = {}
    songDict = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        genreDict[genre] = genreDict.get(genre, 0) + play
        songDict[genre] = songDict.get(genre, []) + [(play, i)]

    genreSort = sorted(genreDict.items(), key=lambda x: x[1], reverse=True)

    for genre, totalplay in genreSort:
        rankSort = sorted(songDict[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([i for play, i in rankSort[:2]])
    return answer

