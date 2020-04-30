#字典定义的方式
hogwarts_dict = {"a":1,"b":2}
hogwarts_dic2 = dict(a=1,b=2)
print(hogwarts_dic2)
print(hogwarts_dict)

#常用的函数
"""
pop
popitem
"""
a = {"a":1,"b":2}
b = dict(a=1,b=2)
#删除组键值
print(a.popitem())
#输出剩余的组键值
print(a)
