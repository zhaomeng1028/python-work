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
#from nt import chdir
from collections import defaultdict
# import matplotlib.pyplot as plt # plt 用于显示图片
# import matplotlib.image as mpimg # mpimg 用于读取图片
# import numpy as np
import time
import sys

# #count number
# synsetlist = open(r"I:\Image_20170227_zhaomeng_n64\n64_count.txt",'w')
#
# imdir = r"I:\Image_20170227_zhaomeng_n64\imagenet_selected_n64"
#
# suffix = '_'
#
# for file in glob.glob(imdir + '\\' + '*'):
#     file = file.split('\\')[-1]
#     if not file.endswith(suffix):
#         ims = glob.glob(imdir + '\\' + file + '\\' + '*.JPEG')
#         synsetlist.write(file + '\t' + str(len(ims)) + '\n')


# ####create_coco_lst#######
# imlist_train_dir = r"I:\Image_20170227_zhaomeng_n64\mscoco\coco\PythonAPI\listinfo_train"
# imlist_val_dir = r"I:\Image_20170227_zhaomeng_n64\mscoco\coco\PythonAPI\listinfo_val"
# imlist_train = open(r"I:\Image_20170227_zhaomeng_n64\mscoco\coco\imlist_train.txt",'w')
# imlist_val = open(r"I:\Image_20170227_zhaomeng_n64\mscoco\coco\imlist_val.txt",'w')
# synset_list = open(r"I:\Image_20170227_zhaomeng_n64\mscoco\coco\synset.txt",'w')
#
# count = 0
# for file in glob.glob(imlist_train_dir + '\\' + '*.txt'):
#     file_name = file.split('\\')[-1]
#     file_name = file_name.split('.')[0]
#     synset_list.write(file_name.split('_')[1] + '\t' + file_name.split('_')[0] + '\n')
#     for line in open(file,'r'):
#         line = line.strip()
#         imlist_train.write(str(count) + '\t' + str(file_name.split('_')[1]) + '\t' + line + '\n')
#         count += 1
#
# count = 0
# for file in glob.glob(imlist_val_dir + '\\' + '*.txt'):
#     file_name = file.split('\\')[-1]
#     file_name = file_name.split('.')[0]
#     for line in open(file,'r'):
#         line = line.strip()
#         imlist_val.write(str(count) + '\t' + str(file_name.split('_')[1]) + '\t' + line + '\n')
#         count += 1


# ####top-5000-left############
# synset_file = r"I:\Image_20170227_zhaomeng_n64\synset_subset.zmeng.20170320.txt"
# imdir_done = r"I:\Image_20170227_zhaomeng_n64\imagenet_selected_n64"
# imdir_5000 = r"I:\Image_20170227_zhaomeng_n64\top_5000_img"
# imdir_5000_left = r"I:\Image_20170227_zhaomeng_n64\top_5000_img_left"
#
# synset_list = defaultdict(list)
# for line in open(synset_file,'r'):
#     line = line.strip()
#     for img in glob.glob(imdir_done + '\\' + line + '\\' + '*.JPEG'):
#         synset_list[line].append(img.split('\\')[-1])
#
# for synset in synset_list.keys():
#     for img in glob.glob(imdir_5000 + '\\' + synset + '\\' + '*.JPEG'):
#         if not os.path.exists(imdir_5000_left + '\\' + synset):
#             os.makedirs(imdir_5000_left + '\\' + synset)
#         if img.split('\\')[-1] not in synset_list[synset]:
#             src = img
#             dst = imdir_5000_left + '\\' + synset + '\\' + img.split('\\')[-1]
#             shutil.copy(src,dst)


# ########敏感标签id转换#####
# synset = r"I:\sharedCentOS\resnet-924-152\synset_924.txt"
# convert_accu = r"I:\sharedCentOS\resnet-924-152\accu.convert.txt"
# convert_tagid  = open(r"I:\sharedCentOS\resnet-924-152\convert_924.txt",'w')
#
# synset_id = {}
# for line in open(synset,'r'):
#     line = line.strip().split(' ')
#     synset_id[line[1]] = line[0]
#
# for line in open(convert_accu,'r'):
#     line = line.strip().split('\t')
#     for kk in range(len(line)):
#         convert_tagid.write(synset_id[line[kk]] + '\t')
#     convert_tagid.write('\n')
#
# ###imclean_list
# imlist = open(r"I:\Image_20170227_zhaomeng_n64\imlist_clean.zmeng.20170324_.txt",'w')
# synsetlist = open(r"I:\Image_20170227_zhaomeng_n64\synset_subset.zmeng.20170324_.txt",'w')
#
# imdir = r"I:\Image_20170227_zhaomeng_n64\imagenet_update_0324"
#
# suffix = '_'
#
# for file in glob.glob(imdir + '\\' + '*'):
#     file = file.split('\\')[-1]
#     if not file.endswith(suffix):
#         synsetlist.write(file + '\n')
#         for ims in glob.glob(imdir + '\\' + file + '\\' + '*'):
#             im = ims.split('\\')[-1]
#             im = im.split('_')
#             if len(im)>2 and im[1].startswith('n'):
#                 im_write = ims
#             imlist.write(file + '/' + ims.split('\\')[-1] + '\n')
#
# ###get new update imgs
# imlist_v2 = r"I:\Image_20170227_zhaomeng_n64\imlist_clean.zmeng.20170320.txt"
# imlist_v3 = r"I:\Image_20170227_zhaomeng_n64\imlist_clean.zmeng.20170324.txt"
# imdir = r"I:\Image_20170227_zhaomeng_n64\openimgs_selected_n64_23"
# imdir_update = r"I:\Image_20170227_zhaomeng_n64\openimgs_update_n64_23"
#
# list_v2 = []
# for line in open(imlist_v2,'r'):
#     line = line.strip()
#     list_v2.append(line)
#
# i = 0
# for line in open(imlist_v3,'r'):
#     line = line.strip()
#     if line not in list_v2:
#         i += 1
#         src = imdir + '\\' + line.split('/')[0] + '\\' + line.split('/')[1]
#         if not os.path.exists(imdir_update + '\\' + line.split('/')[0]):
#             os.makedirs(imdir_update + '\\' + line.split('/')[0])
#         dst = imdir_update + '\\' + line.split('/')[0] + '\\' + line.split('/')[1]
#         shutil.copy(src,dst)
#
# print i


