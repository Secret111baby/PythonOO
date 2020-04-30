# list_square=[]
# for i in range(1,4):
#     list_square.append(i**2)
#
# print(list_square)
#列表的定义，是可变的
# List_square2=[i**2 for i in range(1,4)]
# print("List_square2",List_square2)
# List_square4 = []
# for i in range(1,4):
#     for j in range(1,4):
#         List_square4.append(i*j)


#元祖的定义，不可变，例如执行以下程序会报错，提示TypeError: 'tuple' object does not support item assignment
tuple_hogwarts = (1,2,3)
tuple_hogwarts[1] = 'a'
print(tuple_hogwarts)
#但是元祖当中嵌套列表，就会可变，例如
a = (1,2,3)
tuple_hogwarts2 = (1,2,3,a)
tuple_hogwarts2[2][0] = "a"
print(tuple_hogwarts2)

#相关函数
#例如count,index,count是计数，index是索引，定位元素的位置