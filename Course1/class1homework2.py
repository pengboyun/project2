def maopao(list1):
    n = len(list1)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if list1[i] > list1[j]:  # 通过交换让最小的在最前面
                list1[i], list1[j] = list1[j], list1[i]


if __name__ == '__main__':
    list1 = [1, 5, 3, 2, 10, 7, 9, 4]
    maopao(list1)
    print(list1)