# #############2017-0327###############
# synset_917 = r"I:\Image_20170227_zhaomeng_n64\synset_917.txt"
# tag_1506_eng = r"I:\Image_20170227_zhaomeng_n64\tag_1506_eng.txt"
# synset_metadata = open(r"I:\Image_20170227_zhaomeng_n64\synset_917_metadata.txt",'w')
#
# tag_dict = {}
# for line in open(tag_1506_eng):
#     line = line.strip().split('\t')
#     tag_dict[line[0]] = line[1]
#
# for line in open(synset_917,'r'):
#     line = line.strip()
#     synset_metadata.write(line + '\t' + tag_dict[line] + '\n')



##20170406########


######Caption2Multilabel####################
# ####Part1.get list##########
# imdir_name = r"I:\Image_20170227_zhaomeng_n64\caption2synset\COPY\tagName"
# imdir_id = r"I:\Image_20170227_zhaomeng_n64\caption2synset\COPY\tagId"
# file_zh = r"I:\Image_20170227_zhaomeng_n64\caption2synset\COPY\tag_zh.txt"
# file_list = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\COPY\img_info.txt",'w')
#
# files = os.listdir(imdir_name)
#
# tag_zh = {}
# for line in open(file_zh,'r'):
#     if line != '':
#         line = line.strip().split('\t')
#         tag_zh[line[0]] = line[1]
#
# for file in files:
#     print file
#     file_base = file[:-8]
#     file_list.write(file_base + '\t')
#     for line in open(imdir_name + '\\' + file_base + '.tagname','r'):
#         name = line.strip()
#         name = name[4:-5]
#         file_list.write(str(name) + '\t')
#     for line in open(imdir_id + '\\' + file_base + '.tagid', 'r'):
#         id = line.strip()
#         id = id[4:-5]
#         file_list.write(str(id) + '\t')
#
#         if id != '':
#             id_list = id.split(',')
#             for per_id in id_list:
#                 file_list.write(tag_zh[per_id] + ',')
#     file_list.write('\n')


# #############Part2.show image###############
# show_pic = r"I:\Image_20170227_zhaomeng_n64\caption2synset\COPY\show_img.txt"
# imdir = r"I:\Image_20170227_zhaomeng_n64\mscoco\train2014"
# count = 1
# for line in open(show_pic,'r'):
#     line = line.strip()
#     line = line[:-4]
#     pic_dir = imdir + '\\' + line
#     pic = mpimg.imread(pic_dir)
#     plt.imshow(pic) # 显示图片
#     plt.axis('off') # 不显示坐标轴
#     plt.title(str(count))
#     count += 1
#     plt.pause(3)
#     plt.close()



# #########20170411##################
# tag_894 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_894.txt"
# tag_1505 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_1505.txt"
#
# tag_1505_flag = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_1505_flag.txt",'w')
#
# tag894 = []
# for line in open(tag_894,'r'):
#     line = line.strip()
#     if line != ' ':
#         tag894.append(line)
#
#
# for line in open(tag_1505,'r'):
#     line = line.strip()
#     if line in tag894:
#         tag_1505_flag.write(line + '\t' + 'T\n')
#     else:
#         tag_1505_flag.write(line + '\t' + 'F\n')

##################20170412###############

# file_dir = r"I:\Image_20170227_zhaomeng_n64\mscoco\coco\PythonAPI\listinfo_val"
# img2tags = open(r"I:\Image_20170227_zhaomeng_n64\im2txt\val_list.txt",'w')
#
# imgdict = defaultdict(list)
# categorys = glob.glob(file_dir + '\\' + '*.txt')
# for category in categorys:
#     category = category.strip().split('\\')[-1]
#     cate_name = category.split('_')[0]
#     for line in open(file_dir + '\\' + category,'r'):
#         line = line.strip()
#         imgdict[line].append(cate_name)
#
# for img in imgdict.keys():
#     img2tags.write(img + '\t')
#     for kk in range(len(imgdict[img])):
#         img2tags.write(imgdict[img][kk] + '\t')
#     img2tags.write('\n')
#
# list_train = r"I:\Image_20170227_zhaomeng_n64\im2txt\train_list.txt"
# list_val = r"I:\Image_20170227_zhaomeng_n64\im2txt\val_list.txt"
# id_train = r"I:\Image_20170227_zhaomeng_n64\im2txt\image_id_train.txt"
# id_val = r"I:\Image_20170227_zhaomeng_n64\im2txt\image_id_val.txt"
# list_train_new = open(r"I:\Image_20170227_zhaomeng_n64\im2txt\train_list_new.txt",'w')
# list_val_new = open(r"I:\Image_20170227_zhaomeng_n64\im2txt\val_list_new.txt",'w')
#
# id_train_dict = {}
# id_val_dict = {}
# for line in open(id_train,'r'):
#     line = line.strip().split('\t')
#     id_train_dict[line[0]] = line[1]
#
# for line in open(id_val,'r'):
#     line = line.strip().split('\t')
#     id_val_dict[line[0]] = line[1]
#
# for line in open(list_train,'r'):
#     line = line.strip().split('\t')
#     id = id_train_dict[line[0]]
#     list_train_new.write(id + '\t')
#     for kk in range(len(line)):
#         list_train_new.write(line[kk] + '\t')
#     list_train_new.write('\n')
#
# for line in open(list_val,'r'):
#     line = line.strip().split('\t')
#     id = id_val_dict[line[0]]
#     list_val_new.write(id + '\t')
#     for kk in range(len(line)):
#         list_val_new.write(line[kk] + '\t')
#     list_val_new.write('\n')


