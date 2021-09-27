# 1、产生100以内的随机数，直到随机数为66时终止循环
# 2、把100-200之间的不能被6整除的数输出并且每行输出10个

# 第1题
from random import randint
count = 1
while randint(0,100) != 66:
    count += 1
else:
    print(f"终止于第{count}次循环")

# 第2题
count = 0
for i in range(100,201):
    if count % 10 == 0:
        print("")
    if i % 6 != 0:
        print(i,end=" ")
        count += 1

            
