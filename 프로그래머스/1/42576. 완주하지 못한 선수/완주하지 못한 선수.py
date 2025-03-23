from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

# 시간 복잡도 : O(N)
# Counter(participant) : 이름별 사람 수 카운팅
# Counter(completion) : 완주한 사람 수 카운팅

########### Counter가 머임? ###########
# dictionary처럼 동작하는 파이썬 내장 클래스
# list 같이 iterable 한 데이터 넣으면 자동으로 개수 세줌

# ex. Counter(['a', 'b', 'b', 'c']) >> Counter({'b': 2, 'a': 1, 'c': 1})