######20170417##########
###Caption2Multilabel####################
##Part1.get list##########
# imdir_name = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\v4-0424\tagName"
# imdir_id = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\v4-0424\tagId"
# file_zh = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\v4-0424\tag_zh.txt"
# file_list = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\v4-0424\img_info.txt",'w')
#
# files = os.listdir(imdir_name)
#
# tag_zh = {}
# for line in open(file_zh,'r'):
#     if line != '':
#         line = line.strip().split('\t')
#         tag_zh[line[0]] = line[1]
#
# for file in files:
#     print file
#     file_base = file[:-8]
#     file_list.write(file_base + '\t')
#     for line in open(imdir_name + '\\' + file_base + '.tagname','r'):
#         name = line.strip()
#         name = name[4:-5]
#         file_list.write(str(name) + '\t')
#     for line in open(imdir_id + '\\' + file_base + '.tagid', 'r'):
#         id = line.strip()
#         id = id[4:-5]
#         file_list.write(str(id) + '\t')
#
#         if id != '':
#             id_list = id.split(',')
#             for per_id in id_list:
#                 file_list.write(tag_zh[per_id] + '--')
#     file_list.write('\n')


# #############Part2.show image###############
# show_pic = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v2\show_img.txt"
# imdir = r"I:\Image_20170227_zhaomeng_n64\mscoco\train2014"
# count = 1
# for line in open(show_pic,'r'):
#     line = line.strip()
#     line = line[:-4]
#     pic_dir = imdir + '\\' + line
#     pic = mpimg.imread(pic_dir)
#     plt.imshow(pic) # 显示图片
#     plt.axis('off') # 不显示坐标轴
#     plt.title(str(count))
#     count += 1
#     plt.pause(4)
#     plt.close()

# ####top50 with captions#############
# img_info = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\img_info_50.txt"
# imdir_caption = r"I:\Image_20170227_zhaomeng_n64\caption2synset\capions_50"
# img_info_caption = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\img_info_caption_50.txt",'w')
#
#
# for line in open(img_info,'r'):
#     line = line.strip()
#     filename = line.split('\t')[0]
#     img_info_caption.write(line + '\n')
#     for captions in open(imdir_caption + '\\' + filename,'r'):
#         img_info_caption.write('\t' + captions)

# #######20170418#############
# #
# tag_894 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\synset_894.txt"
# img_info = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\img_info_500.txt"
# file_zh = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_zh_894.txt"
# img_info_894 = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\img_info_500_894.txt",'w')
#
# tag_zh = {}
# for line in open(file_zh,'r'):
#     if line != '':
#         line = line.strip().split('\t')
#         tag_zh[line[0]] = line[1]
#
# tag_894_list = []
# for line in open(tag_894,'r'):
#     line = line.strip()
#     tag_894_list.append(line)
#
# for line in open(img_info,'r'):
#     line = line.strip().split('\t')
#     synset_info = line[2].split(',')
#     synset_info_new = []
#     for synset in synset_info:
#         if synset in tag_894_list:
#             synset_info_new.append(synset)
#     if len(synset_info_new) != 0 :
#         img_info_894.write(line[0] + '\t')
#
#         for kk in range(len(synset_info_new) - 1):
#             img_info_894.write(synset_info_new[kk] + ',')
#         img_info_894.write(synset_info_new[-1] + '\t')
#
#         for kk in range(len(synset_info_new) - 1):
#             img_info_894.write(tag_zh[synset_info_new[kk]] + '--')
#         img_info_894.write(tag_zh[synset_info_new[-1]] + '\n')
#     else:
#         img_info_894.write(line[0] + '\n')


# ############20170419#############
#
# tag_894 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_894_flag.txt"
# tag_1505 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_1505.txt"
#
# tag_1505_flag = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_1505_flag.txt",'w')
#
# tag894_flag = {}
# for line in open(tag_894,'r'):
#     line = line.strip().split('\t')
#     tag894_flag[line[0]] = line[1]
#
#
# for line in open(tag_1505,'r'):
#     line = line.strip()
#     if line in tag894_flag.keys():
#         tag_1505_flag.write(line + '\t' + tag894_flag[line] + '\n')
#     else:
#         tag_1505_flag.write(line + '\t' + '2\n')


# ####add tag_zh_894 to tag_zh#############
#
# tag_zh = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_zh_1505.txt"
# tag_zh_894 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_zh_894.txt"
# tag_zh_new = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_zh_1505_update.txt",'w')
#
# tag_894_dict = {}
# for line in open(tag_zh_894,'r'):
#     line = line.strip().split('\t')
#     tag_894_dict[line[0]] = line[1]
#
# for line in open(tag_zh,'r'):
#     tag = line.strip().split('\t')[0]
#     if tag in tag_894_dict.keys():
#         tag_zh_new.write(tag + '\t' + tag_894_dict[tag] + '\n')
#     else:
#         tag_zh_new.write(line)

##########20170424###############

# ###创建基于885类的新tag列表，包括翻译及优先级（0-4）##
# info_885 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\v4-0424\tag_885.txt"
# tag_zh_1505 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\v4-0424\tag_zh.txt"
# info_1505 = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\v4-0424\info_1505.txt",'w')
#
# tag_885 = []
# for line in open(info_885,'r'):
#     line = line.strip().split('\t')[0]
#     print line
#     tag_885.append(line)
#
# for line in open(tag_zh_1505,'r'):
#     line = line.strip().split('\t')
#     if line[0] not in tag_885:
#         info_1505.write(line[0] + '\t' + line[1] + '\t4\n')
#
# for line in open(info_885,'r'):
#     info_1505.write(line)



