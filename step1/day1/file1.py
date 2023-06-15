import os

print(os.getcwd()) # 현재 경로
path = os.getcwd()
file_list = os.listdir(path) # 경로에 파일에 접근
for file_nm in file_list:
    file_path = path + "/" + file_nm +"/files"
    if os.path.exists(path + "/" + file_nm):
        print(file_nm)
        if os.path.isdir(path + "/" + file_nm):
            print('디렉토리')
        if os.path.isfile(file_path):
            print("파일임")
            os.remove(file_path) #파일 삭제