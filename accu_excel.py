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

tag_excel = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\tag_excel.txt"
tag_accu = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\top5_accu_all_relation.txt"
accu_excel = open(r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\accu.exel_top5_relation.txt",'w')


accu_dict = {}
for line in open(tag_accu,'r'):
    line = line.strip().split('\t')
    accu_dict[line[1]] = line[2]

for line in open(tag_excel,'r'):
    line  = line.strip()
    if line in accu_dict.keys():
        accu_excel.write(line + '\t' + accu_dict[line] + '\n')
    elif line == '':
        accu_excel.write('\n')
    else:
        accu_excel.write(line + '\t' + str(0) + '\n')