# #####映射标签至885类##############
# tag_885 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\v4-0424\tag_885.txt"
# img_info = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\v4-0424\img_info_500.txt"
# img_info_885 = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\v4-0424\img_info_500_885.txt",'w')
#
# tag885_zh = {}
# for line in open(tag_885,'r'):
#     line = line.strip().split('\t')
#     tag885_zh[line[0]] = line[1]
#
# for line in open(img_info,'r'):
#     line = line.strip().split('\t')
#     synset_info = line[2].split(',')
#     synset_info_new = []
#     for synset in synset_info:
#         if synset in tag885_zh.keys():
#             synset_info_new.append(synset)
#     if len(synset_info_new) != 0 :
#         img_info_885.write(line[0] + '\t')
#
#         for kk in range(len(synset_info_new) - 1):
#             img_info_885.write(synset_info_new[kk] + ',')
#         img_info_885.write(synset_info_new[-1] + '\t')
#
#         for kk in range(len(synset_info_new) - 1):
#             img_info_885.write(tag885_zh[synset_info_new[kk]] + '--')
#         img_info_885.write(tag885_zh[synset_info_new[-1]] + '\n')
#     else:
#         img_info_885.write(line[0] + '\n')


##############20170425###########
##简单的过滤词频试验###
# ##part1:第一种方式，直接过滤重复words
# sentence_ori = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\sentencetonoun_0421.txt"
# sentence_out = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\sentence_delete_repeat.txt",'w')
#
# for line in open(sentence_ori,'r'):
#     line = line.strip().split('    ')
#     img = line[0]
#     words = line[1].split(',')
#     wors_f = {}
#     for word in words:
#         if word not in wors_f.keys():
#             wors_f[word] = 1
#         else:
#             wors_f[word] += 1
#     sentence_out.write(img + '\t')
#     for word in wors_f.keys():
#         if wors_f[word] > 1:
#             sentence_out.write(word + ',')
#     sentence_out.write('\n')


# ###part2：制作vocab词库
#
# vocab = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\tag2words.txt"
# vocab_all = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\vocab.txt",'w')
#
# vocab_dict = {}
# for line in open(vocab,'r'):
#     line = line.strip('\n').split('\t')
#     tag = line[0]
#     vocab_dict[tag] = []
#     for kk in range(len(line) - 1):
#         voc = line[kk + 1].split(',')
#         for word in voc:
#             if word != '':
#                 vocab_dict[tag].append(word)
#
# for tag in vocab_dict.keys():
#     vocab_all.write(tag + '\t')
#     for kk in range(len(vocab_dict[tag]) - 1):
#         vocab_all.write(vocab_dict[tag][kk] + ',')
#     vocab_all.write(vocab_dict[tag][-1] + '\n')


# ###part 3:映射到tag,并找出没有匹配上的单词和词频
# sentence = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\sentence_delete_repeat.txt"
# vocab = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\vocab.txt"
# sentence_id = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\sentence_delete_repeat_id.txt",'w')
# words_not_in_vocab = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\words_not_in_vocab.txt",'w')
#
# vocab_dict = {}
# for line in open(vocab,'r'):
#     line = line.strip().split('\t')
#     tag = line[0]
#     words = line[1].split(',')
#     for word in words:
#         if word not in vocab_dict.keys():
#             vocab_dict[word] = []
#         vocab_dict[word].append(tag)
#
# word_not_in = {}
# count = 0
# for line in open(sentence,'r'):
#     count += 1
#     print str(count)
#     line = line.strip().split('\t')
#     img = line[0]
#     if len(line)>1:
#         words = line[1].split(',')
#         sentence_id.write(img + '\t')
#         for word in words:
#             if word != '':
#                 if word in vocab_dict.keys():
#                     for kk in range(len(vocab_dict[word])):
#                         sentence_id.write(vocab_dict[word][kk] + ',')
#                     # sentence_id.write('---')
#                 # sentence_id.write('\n')
#                 else:
#                     if word not in word_not_in.keys():
#                         word_not_in[word]  = 1
#                     else:
#                         word_not_in[word] += 1
#         sentence_id.write('\n')
#     else:
#         sentence_id.write(img + '\n')
#
# for word in word_not_in.keys():
#     words_not_in_vocab.write(word + '\t' + str(word_not_in[word]) + '\n')


# ####part 4:组合全部info
# info_1505 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\info_1505.txt"
# info_name = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\sentence_delete_repeat.txt"
# info_id = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\sentence_delete_repeat_id.txt"
# sentence_info = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\sentence_info.txt",'w')
#
# tag_zh_885 = {}
# for line in open(info_1505,'r'):
#     line = line.strip().split('\t')
#     if line[-1]!= str(4):
#         tag_zh_885[line[0]] = line[1]
# print len(tag_zh_885)
#
# name_list = {}
# for line in open(info_name,'r'):
#     line = line.strip().split('\t')
#     if len(line) > 1 :
#         name_list[line[0]] = line[1]
#     else:
#         name_list[line[0]] = ''
#
#
# for line in open(info_id,'r'):
#     line = line.strip().split('\t')
#     if len(line) > 1:
#         sentence_info.write(line[0] + '\t' + name_list[line[0]] + '\t')
#         tags_ori = line[1].split(',')
#         tags_new = []
#         for tag in tags_ori:
#             if tag in tag_zh_885.keys():
#                 tags_new.append(tag)
#         for tag in tags_new:
#             sentence_info.write(tag + ',')
#         sentence_info.write('\t')
#         for tag in tags_new:
#             sentence_info.write(tag_zh_885[tag] + '---')
#         sentence_info.write('\n')
#     else:
#         sentence_info.write(line[0] + '\t' + name_list[line[0]] + '\n')



##############20170425###########

# ##给词表添加层级结构###
# vocab = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\vocabulary_add_similarity0.5_v2_0425.txt"
# hierarchical_885 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\hierarchical_885.txt"
#
# vocab_hierarchical = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v1\vocab_hierarchical_885.txt",'w')
#
# vocab_dict = {}
# for line in open(vocab,'r'):
#     tag = line.strip().split('\t')[1]
#     vocab_dict[tag] = line.strip()
#
# for line in open(hierarchical_885,'r'):
#     if line.strip() != '':
#         tag = line.strip().split('\t')[0]
#         vocab_hierarchical.write(line.strip() + '\t' + vocab_dict[tag] + '\n')
#     else:
#         vocab_hierarchical.write('\n')


