####test code of wwm##########
import numpy as np

classes = 899
PR_file = open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\PRfile.txt','w')

# read synset
synset_2_label = {}
label_2_synset = {}
for line in open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\synset.txt','r'):
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
# for line in islice(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\tagid.txt', 1, None):
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
for line in open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\imListTest.txt','r',encoding='utf-8'):
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
for line in open(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\threshold.txt','r'):
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
score = np.loadtxt(r'I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\log_total_test_wwm.txt')
score_sub = {}
for synset in submodeltags:
    label = synset_2_label[synset]
    score_sub[label] = np.loadtxt(r"I:\Image_20170227_zhaomeng_n64\submodel\test_wwm\\log_total_" + synset + '.txt')

# result (original predict)
result = score - threshold_mat
result[result >= 0] = 1
result[result < 0] = 0

# result (add hierarchy)
for cls in hirarchy_dict.keys():
    pred_array = result[:,cls]
    pred_index = np.where(pred_array == 1)
    p_array = pred_index[0]
    result[p_array,hirarchy_dict[cls]] = 1

# result (add submodel)
for synset in submodeltags:
    label = synset_2_label[synset]
    pred_array_father = result[:,label]

    pred_array_child = score_sub[label][:,1]
    pred_array_child[pred_array_child > 0.5] = 1
    pred_array_child[pred_array_child <= 0.5] = 0

    p_array = pred_array_father*pred_array_child
    result[:,label] = p_array

# get presion and recall
for cls in range(classes):
    presion = 0
    recall = 0
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
            recall = num_tp/num_gt
    # print ('cls {:d}    presion={:f}   recall={:f}'.format(cls, presion, recall))
    PR_file.write(str(cls) + '\t'  + label_2_synset[cls] + '\t' + str("%.2f"%presion) + '\t' + str("%.2f"%recall) + '\n')
