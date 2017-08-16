# -*- coding: utf-8 -*-
import glob
import os
import re
import string
import operator
import shutil
import sys
import urllib
import socket
from nt import chdir

# ##########part.1:convert log format##################F
file_path = r'C:\zhaomeng\tag-workspace\accu.balance.921\log.txt'
file_temp_path = r'C:\zhaomeng\tag-workspace\accu.balance.921\log_top5.txt'
file = open(file_path, 'r')
file_temp = open(file_temp_path, 'w')
for line in file.readlines():
    # line = line.strip('\n\t[[')
    line = line.split('\t')
    line_new_ = []
    for kk in range(len(line)):
        if (kk == 10):
            line_new = line[kk][1:-2]
            line_new_.append(line_new)
            file_temp.write(str(line_new) + '\t')
        else:
            if (kk%2):
                line_new = line[kk][1:-1]
                line_new_.append(line_new)
                file_temp.write(str(line_new) + '\t')
            else:
                line_new = line[kk][3:-2]
                line_new_.append(line_new)
                file_temp.write(str(line_new) + '\t')

    file_temp.write('\n')

###########get top-5 > 0.86 tags :Part1#############

file_path = r"C:\zhaomeng\tag-workspace\accu.balance.921\log_top5.txt"
top5_tag_path = r"C:\zhaomeng\tag-workspace\accu.balance.921\temp.txt"
top5_tag_file = open(top5_tag_path,'w')
for line in open(file_path,'r'):
    line = line.strip().split('\t')
    line = line[-1]
    top5_tag_file.write(line + '\n')

# ############get top-5 > 0.86 tags :Part2#############
file_path = r"C:\zhaomeng\tag-workspace\accu.balance.921\temp.txt"
top5_accu_file = open(r"C:\zhaomeng\tag-workspace\accu.balance.921\top5_accu.txt",'w')
tagleaf_path = r"C:\zhaomeng\tag-workspace\accu.balance.921\tags.balance.921.txt"
tagid_path = r"C:\zhaomeng\tag-workspace\accu.balance.921\tagid.1500.txt"
val_label = {}
tagleaf = {}
tagid = {}
for line in open(tagid_path,'r'):
    line = line.strip().split('\t')
    info = []
    info1 = ""
    for i in range(len(line) -3):
        info.append(line[i+2])
        info1 = info1 + line[i+2] + ','
    info1 += line[-1]
    tagid[line[1]] = info1

for line in open(tagleaf_path,'r'):
    line = line.strip().split(' ')
    tagleaf[line[0]] = line[1]

for k in range(921):
    val_label[str(k)] = 0

for line in  open(file_path,'r'):
    line = line.strip().split('\t')
    line = line[0]
    val_label[line] += 1

for tag in val_label.keys():
    # print float(val_label[tag]/50.0)
    accu = float(val_label[tag]/50.0)
    if accu < 50:
        top5_accu_file.write(tag + '\t' + tagleaf[tag] + '\t' + str(val_label[tag]/50.0)  + '\t' + tagid[tagleaf[tag]] + '\t'  + '\n')



###top1-accuracy
file_accu_all = r"C:\zhaomeng\tag-workspace\accu.balance.921\log_top5.txt"
file_top1 = open(r"C:\zhaomeng\tag-workspace\accu.balance.921\temp_top1.txt",'w')

for line in open(file_accu_all,'r'):
    line = line.strip().split('\t')
    if line[1] == line[-1]:
        file_top1.write(line[1] + '\n')

##excel format accu
tags_excel = r"C:\zhaomeng\tag-workspace\accu.test.0110.balance\tags.excel.txt"
top5 = r"C:\zhaomeng\tag-workspace\accu.test.0110.balance\top5_accu.txt"
top5_excel = open(r"C:\zhaomeng\tag-workspace\accu.test.0110.balance\top5_excel.txt",'w')

top5_dict = {}
for line in open(top5,'r'):
    line = line.strip().split('\t')
    if line[1] not in top5_dict.keys():
        top5_dict[line[1]] = line[2]

for line in open(tags_excel,'r'):
    line = line.strip()
    if line != '':
        if line in top5_dict.keys():
            top5_excel.write(line  + '\t' + top5_dict[line] + '\n')
        else:
            top5_excel.write(line + '\n')
    else:
        top5_excel.write(line + '\n')



##wrong info

top5_file = r"C:\zhaomeng\tag-workspace\accu.navigation\accu.navi.relation.v3\log_info_all.txt"
top5_out_file = open(r"C:\zhaomeng\tag-workspace\accu.navigation\accu.navi.relation.v3\log_info_wrong.txt",'w')

flag = 0
for line in open(top5_file,'r'):
    flag = 0
    line = line.strip().split('\t')
    for kk in range(5):
        if line[kk*3 + 1] == line[-3]:
            flag = 1
    if flag == 0:
        for kk in range(len(line)):
            top5_out_file.write(line[kk] + '\t')
        top5_out_file.write('\n')