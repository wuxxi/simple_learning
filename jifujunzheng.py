#! usr/bin/env python
# -*- coding=utf-8 -*-

try:
    n=int(input())
    initial_list = input()
    initial_list = list(map(int,initial_list.split()))
    print(initial_list)
    rea_num = 0
    fake_num = 0
    rea_sum = 0
    for i in initial_list:
        i = int(i)
        if i < 0:
            fake_num += 1
        elif i > 0:
            rea_num += 1
            rea_sum += i
        else :
            print('to')
            pass
    print("{0} {1:.1f}".format(fake_num,rea_sum/rea_num))
except:
    pass

