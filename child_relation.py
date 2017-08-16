root_relation = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\root_relation.txt"
father_relation = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\father_relation.txt"

child_relation = open(r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\child_relation.txt",'w')

root_tags = []
child_relation_dict = {}
for line in open(root_relation,'r'):
    line = line.strip().split('\t')
    root_tags.append(line[0])
    for kk in range(len(line) - 1):
        child_relation_dict[line[kk+1]] = []
        child_relation_dict[line[kk + 1]].append(line[0])

for line in open(father_relation,'r'):
    line = line.strip().split('\t')
    if line[0] not in root_tags:
        for kk in range(len(line) - 1):
            child_relation_dict[line[kk+1]].append(line[0])

for tag in child_relation_dict.keys():
    child_relation.write(tag + '\t')
    for kk in range(len(child_relation_dict[tag])):
        child_relation.write(child_relation_dict[tag][kk] + '\t')
    child_relation.write('\n')