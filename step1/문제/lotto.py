# 사용자에게 숫자를 입력받아
# 입력받은 수 만큼 로또번호를 생성(출력)해주세요
# 로또 번호는 1 ~ 45 숫자(중복없음)의 6자리
# ex2를 입력받으면 6자리 2개 출력

# 랜덤함수, input, 조건, 반복문을 활용

import random #라이브러리 임포트
user_num = int(input('숫자를 입력해 주세요 : '))

for i in range(user_num):
    lotto_num = set()
    while True:
        if len(lotto_num) < 6:
            com = random.randint(1,45) # 1~10 랜덤값
            lotto_num.add(com)
        else:
            break

    lotto_num.sort()
    print(i+1, "번째", lotto_num)
