##im2txt detection precision/recall##

def loadFile(file_name,label_name,convert = False):
    #load labels
    labels = {}
    for num, line in enumerate(open(label_name, 'r')):
        line = line.strip().split(' ')
        if len(line) > 2:
            labels[line[0] + ' ' + line[1]] = num
        else:
            labels[line[0]] = num
    #load files
    img_info = {}
    for line in open(file_name, 'r'):
        line = line.strip().split('\t')
        img_info[line[0]] = []
        for word in range(len(line) - 1):
            if convert:
                img_info[line[0]].append(labels[line[word + 1]])
            else:
                img_info[line[0]].append(line[word + 1])

    return img_info

def imgUnion(result_dict,gt_dict):

    return list(set(gt_dict.keys()) & set(result_dict.keys()))


def getPRArray(gt_info,result_info,img_union):

    ##get gt_mat and result_mat
    gt_mat = np.zeros((len(img_union), nclassess), dtype=bool)
    result_mat = np.zeros((len(img_union), nclassess), dtype=bool)
    count = 0
    for img in img_union:
        cls_gt_list = gt_info[img]
        cls_result_list = result_info[img]
        for cls in cls_gt_list:
            gt_mat[count, int(cls)] = True
        for cls in cls_result_list:
            result_mat[count, int(cls)] = True
        count += 1

    tp_mat = gt_mat * result_mat

    tp_cls = np.sum(tp_mat, axis=0)[2:]
    tp_fp_cls = np.sum(result_mat, axis=0)[2:]
    tp_fn_cls = np.sum(gt_mat, axis=0)[2:]

    pre_cls = tp_cls.astype(np.float32) / tp_fp_cls.astype(np.float32)
    rec_cls = tp_cls.astype(np.float32) / tp_fn_cls.astype(np.float32)

    return pre_cls,rec_cls


def avgPR(result_file,gt_file,label_file,clsinfo = True):

    ##load file
    img_gt = loadFile(gt_file,label_file,convert=True)
    img_result = loadFile(result_file,label_file)

    ##get image union
    img_union = imgUnion(img_result,img_gt)

    ##get pre,rec info for all cls
    [pre_cls,rec_cls] = getPRArray(img_gt,img_result,img_union)
    if clsinfo:
        for cls in range(nclassess - 2):
            print "cls " + str(cls + 1) + ': precision ' + str(pre_cls[cls]) + ' recall ' + str(rec_cls[cls])

    pre_avg = np.sum(pre_cls[2:])/(nclassess-2)
    rec_avg = np.sum(rec_cls[2:])/(nclassess-2)

    return pre_avg,rec_avg

if __name__ == '__main__':
    result = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/im2txt/detection_PR/output.log'
    val_list = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/im2txt/detection_PR/val_list.txt'
    words_label = '/mnt/hgfs/I/Image_20170227_zhaomeng_n64/im2txt/detection_PR/word_counts.txt'

    nclassess = 82
    [pre_avg,rec_avg] = avgPR(result,val_list,words_label,clsinfo = False)

    print "pre_avg = " + str(pre_avg)
    print "rec_avg = " + str(rec_avg)