from random import choice
import datetime
import time
begin_input = input("你希望挑战几个数的组合？\n")
response = []
print("请按顺序找出数字：")
if begin_input == "":
    begin_input = "8"
for i in range(1, int(begin_input)+1):     # 选择难度，希望挑战的数字越多，则难度越大
    response.append(i)
for j in range(len(response)):          # 计数，准备选择数据
    choose = choice(response)
    print(choose, end="  ")
    response.remove(choose)
    if (j+1) % 7 == 0:
        print("")
# 开始计算运行时间
start_time = time.strftime('%Y-%m-%d %H:%M:%S')     # 格式化时间
end_input = input("\n如果你按顺序找出了全部数字，请点击enter（回车键）:")
# 运行时间完成计算
end_time = time.strftime('%Y-%m-%d %H:%M:%S')   # 格式化时间
t1 = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")    # datetime.datetime对象
t2 = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")      # datetime.datetime对象
interval_time = (t2 - t1).seconds
all_store = 300
store = all_store - interval_time
if store < 0:
    print("你用的时间已超过5分钟，可以尝试降低难度")
else:
    print("满分为300分")
    print("你获得的分数是：" + str(store))
