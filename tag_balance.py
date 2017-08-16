####get balanced image list########
trainfile = r"C:\zhaomeng\image-balance\trainIm.balance.921.txt"
filecount = open(r"C:\zhaomeng\image-balance\trainIm.balance.921.count.txt",'w')
trainfile_new = open(r"C:\zhaomeng\image-balance\trainIm.balance.921.new.txt",'w')
tag_count = {}
for line in open(trainfile,'r'):
    line  = line.strip().split('\t')
    line = line[1]
    if line not in tag_count.keys():
        tag_count[line] = 1
    else:
        tag_count[line] += 1

for kk in tag_count.keys():
    filecount.write(kk + '\t' + str(3000 - tag_count[kk]) + '\n')

i= 1607192
for kk in tag_count.keys():
    if tag_count[kk] > 0:
        train_add = []
        add_total = 3000 - tag_count[kk]
        add_num = 0
        while(add_num < add_total):
            for line in open(trainfile, 'r'):
                line = line.strip().split('\t')
                if line[1] == kk:
                    train_add.append(line[-1])
                    trainfile_new.write(str(i) + '\t' + str(kk) + '\t' + line[-1] + '\n')
                    i += 1
                    add_num += 1
                    if add_num == add_total:
                        print (kk + '\t' + str(add_num))
                        break




#########count numbers of image########
trainIm = r"C:\zhaomeng\tag-workspace\tags.0117\trainIm.leaf.877.balance.txt"
trainIm_count = open(r"C:\zhaomeng\tag-workspace\tags.0117\trainIm.count.leaf.877.balance.txt",'w')


trainIm_count_dict = {}
for line in open(trainIm,'r'):
   line = line.strip().split('\t')
   if line[1] not in trainIm_count_dict.keys():
       trainIm_count_dict[line[1]] = 1
   else:
       trainIm_count_dict[line[1]] += 1

for label in trainIm_count_dict.keys():
   trainIm_count.write(label + '\t' + str(trainIm_count_dict[label]) + '\n')