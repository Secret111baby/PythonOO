#元祖的定义，不可变，例如执行以下程序会报错，提示TypeError: 'tuple' object does not support item assignment
tuple_hogwarts = (1,2,3)
tuple_hogwarts[1] = 'a'
print(tuple_hogwarts)
#但是元祖当中嵌套列表，就会可变，例如
a = (1,2,3)
tuple_hogwarts2 = (1,2,3,a)
tuple_hogwarts2[2][0] = "a"
print(tuple_hogwarts2)