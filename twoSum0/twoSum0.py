nums = []
while True:
    num = input("请123录入一个整数(输入STOP结束)：")
    if num == "STOP":
        break
    else:
        nums.append(int(num))
# 获取 nums 的长度，并将结果存放到 n 变量中 #
target = int(input("请输入目标值："))
n = len(nums)
for i in range(n):
    for j in range(i+1,n ):
        if nums[i] + nums[j] == target:
            # 将找到的两个元素下标值以列表的形式打印出来 #
            print(i,j)