top5_file = r"C:\zhaomeng\tag-workspace\accu.balance.921\log_top5.txt"
max_info_file = r"C:\zhaomeng\tag-workspace\accu.balance.921\max_info.txt"
top5_info_file = open(r"C:\zhaomeng\tag-workspace\accu.balance.921\top5_info.txt",'w')
max_info = {}
for line in open(max_info_file,'r'):
    tag_pair = []
    line = line.strip().split('\t')
    tag_pair.append(line[0])
    tag_pair.append(line[1])
    max_info[tag_pair] = line[2]

i = 0
for line in open(top5_file,'r'):
    line = line.strip().split('\t')
    tag_pair = []
    tag_pair.append(line[1])
    tag_pair.append(line[-1])
    top5_info_file.write()