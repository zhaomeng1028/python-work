log_top5 = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\log_top5_relation.txt"
tags = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\tags.merge.960.txt"
tagid = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\tagid_ch.txt"
log_info = open(r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\log_info.txt",'w')

tagid_dict = {}
for line in open(tagid,'r'):
    if line != '\t\n':
        line = line.strip().split('\t')
        tagid_dict[line[0]] = line[1]

tags_dict = {}
for line in open(tags,'r'):
    line = line.strip().split(' ')
    tags_dict[line[0]] = line[1]

for line in open(log_top5,'r'):
    line = line.strip().split('\t')
    for kk in range(len(line)):
        log_info.write(line[kk] + '\t')
        if kk%2 != 0 :
            log_info.write(tagid_dict[tags_dict[line[kk]]] + '\t')
        elif kk ==len(line)-1 :
            log_info.write(tagid_dict[tags_dict[line[kk]]] + '\n')


