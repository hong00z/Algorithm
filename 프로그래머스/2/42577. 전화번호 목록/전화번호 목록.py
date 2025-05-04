def solution(phone_book):
    answer = True
    # 정렬하고
    phone_book = sorted(phone_book)
    # 앞뒤로 비교
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return answer