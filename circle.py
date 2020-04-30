
"""
1. 计算1-100的和
2. 加入分支结构实现1-100之间的偶数求和
3. 使用python实现1-100之间的偶数求和
"""

#python语法写的
#result = 0
#for i in range(2,101,2):
 #   result = result + i
#print(result)


"""
猜数字游戏
计算机出一个1-100的随机数由人来猜
计算机根据人猜的数字分组
给出提示，大一点，小一点，猜对了

"""
import random
p_no = 0
c_no = random.randint(1,100)
#print(c_no)
while True:
    p_no = int(input("请输入一个数字: "))
    if p_no > c_no:
        print("大了")
    elif p_no < c_no:
        print("小了")
    elif p_no == c_no:
        print("bingo,猜对啦")
        break