# ###产生885个词库########
# vocab_1505 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v2\vocab_1505.txt"
# info_1505 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v2\info_1505.txt"
# vocab_885 = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v2\vocab_885.txt",'w')
# info = {}
# for line in open(info_1505,'r'):
#     line = line.strip().split('\t')
#     info[line[0]] = line[2]
#
# for line in open(vocab_1505,'r'):
#     tag = line.strip().split('\t')[0]
#     if info[tag] != '4':
#         vocab_885.write(line)

# ###第二种方式，过滤映射的标签频率##
# sentence = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v2\sentencetonoun_0421_1000.txt"
# vocab = r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v2\vocab_1505.txt"
# sentence_to_tag = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\delete_repeat_v2\sentence_to_tag_1505.txt",'w')
#
# vocab2tag = {}
# tag_zh = {}
# for line in open(vocab,'r'):
#     line = line.strip().split('\t')
#     for kk in range(len(line) - 2):
#         words = line[kk + 2]
#         if (words!= ''):
#             words = words.split(',')
#             for word in words:
#                 if word != '':
#                     if word in vocab2tag.keys():
#                         vocab2tag[word].append(line[0])
#                     else:
#                         vocab2tag[word] = []
#                         vocab2tag[word].append(line[0])
#     tag_zh[line[0]] = line[1]
#
# count = 0
# for line in open(sentence,'r'):
#     count += 1
#     print str(count)
#     words_frequency = {}
#     line = line.strip().split('    ')
#     words = line[1]
#     if words != '':
#         words = words.split(',')
#         for word in words:
#             if word in vocab2tag.keys():
#                 tags = vocab2tag[word]
#                 for tag in tags:
#                     if tag not in words_frequency.keys():
#                         words_frequency[tag] = 1
#                     else:
#                         words_frequency[tag] += 1
#
#     sentence_to_tag.write(line[0] + '\t')
#     words_f_bitter_than_two = []
#     for tag in words_frequency.keys():
#         if words_frequency[tag]>1:
#             words_f_bitter_than_two.append(tag)
#
#     for kk in range(len(words_f_bitter_than_two)):
#         sentence_to_tag.write(words_f_bitter_than_two[kk] + ',')
#     sentence_to_tag.write('\t')
#     for kk in range(len(words_f_bitter_than_two)):
#         sentence_to_tag.write(tag_zh[words_f_bitter_than_two[kk]] + '--')
#     sentence_to_tag.write('\n')



# ####2017-05-02#####
#
# import matplotlib.pyplot as plt # plt 用于显示图片
# import matplotlib.image as mpimg # mpimg 用于读取图片
# import numpy as np
# import time
#
# pic = "/mnt/hgfs/I/sharedCentOS/review_val_img_0503/test.txt"
# imdir = "/mnt/hgfs/I/sharedCentOS/review_val_img_0503/n03773035"
# count = 1
# for line in open(pic,'r'):
#     line = line.strip()
#     pic_dir = imdir + '/' + line
#     pic = mpimg.imread(pic_dir)
#     plt.imshow(pic) # 显示图片
#     plt.axis('off') # 不显示坐标轴
#     plt.title(str(line))
#     count += 1
#     plt.pause(3)
#     plt.close()


# ####3017-05-08####
# #im2txt detection precision/recall##
# val_list = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/im2txt/detection_PR/val_list.txt'
# result = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/im2txt/detection_PR/output.log'
# words_label = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/im2txt/detection_PR/word_counts.txt'
#
# ##get labels
# labels = {}
#
# for num,line in enumerate(open(words_label,'r')):
#     line = line.strip().split(' ')
#     if len(line) > 2:
#         labels[line[0] + ' ' + line[1]] = num
#     else:
#         labels[line[0]] = num
#
#
# ##load file
# img_union = []
# img_gt = {}
# img_result = {}
#
# for line in open(val_list,'r'):
#     line = line.strip().split('\t')
#     img_gt[line[0]] = []
#     for kk in range(len(line) - 1):
#         img_gt[line[0]].append(labels[line[kk + 1]])
#
# for line in open(result,'r'):
#     line = line.strip().split('\t')
#     img_result[line[0]] = []
#     for kk in range(len(line) - 1):
#         # img_result[line[0]].append(labels_[line[kk + 1]])
#         img_result[line[0]].append(line[kk + 1])
#
# ##get tag union
# # img_union = [img for img in img_gt.keys() if img in img_result.keys()]
# img_union = list(set(img_gt.keys()) & set(img_result.keys()))
#
# ##get gt_mat and result_mat
# nclassess = len(labels)
# gt_mat=np.zeros((len(img_union),nclassess),dtype=bool)
# result_mat=np.zeros((len(img_union),nclassess),dtype=bool)
# count = 0
# for img in img_union:
#     cls_gt_list = img_gt[img]
#     cls_result_list = img_result[img]
#     for cls in cls_gt_list:
#         gt_mat[count,int(cls)]=True
#     for cls in cls_result_list:
#         result_mat[count, int(cls)] = True
#     count += 1
#
#
# tp_mat = gt_mat*result_mat
#
# tp_cls = np.sum(tp_mat,axis = 0)[2:]
# tp_fp_cls = np.sum(result_mat,axis = 0)[2:]
# tp_fn_cls = np.sum(gt_mat,axis = 0)[2:]
#
# pre_cls = tp_cls.astype(np.float32)/tp_fp_cls.astype(np.float32)
# rec_cls = tp_cls.astype(np.float32)/tp_fn_cls.astype(np.float32)
#
# pre_avg = np.sum(pre_cls[2:])/(nclassess-2)
# rec_avg = np.sum(rec_cls[2:])/(nclassess-2)
#
# for cls in range(nclassess - 2):
#     print "cls " + str(cls + 1) + ': precision ' + str(pre_cls[cls]) + ' recall ' + str(rec_cls[cls])
#
# print "pre_avg = " + str(pre_avg)
# print "rec_avg = " + str(rec_avg)



