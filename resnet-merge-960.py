# ##########part.1:convert log format##################
file_path = r'C:\Users\zhaom\Desktop\tag-workspace\accu.960\log.txt'
file_temp_path = r'C:\Users\zhaom\Desktop\tag-workspace\accu.960\log_top5.txt'
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


# ###part.2:top5-accuracy###################
# file_path = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\log_top5.txt"
# top5_tag_path = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\temp_top5.txt"
#
# top5_tag_file = open(top5_tag_path,'w')
# for line in open(file_path,'r'):
#     line = line.strip().split('\t')
#     line = line[-1]
#     top5_tag_file.write(line + '\n')

# ###part.2:top1-accuracy###################
# file_accu_all = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\log_top5.txt"
# file_top1 = open(r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\temp_top1.txt",'w')
#
# for line in open(file_accu_all,'r'):
#     line = line.strip().split('\t')
#     if line[1] == line[-1]:
#         file_top1.write(line[1] + '\n')



# # ############part.3:get top-1#############
# file_path = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\temp_top1.txt"
# top5_accu_file = open(r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\top1_accu_all.txt",'w')
# tagleaf_path = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\tags.merge.960.txt"
# tagid_path = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\tagid.txt"
# val_label = {}
# tagleaf = {}
# tagid = {}
# for line in open(tagid_path,'r'):
#     line = line.strip().split(',')
#     info = []
#     info1 = ""
#     for i in range(len(line) -3):
#         info.append(line[i+2])
#         info1 = info1 + line[i+2] + ','
#     info1 += line[-1]
#     tagid[line[1]] = info1
#
# for line in open(tagleaf_path,'r'):
#     line = line.strip().split(' ')
#     tagleaf[line[0]] = line[1]
#
# for k in range(953):
#     val_label[str(k)] = 0
#
# for line in  open(file_path,'r'):
#     line = line.strip().split('\t')
#     line = line[0]
#     val_label[line] += 1
#
# for tag in val_label.keys():
#     # print float(val_label[tag]/50.0)
#     accu = float(val_label[tag]/50.0)
#     if accu < 100:
#         print tag
#         top5_accu_file.write(tag + '\t' + tagleaf[tag] + '\t' + str(val_label[tag]/50.0)  + '\t' + tagid[tagleaf[tag]] + '\t'  + '\n')


# # ############part.3:get top-5#############
# file_path = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\temp_top5.txt"
# top5_accu_file = open(r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\top5_accu_all.txt",'w')
# tagleaf_path = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\tags.merge.960.txt"
# tagid_path = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\tagid.txt"
# val_label = {}
# tagleaf = {}
# tagid = {}
# for line in open(tagid_path,'r'):
#     line = line.strip().split(',')
#     info = []
#     info1 = ""
#     for i in range(len(line) -3):
#         info.append(line[i+2])
#         info1 = info1 + line[i+2] + ','
#     info1 += line[-1]
#     tagid[line[1]] = info1
#
# for line in open(tagleaf_path,'r'):
#     line = line.strip().split(' ')
#     tagleaf[line[0]] = line[1]
#
# for k in range(953):
#     val_label[str(k)] = 0
#
# for line in  open(file_path,'r'):
#     line = line.strip().split('\t')
#     line = line[0]
#     val_label[line] += 1
#
# for tag in val_label.keys():
#     # print float(val_label[tag]/50.0)
#     accu = float(val_label[tag]/50.0)
#     if accu < 100:
#         print tag
#         top5_accu_file.write(tag + '\t' + tagleaf[tag] + '\t' + str(val_label[tag]/50.0)  + '\t' + tagid[tagleaf[tag]] + '\t'  + '\n')
