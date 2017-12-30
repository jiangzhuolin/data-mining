# -*- coding:utf-8 -*-


def test(tar):
    '''
    测试欧几里德距离算法
    :param tar:
    :return:
    '''
    a = [1, 3, 2, 3, 4, 3]

    distance = sum((a[i] - tar[i]) ** 2 for i in range(len(a)))

    standard_deviation = 1 / (1 + distance ** .5)
    print(standard_deviation)

b = [1, 3, 4, 3, 2, 3]
c = [5, 1, 4, 9, 8, 6]
test(c)