# ##im2txt detection precision/recall##
#
# def loadFile(file_name,label_name,convert = False):
#     #load labels
#     labels = {}
#     for num, line in enumerate(open(label_name, 'r')):
#         line = line.strip().split(' ')
#         if len(line) > 2:
#             labels[line[0] + ' ' + line[1]] = num
#         else:
#             labels[line[0]] = num
#     #load files
#     img_info = {}
#     for line in open(file_name, 'r'):
#         line = line.strip().split('\t')
#         img_info[line[0]] = []
#         for word in range(len(line) - 1):
#             if convert:
#                 img_info[line[0]].append(labels[line[word + 1]])
#             else:
#                 img_info[line[0]].append(line[word + 1])
#
#     return img_info
#
# def imgUnion(result_dict,gt_dict):
#
#     return list(set(gt_dict.keys()) & set(result_dict.keys()))
#
#
# def getPRArray(gt_info,result_info,img_union):
#
#     ##get gt_mat and result_mat
#     gt_mat = np.zeros((len(img_union), nclassess), dtype=bool)
#     result_mat = np.zeros((len(img_union), nclassess), dtype=bool)
#     count = 0
#     for img in img_union:
#         cls_gt_list = gt_info[img]
#         cls_result_list = result_info[img]
#         for cls in cls_gt_list:
#             gt_mat[count, int(cls)] = True
#         for cls in cls_result_list:
#             result_mat[count, int(cls)] = True
#         count += 1
#
#     tp_mat = gt_mat * result_mat
#
#     tp_cls = np.sum(tp_mat, axis=0)[2:]
#     tp_fp_cls = np.sum(result_mat, axis=0)[2:]
#     tp_fn_cls = np.sum(gt_mat, axis=0)[2:]
#
#     pre_cls = tp_cls.astype(np.float32) / tp_fp_cls.astype(np.float32)
#     rec_cls = tp_cls.astype(np.float32) / tp_fn_cls.astype(np.float32)
#
#     return pre_cls,rec_cls
#
#
# def avgPR(result_file,gt_file,label_file,clsinfo = True):
#
#     ##load file
#     img_gt = loadFile(gt_file,label_file,convert=True)
#     img_result = loadFile(result_file,label_file)
#
#     ##get image union
#     img_union = imgUnion(img_result,img_gt)
#
#     ##get pre,rec info for all cls
#     [pre_cls,rec_cls] = getPRArray(img_gt,img_result,img_union)
#     if clsinfo:
#         for cls in range(nclassess - 2):
#             print "cls " + str(cls + 1) + ': precision ' + str(pre_cls[cls]) + ' recall ' + str(rec_cls[cls])
#
#     pre_avg = np.sum(pre_cls[2:])/(nclassess-2)
#     rec_avg = np.sum(rec_cls[2:])/(nclassess-2)
#
#     return pre_avg,rec_avg
#
# if __name__ == '__main__':
#     result = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/im2txt/detection_PR/output.log'
#     val_list = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/im2txt/detection_PR/val_list.txt'
#     words_label = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/im2txt/detection_PR/word_counts.txt'
#
#     nclassess = 82
#     [pre_avg,rec_avg] = avgPR(result,val_list,words_label,clsinfo = False)
#
#     print "pre_avg = " + str(pre_avg)
#     print "rec_avg = " + str(rec_avg)



# ####2017-05-09#####
# ##compare imListTrain and imListVal
# train_lst = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/review_train_img_0503/imListTrain.txt'
# val_lst = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/review_train_img_0503/imListVal.txt'
#
# val = []
# train = []
# for line in open(val_lst,'r'):
#     line = line.strip().split('\t')[-1]
#     val.append(line)
#
# for line in open(train_lst,'r'):
#     line = line.strip().split('\t')[-1]
#     train.append(line)
#
# lstunion = list(set(val) & set(train))
#
# print len(lstunion)


