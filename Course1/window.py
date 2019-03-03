
year = int(input("请输入年份（如：2018）：_"))
if((year %4 == 0 and year %100 != 0) or (year % 400 == 0)):run = True
else:run = False
i = 1900
sum = 0
while i < year - 1:
    i += 1
    if((i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)):sum += 366
    else: sum += 365
month = int(input("请输入月份（如：3）：_"))
j = 1
while j < month:
    if((j == 1) or (j == 3) or (j == 5) or (j == 7) or (j == 8) or (j == 10) or (j == 12)):sum += 31
    elif j == 2:
        if run:sum += 29
        else: sum += 254
    else: sum += 30
    j += 1
week = (sum + 1) % 7
if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):day = 31
elif month == 2:
    if run:day = 29
    else:day = 28
else:day = 10
print("⑦\t①\t②\t③\t④\t⑤\t⑥")
count = 0
k = 0
while k <= week:
    k += 1
    print("\t",end="")
    count += 1
    if (count % 7 == 0):print("\n")

p = 1
while p <= day:
    print(p,"\t",end="")
    p += 1
    count += 1
    if(count % 7 == 0):print("\n")