import random
def make_lotto(num):
    result = []
    # num의 수 만큼 lotto 번호를 생성하여 리턴하는 함수
    for i in range(num):
        lotto_num = set()
        while len(lotto_num) < 6:  # 수정: make_lotto() -> lotto_num
            com = random.randint(1, 45)  # 1~45 랜덤값
            lotto_num.add(com)
        result.append(list(lotto_num))  # 수정: list(com) -> list(lotto_num)
    return result

if __name__ == "__main__":
    print('모듈 자체 실행')
    lotto_num = make_lotto(3)
    print(lotto_num)
else:
    print("import 했음")

lotto_num = make_lotto(3)
print(lotto_num)