# ##2017-06-07#######
# ###验证集结果分析
# log_file = r"I:\Image_20170227_zhaomeng_n64\validation_analysis\log_total.txt"
# threshold_file = r"I:\Image_20170227_zhaomeng_n64\validation_analysis\threshold.txt"
# tagid_file = r"I:\Image_20170227_zhaomeng_n64\validation_analysis\tagid.txt"
# imlist_file = r"I:\Image_20170227_zhaomeng_n64\validation_analysis\imListVal_gt_899.txt"
# synset_file = r"I:\Image_20170227_zhaomeng_n64\validation_analysis\synset.txt"
#
# analysis_dir = r"I:\Image_20170227_zhaomeng_n64\validation_analysis\badcase\n03815615_领带"
#
# IMG_CUT = True
# img_cut_convert = {}
# topk = 5
# clsnum = 899
# analysis_result_file = open(r"I:\Image_20170227_zhaomeng_n64\validation_analysis\analysis_info_n03815615_领带.txt",'w',encoding='utf-8')
#
# ###convert analysis_tag to classID###
# classID = {}
# for clsID,line in enumerate(open(synset_file,'r')):
#     line = line.strip('\n').split(' ')
#     classID[line[1]] = clsID
# analysis_img = []
# imgs = glob.glob(analysis_dir + '\\' + '*')
# for img in imgs:
#     img_save = img.split('\\')[-1]
#     if IMG_CUT:
#         img_cut = img.split('-')[-1]
#         img_cut_convert[img_cut] = img_save
#         img_save = img_cut
#     analysis_img.append(img_save)
#
#     # analysis_img.append(img.split('\\')[-1])
#
# ###get chinese if tag###
# tag_ch = {}
# for line in open(tagid_file,'r',encoding='utf-8'):
#     line = line.strip().split(',')
#     if line[1] in classID.keys():
#         tag_ch[classID[line[1]]] = line[2].strip('"')
#
# ###get threshold file###
# threshold = []
# for line in open(threshold_file,'r'):
#     line = line.strip().split('\t')
#     threshold.append(float(line[1]))
#
# # ###get imlist and log of analysis_tag###
# log_info = np.loadtxt(log_file)
#
# # type = sys.getfilesystemencoding()
# analysis_info = {}
# count = 0
# for line in open(imlist_file,'r'):
#     line = line.strip('\n').split('\t')
#     if line[1] in analysis_img:
#         count += 1
#         if IMG_CUT:
#             img_name = img_cut_convert[line[1]]
#         else:
#             img_name = line[1]
#         analysis_result_file.write(str(count) + '\t' + img_name)
#         for kk in range(len(line) - 2):
#             analysis_result_file.write('\t' + line[kk+2] + '\t' + tag_ch[int(line[kk+2])] + '\t')
#         analysis_result_file.write('\n')
#         analysis_result_file.write('\t')
#
#         accuracy = log_info[int(line[0])]
#         sorted_accuracy = np.argsort(accuracy)
#         for kk in range(topk):
#             num = clsnum - 1 - kk
#             analysis_result_file.write('\t' + str(sorted_accuracy[num]) + '\t' + tag_ch[sorted_accuracy[num]] + '\t' + str(accuracy[sorted_accuracy[num]]))
#             # analysis_result_file.write('\t' + tag_ch[sorted_accuracy[kk]])
#         analysis_result_file.write('\n')
#         analysis_result_file.write('\t')
#
#         thres_pred = accuracy-np.array(threshold)
#         thres_pred_cls = np.where(thres_pred>0)
#         for kk in range(len(thres_pred_cls[0])):
#             analysis_result_file.write('\t' + str(thres_pred_cls[0][kk]) + '\t' + tag_ch[int(thres_pred_cls[0][kk])] + '\t' + str(accuracy[int(thres_pred_cls[0][kk])]))
#         analysis_result_file.write('\n')



# import matplotlib.pyplot as plt # plt 用于显示图片
# import matplotlib.image as mpimg # mpimg 用于读取图片
#
# wrong_pic = r"I:\Image_20170227_zhaomeng_n64\validation_analysis\img.txt"
# imdir = r"I:\Image_20170227_zhaomeng_n64\validation_analysis\badcase\n03815615_领带"
# count = 1
# for line in open(wrong_pic,'r'):
#     line = line.strip()
#     if line != '':
#         pic_dir = imdir + '\\' + line
#         pic = mpimg.imread(pic_dir)
#         plt.imshow(pic) # 显示图片
#         plt.axis('off') # 不显示坐标轴
#         plt.title(str(count))
#         count += 1
#         plt.pause(20)
#         plt.close()


#  ####get image
# x = 1
# page = 0
# socket.setdefaulttimeout(5.0)
# while (page<=1000):
#     fileurl= open(r"I:\Image_20170227_zhaomeng_n64\review_train_img_0503\addWebImg\fileurl.txt",'w')
#     url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E7%A2%91%E6%96%87&pn=" + str(page) + "&gsm=0"
#     imgcontent = urllib.urlopen(url).read()
#     fileurl.write(imgcontent)
#     # urllist = re.findall(r'src="(http.+?\.jpg)"', imgcontent, re.I)
#     urllist = re.findall(r'"objURL":"(http.+?\.JPG)"', imgcontent, re.I)
#     # urllist = re.findall(r'href="(http.+?\.jpg)"', imgcontent, re.I)
#
#     if not urllist:
#         print ('not found...')
#     else:
#         filepath = r'I:\Image_20170227_zhaomeng_n64\review_train_img_0503\addWebImg\n02892201_4'
#         if os.path.exists(filepath) is False:
#             os.mkdir(filepath)
#         for imgurl in urllist:
#             # print imgurl
#             temp = filepath + '\%s.jpg' % x
#             print  (x)
#             try:
#                 urllib.urlretrieve(imgurl, temp)
#                 x += 1
#             except IOError as e:  # 如果找不到，好像会引发IOError。
#                 print("download ", imgurl, "/nerror:", e)
#             print("Done:%s Copy to:%s" % (imgurl, temp))
#
#     page+=60


# imdir = r"I:\pic\n064_6"
# tag = 'neg_add_zm_'
# date = '20170801_'
# count = 929
#
# for ims in glob.glob(imdir + '\\' + '*.jpg'):
#     src = imdir + '\\' + ims.split('\\')[-1]
#     ori_name = src.split('\\')[-1]
#     ori_name = ori_name.split('.')[0]
#     # dst = imdir + '\\' + tag + date + ori_name + '.JPEG'
#     dst = imdir + '\\' + tag + date + str(count) + '.JPEG'
#     if not os.path.exists(dst):
#         os.rename(src,dst)
#     else:
#         count +=1
#         # dst = imdir + '\\' + tag + date + ori_name + '.JPEG'
#         dst = imdir + '\\' + tag + date + str(count) + '.JPEG'
#         while (os.path.exists(dst)):
#             count += 1
#             # dst = imdir + '\\' + tag + date + ori_name + '.JPEG'
#             dst = imdir + '\\' + tag + date + str(count) + '.JPEG'
#         os.rename(src, dst)
#     count += 1


####test code of wwm##########
import numpy as np

classes = 896
PR_file = open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\PRfile.txt','w')

# read synset
synset_2_label = {}
label_2_synset = {}
for line in open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\synset.txt_0811','r'):
    line = line.strip().split(' ')
    label = int(line[0])
    synset = line[1]
    synset_2_label[synset] = label
label_2_synset = dict(zip(synset_2_label.values(), synset_2_label.keys()))

# read tags
submodeltags = []
for line in open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\submodellist.txt','r'):
    line = line.strip()
    synset = line
    submodeltags.append(synset)

