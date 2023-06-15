import datetime

# 현재 날짜와 시간
now = datetime.datetime.now()

#format
now_yyyymmdd = now.strftime("%Y-%m-%d %H:%M:$S")
print(now_yyyymmdd)
now_yymmdd = now.strftime("%y-%m-%d %H:%M:%S")
print(now_yymmdd)

# 문자열 to datetime
data_str = '2023-01-01 11:30:01'
foramt = '%Y-%m-%d %H:%M:%S'
data = datetime.datetime.strptime(data_str, foramt)
print(data,type(data))