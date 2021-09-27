# 1、条件语句有几种结构，分别是哪些
# 2、输入一个点的坐标(x,y)，判断其所在的象限
# 3、输入一个分数，分数在0-100之间，90以上是A，80到89是B，70到79是C，60到69是D，60以下是E

# 第2题
x = int(input("请输入该点的横坐标："))
y = int(input("请输入该点的纵坐标："))
if x > 0 and y > 0:
    print("您输入的点在第一象限")
elif x < 0 and y > 0:
    print("您输入的点在第二象限")
elif x < 0 and y < 0:
    print("您输入的点在第三象限")
elif x > 0 and y < 0:
    print("您输入的点在第四象限")

# 第3题
score = int(input("请输入您的分数："))
while score < 0 or score > 100:
    score = int(input("您输入的分数不合法，请重新输入："))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E") 