# read tagid
tagid_dict = {}
tagid_2_label = {}
# label_2_tagid = {}
for line in open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\tagid.txt','r',encoding='utf-8'):
    line = line.strip().split(',')
    tagid = line[0]
    synset = line[1]
    tagid_dict[synset] = tagid
    if synset in synset_2_label.keys():
        tagid_2_label[int(tagid)] = synset_2_label[synset]
# label_2_tagid = dict(zip(tagid_2_label.values(), tagid_2_label.keys()))

# read hierarchy
hirarchy_dict = {}
line_num = 0
for line in open(r"I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\tags_hierarchy.csv",'r',encoding='utf-8'):
    line_num += 1
    if (line_num != 1):
        flag_child = False
        flag_father = False
        line = line.strip().split(',')
        tagid_child = int(line[0])
        tagid_father = int(line[-3])
        if tagid_child in tagid_2_label.keys():
            label_child = tagid_2_label[tagid_child]
            flag_child = True
        if tagid_father in tagid_2_label.keys():
            label_father = tagid_2_label[tagid_father]
            flag_father = True
        if flag_child and flag_father:
            hirarchy_dict[label_child] = label_father

# read groundtruth
imlist = []
gt_info = {}
index_info = {}
for line in open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\imListTest_0728.txt','r',encoding='utf-8'):
    line = line.strip().split('\t')
    gt_cls = []
    for cls in line[2:]:
        cls = int(cls)
        if cls not in gt_info.keys():
            gt_info[cls] = []
            index_info[cls] = []
        gt_info[cls].append(line[1])
        index_info[cls].append(int(line[0]))
    imlist.append(line[1])

# read threshold
thres_dict = {}
for line in open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\threshold.txt_0811','r'):
    line = line.strip().split('\t')
    tagid = int(line[0])
    thres = float(line[1])
    label = tagid_2_label[tagid]
    thres_dict[label]=thres
threshold = []
for index in range(len(thres_dict)):
    threshold.append(thres_dict[index])
threshold_score = np.reshape(np.array(threshold),(1,len(thres_dict)))
threshold_mat = np.dot(np.ones((len(imlist),1)),threshold_score)


# read score
# score = np.loadtxt(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\log_total_test_wwm.txt')
score = np.loadtxt(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\log_total_wwm_0811.txt')
# score = np.loadtxt(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\VM_score_0728\result.txt')
# score = np.loadtxt(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\online_score_0728\testscore.txt')
# score = np.loadtxt(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\online_score_0728\onlinetestresult.txt')


# tag_score = open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\online_score_0728\score_134_online.txt','w')
# # tag_score = open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\online_score_0728\score_134_testscore.txt','w')
#
# subscore = score[:,134]
# for element in subscore.flat:
#     tag_score.write(str(element) + '\n')




score_sub = {}
for synset in submodeltags:
    label = synset_2_label[synset]
    score_sub[label] = np.loadtxt(r"I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\log_total_" + synset + '.txt')

# result (original predict)
result = score - threshold_mat
result[result >= 0] = 1
result[result < 0] = 0

# result (add submodel)
for synset in submodeltags:
    label = synset_2_label[synset]
    pred_array_father = result[:,label]

    pred_array_child = score_sub[label][:,1]
    pred_array_child[pred_array_child > 0.5] = 1
    pred_array_child[pred_array_child <= 0.5] = 0

    p_array = pred_array_father*pred_array_child
    result[:,label] = p_array


# result (add hierarchy)
for cls in hirarchy_dict.keys():
    pred_array = result[:,cls]
    pred_index = np.where(pred_array == 1)
    p_array = pred_index[0]
    result[p_array,hirarchy_dict[cls]] = 1

# gt_file = open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\view_gt\gt_n02121620_vm.txt','w')
# # pred_file = open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\view_p\p_n02121620.txt','w')
# pred_score_file = open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\view_p\p_s_n02121620_vm.txt','w')

# get presion and recall
for cls in range(classes):
    presion = 0
    recall = 0
    num_tp = 0
    num_p = 0
    num_gt = 0
    pred_array = result[:,cls]
    pred_index = np.where(pred_array == 1)
    p_array = pred_index[0]
    if cls in index_info.keys():
        gt_array = index_info[cls]
        tp = np.intersect1d(gt_array, p_array)
        num_p = len(p_array)
        num_tp = len(tp)
        num_gt = len(gt_array)
        if num_p > 0:
            presion = num_tp/num_p
        if num_gt > 0:
            recall = num_tp/num_gt
    print ('cls {:d}    presion={:f}   recall={:f}'.format(cls, presion, recall))
    # PR_file.write(str(cls) + '\t'  + label_2_synset[cls] + '\t' + str("%0.2f"%presion) + '\t' + str("%0.2f"%recall) + '\n')
    PR_file.write(str(cls) + '\t'  + label_2_synset[cls] + '\t' + str("%d/%d=%0.2f"%(num_tp,num_p,presion)) + '\t' + str("%d/%d=%0.2f"%(num_tp,num_gt,recall)) + '\n')

    # if cls == 134:
    #     # for index_ in p_array:
    #     #     pred_file.write(str(index_)  + '\n')
    #     for index_ in gt_array:
    #         gt_file.write(str(index_) + '\n')
    #     for index_ in p_array:
    #          if index_ in gt_array:
    #              pred_score_file.write(str(index_)  + '\t' + str(score[index_,134]) + '\t' + '1' + '\n')
    #          else:
    #              pred_score_file.write(str(index_)  + '\t' + str(score[index_,134]) + '\t' + '0' + '\n')




# ##2017-08-16
# import numpy as np
# # read score
# # score = np.loadtxt(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\log_total_test_wwm.txt')
# score = np.loadtxt(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\online_score_0728\onlinetestresult.txt')
#
# tag_score = open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\online_score_0728\onlinescore_134.txt','w')
# subscore = score[:,134]
# for element in subscore.flat:
#     tag_score.write(str(element) + '\n')
#
# threshold = 0.08458
