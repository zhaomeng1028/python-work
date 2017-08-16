##navigation-accuracy
tag_navigation = r"C:\Users\zhaom\Desktop\tag-workspace\accu.navigation\Navigation_tag.tsv"
top5_all = r"C:\Users\zhaom\Desktop\tag-workspace\accu.navigation\top5_accu.txt"
top1_all = r"C:\Users\zhaom\Desktop\tag-workspace\accu.navigation\top1_accu.txt"
top5_navi = open(r"C:\Users\zhaom\Desktop\tag-workspace\accu.navigation\top5_navi.txt",'w')
top1_navi = open(r"C:\Users\zhaom\Desktop\tag-workspace\accu.navigation\top1_navi.txt",'w')

tag_navi = []
for line in open(tag_navigation,'r'):
    line = line.strip().split('\t')
    tag_navi.append(line[1])

top5_dict = {}
for line in open(top5_all,'r'):
    line = line.strip().split('\t')
    top5_dict[line[1]] = line[2:]

top1_dict = {}
for line in open(top1_all,'r'):
    line = line.strip().split('\t')
    top1_dict[line[1]] = line[2:]

for kk in range(len(tag_navi)):
    if tag_navi[kk] in top5_dict.keys():
        top5_navi.write(tag_navi[kk] + '\t' + top5_dict[tag_navi[kk]][0] + '\t' + top5_dict[tag_navi[kk]][1] +'\n')
        top1_navi.write(tag_navi[kk] + '\t' + top1_dict[tag_navi[kk]][0] + '\t' + top1_dict[tag_navi[kk]][1] + '\n')
    else:
        print tag_navi[kk]