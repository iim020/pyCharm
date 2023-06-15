import os
#
# path = "/"
# filename = 'file1'
# dir = os.path.abspath(path)
# for dirpath, dirnames, filenames in os.walk(dir):
#     # print(dirpath, dirnames, filenames)
#     for file in filenames:
#         if file == filename:
#             print(dirpath, filename)

# path = "/"
# filename = 'file1'
# dir = os.path.abspath(path)
# for dirpath, dirnames, filenames in os.walk(dir):
#         # print(dirpath, dirnames, filenames)
#     for file in filenames:
#         if filename in file:
#              print(dirpath, file)

path = "/"
filename = 'file1'
dir = os.path.abspath(path)
for dirpath, dirnames, filenames in os.walk(dir):
         # print(dirpath, dirnames, filenames)
     for file in filenames:
         if filename in file:
              print(dirpath, file)
              msg = input('c찾는 파일이 맞나요')
              if msg == 'Y':
                  break