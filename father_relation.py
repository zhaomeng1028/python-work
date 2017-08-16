#####get father.relaton&root.relation label of tags.960#######
father_relation_path = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\father_relation.txt"
tag_960_path = r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\tags.merge.960.txt"
father_relation_label = open(r"C:\Users\zhaom\Desktop\tag-workspace\accu.960\father.relation.label.960.txt",'w')
tags960 = {}
for line in open(tag_960_path,'r'):
    line = line.strip().split(' ')
    tags960[line[1]] = line[0]

for line in open(father_relation_path,'r'):
    line = line.strip().split('\t')
    father = line[0]
    if father in tags960.keys():
        father_relation_label.write(tags960[father] + '\t')
        father_relation_label.write(tags960[father] + '\t')
        for k in range(len(line)-1):
            tag = line[k+1]
            if tag in tags960.keys():
                father_relation_label.write(tags960[tag] + '\t')
        father_relation_label.write('\n')