import os
file = 'delay.txt'
f= open(file, 'a') # a appen, r read , w write
while True:
    n = input('오늘 지각한 사람 !! (종료q)')
    if 'q' == n:
        break
    f.write(n)
    f.writelines('\n')
f.close()