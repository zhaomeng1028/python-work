####test-map############
import numpy as np
import os

nclasses = 921
def mapcal(score_file, gt_file, vis=True):
    all_scores = np.loadtxt(score_file)
    gt_list = np.loadtxt(gt_file, usecols=(1,), dtype=int)
    ap_array = np.zeros((nclasses, 1), dtype=np.float32)
    for cls in range(0, nclasses):
        ap = apcal(gt_list, cls, all_scores[:, cls])
        ap_array[cls] = ap
        if vis:
            print ('cls {:d}   ap={:f}'.format(cls, ap))
    map = ap_array.mean()
    if vis:
        print ('map = {:f}'.format(map))
    return map


def apcal(gt_list, cls, scores):
    gt = np.zeros((len(gt_list), 1), dtype=int)
    gt[gt_list == cls] = 1
    si = scores.argsort()[::-1]
    tp = (gt[si] > 0).astype('Float32')
    fp = (gt[si] <= 0).astype('Float32')

    fp = np.cumsum(fp)
    tp = np.cumsum(tp)
    rec = tp / np.sum(gt > 0)
    prec = tp / (fp + tp)

    ap = 0
    for t in range(0, 11, 1):
        tt = t * 0.1
        p_ind = prec[rec >= tt]
        if len(p_ind) > 0:
            p = np.max(p_ind)
        else:
            p = 0.0
        ap = ap + p / 11
    return ap

score_file = r'I:\ImageNet_new\log_total.txt'
gt_file = r"I:\ImageNet_new\valIm.balance.921.txt"
mapcal(score_file, gt_file, vis=True)