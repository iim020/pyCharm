# 문자열 '' on "" 긴문자열 쓸경우 ''' ''', """ """
print("\n========= 문자열 ===========\n")
a = "hi"
print(a)
print(type(a)) # type 함수는 자료의 타입을 볼때 사용
a = 1
print(type(a))
a = str(a) # to str
print(type(a))
print(a * 100) # 문자열 곱이 됨
a = int(a)
print(type(a))

print("\n========= 배열 ===========\n")
# 배열
arr = [] # 빈 배열
arr.append(1)
arr.append('hi')
arr.append([1,2,3,4])
print(arr)
print(arr[2][1]) # 2번째의 1번째 데이터
print('슬랑이스 1:3 ->', arr[1:3])
print(arr * 100)

print("\n========= 반복문 ===========\n")
# 반목문 for (3가지)
# 1값만 필요할때
for v in arr:
    print(v) # <-- v는 순차적인 배열의 값
# 인덱스값과 volue 값이 필요할때
for i, v in enumerate(arr):
    print('idx', 1,'val',v)

# 3. 단순 반복이 필요할때
for i in range(10):
    print(i)

for i in range(1,10):
    print(i)

for i in range(len(arr)): # len -> length
    print(arr[i])

msg = input('숫자를 입력해 주세요^^')
#input의 입력 값은 문자열
for i in range(input(msg)):
    print(i)

