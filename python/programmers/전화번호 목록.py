# v1
def solution(phone_book):
    answer = True
    trg = False
    for phone_num1 in phone_book:
        num1_len = len(phone_num1)
        if trg:
            break
        for phone_num2 in phone_book:
            if num1_len < len(phone_num2):
                if phone_num1 == phone_num2[:num1_len]:
                    answer = False
                    trg = True
                    break

    return answer