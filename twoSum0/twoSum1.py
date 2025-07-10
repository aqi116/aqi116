import random
nums = []
for i in range(10000):
    nums.append(random.randint(1,65535))
# 获取 nums 的长度，并将结果存放到 n 变量中 #
target = int(input("请输入目标值："))
n = len(nums)
isFind = False
for i in range(n):
    for j in range(i+1,n ):
        if nums[i] + nums[j] == target:
            # 将找到的两个元素下标值以列表的形式打印出来 #
            print(f"[{i},{j}]")
            isFind = True
if isFind == False:
    print("没有找到")