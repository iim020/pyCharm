# set 종복 없이 유니크한 값만 얻고자 할때
my_set = {1,2,3,4,5,5}
print(my_set)
my2_set = set()
print(type(my2_set))
my_set.add(1) # 하나만 추가
my_set.update({4,5,10}) # 여러개 추가
print(my2_set)

# 교집합
a = my_set & my2_set
print(a)

# 합집합
b = my_set | my2_set
print(b)

# 차집합
c = my_set - my2_set
print(c)
