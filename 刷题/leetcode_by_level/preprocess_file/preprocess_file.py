'''
文件预处理，提前建好文件名（题目编号和题目名称），按难度分为不同的文件夹
/Linklist/easy/x.py x2.py
/Linklist/medium/x.py x2.py
/Linklist/hard/x.py x2.py
'''


# -*- coding:  gbk -*-
import os
import codecs
tag = 'Heapq'
file = '1.txt'
title = ''
prefix = '../' + tag
labels = {'简单': 'easy', '中等': 'medium', '困难': 'hard'}
sub_folder=''
try:
    os.mkdir(prefix)
except OSError:
    pass

with codecs.open(file, 'r',encoding='gbk',errors='strict') as f:
    for line in f.readlines():
        tmp=line.replace('\t\r\n', '').replace('\r\n', '').replace(' ','').split('\t')
        print(tmp)
        if len(tmp) == 1:
            title += tmp[0]
        else:
            name = tmp[0]
            title += '_' + name+'.cpp'
            label_name = tmp[-1]
            try:
                sub_folder = prefix + '/' + labels[label_name]
                os.mkdir(sub_folder)
            except OSError:
                pass
            new_py_path = sub_folder+'/'+title
            x=open(new_py_path,'a+')
            x.close()
            title = ''
