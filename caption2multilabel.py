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
#     plt.pause(5)
#     plt.close()


###映射至894类###########
# #######20170418#############
#
tag_894 = r"I:\Image_20170227_zhaomeng_n64\caption2synset\synset_894.txt"
img_info = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\img_info_500.txt"
file_zh = r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\tag_zh_894.txt"
img_info_894 = open(r"I:\Image_20170227_zhaomeng_n64\caption2synset\change_translation\img_info_500_894.txt",'w')

tag_zh = {}
for line in open(file_zh,'r'):
    if line != '':
        line = line.strip().split('\t')
        tag_zh[line[0]] = line[1]

tag_894_list = []
for line in open(tag_894,'r'):
    line = line.strip()
    tag_894_list.append(line)

for line in open(img_info,'r'):
    line = line.strip().split('\t')
    synset_info = line[2].split(',')
    synset_info_new = []
    for synset in synset_info:
        if synset in tag_894_list:
            synset_info_new.append(synset)
    if len(synset_info_new) != 0 :
        img_info_894.write(line[0] + '\t')

        for kk in range(len(synset_info_new) - 1):
            img_info_894.write(synset_info_new[kk] + ',')
        img_info_894.write(synset_info_new[-1] + '\t')

        for kk in range(len(synset_info_new) - 1):
            img_info_894.write(tag_zh[synset_info_new[kk]] + '--')
        img_info_894.write(tag_zh[synset_info_new[-1]] + '\n')
    else:
        img_info_894.write(line[0] + '\n')