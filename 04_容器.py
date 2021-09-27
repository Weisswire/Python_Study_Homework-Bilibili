# 1、以下是一部番的多个评分
# [8 8.5 9 9.5 8.2 10 6 8.8 9.2 8.2]
# 查找里面的内容有没有满分10以上及0分，去掉最高分与最低分输出结果
# 2、编写程序存储三个番的信息，其中保存番名、评分、发布时间

# 第1题
print("="*10,"第1题","="*10)    
scores = [8, 8.5, 9, 9.5, 8.2, 10, 6, 8.8, 9.2, 8.2]

if 0 not in scores:
    print("没有找到评分为0分番剧")
else:
    print(f"评分为0分的番剧有{scores.count(0)}部")
if 10 not in scores:
    print("没有找到评分为10分番剧")
else:
    print(f"评分为10分的番剧有{scores.count(10)}部")

min,max = 0,1
for i in range(len(scores)):
    if scores[i] <= scores[min]:
        min = i
    if scores[i] >= scores[max]:
        max = i
scores.pop(min)
del scores[max]
print(f"去掉最高分和最低分后的番剧分数列表为：{scores}")

# 第2题
print("="*10,"第2题","="*10)      
animation_list = [{"name":"致不灭的你","score":"9.8","date":"2021-04"},\
                 {"name":"佐贺偶像是传奇 卷土重来","score":"9.9","date":"2021-04"},\
                 {"name":"炎炎消防队","score":"9.2","date":"2020-07"}]
for animation in animation_list:
    print(animation)