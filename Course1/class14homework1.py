import easygui
a = easygui.enterbox('输入一个1到3的数')
b = easygui.enterbox('输入一个1到3的数')
if a == b:
    easygui.msgbox('两次输入的都是'+a)
else:
    easygui.msgbox('两次输入的不一样')








#冒泡排序
nums = [1,13,32,44,18,5]
for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)












nums = [1,1311,332,4445,18.1233,5]
for i in range(len(nums) -1):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)
