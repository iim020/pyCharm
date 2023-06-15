# 경로, 파일명을 입력받아
# 파일을 찾고 경로를 출력하는 함수를 만드세요
import os

def fn_search(filename, path='/'):  # 경로가 없으면 전체에서 검색
    print('찾은 파일 전체 경로:')
    dir = os.path.abspath(path)
    for dirpath, dirnames, filenames in os.walk(dir):
        # print(dirpath, dirnames, filenames)
        for file in filenames:
            if filename in file:
                print(os.path.join(dirpath, file))

filename = input('파일명을 입력하세요: ')
path = input('파일 경로를 입력하세요: ')

fn_search(filename, path)