# 1、创建文件text.txt 并输入100行192.168.1.0-50的IP地址
# 例如：192.168.1.1 192.168.1.6 1.2.168.1.32
# 2、统计text.txt文件中192.168.1.6的IP出现频率
import os
from random import randint 

with open('text.txt','w') as f:
    for i in range(101):
        IPAdd = randint(0,50)
        f.write(f'192.168.1.{IPAdd}\n')

if os.path.exists("text.txt"):
    with open("text.txt","r") as f:
        count = 0
        for IP in f.readlines():
            if IP == '192.168.1.6\n':
                count += 1
    print(count)
else:
    print("There is not such a file named 'text.txt'!")