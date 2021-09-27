# 1、定义一个函数实现：计算年龄并返回的功能
# 2、定义一个函数实现：查找数据容器中是否存在评分超过9.5的番剧并返回超过9.5分的番剧信息

# 第1题
# def agecalc(birth : int,year : int):
#     return year - birth
# ago = int(input("请输入出生年份："))
# now = int(input("请输入今年的年份："))
# print("计算年龄为：",agecalc(ago,now))

# 第2题
Animation_List = {'name':'名侦探柯南','score':9.8},\
{'name':'鬼灭之刃','score':9.1},\
{'name':'无能力者娜娜','score':9.4}

def search(info):
    if info.get('score') > 9.5:
            print(f"符合要求的有{info['name']}")
for info in Animation_List:
    search(info)  
    
def test(*args):
    for info in args:
        if info.get('score') > 9.5:
            print(f"符合要求的有{info['name']}")
test(*Animation_List)

def test(**args):
        if args.get('score') > 9.5:
            print(f"符合要求的有{args['name']}")
for info in Animation_List:
    test(**info)