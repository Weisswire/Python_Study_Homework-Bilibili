# 1、使用字符串复制：打印100次 "爱你一百遍"
# 2、将"to be or not to be" 字符串倒序输出
# 3、将"China China China"字符串中所有的C输出
print("爱你一百遍\n"*99+"爱你一百遍")
info = "to be or not to be"
print(info[::-1])
info1 = "China China China"
print("C"*(info1.count("C")))
start = 0
result = ""
while start <= len(info1):
    if info1.find("C",start,len(info1)) >= 0:
        result += info1[info1.find("C",start,len(info1))]
        start = info1.find("C",start,len(info1)) + 1
    else:
        start += 1
print(result)