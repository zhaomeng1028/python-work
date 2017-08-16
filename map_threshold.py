##threshold
import numpy as np
import os

nclasses=918

def mapcal(score_file, gt_file, result_file, vis=True, prt=True):
    gt_mat=loadGT(gt_file)
    all_scores = np.loadtxt(score_file)
    ap_array=np.zeros((nclasses,), dtype=np.float32)
    threshold_array=np.zeros((nclasses,), dtype=np.float32)
    prec_array=np.zeros((nclasses,), dtype=np.float32)
    rec_array=np.zeros((nclasses,), dtype=np.float32)
    for cls in range(0,nclasses):
        (ap_array[cls],threshold_array[cls],prec_array[cls],rec_array[cls])=apcal(gt_mat[:,cls], cls, all_scores[:,cls])
        if vis:
            print ('cls {:d}    ap={:f}'.format(cls,ap_array[cls]))
    map=ap_array.mean()
    if vis:
        print ('map = {:f}'.format(map))

    if prt:
        fid=open(result_file,'w')
#        fid.write('ap\tthresh\tprec\trec\n')
        for cls in range(nclasses):
            fid.write('%.3f\t%.3e\t%.3f\t%.3f\n'% (ap_array[cls],threshold_array[cls],prec_array[cls],rec_array[cls]))
        fid.close()
    return map

def loadGT(gt_file):
    with open(gt_file) as fid:
        lines=fid.readlines()
    gt_mat=np.zeros((len(lines),nclasses),dtype=bool)
    count=0
    for line in lines:
        cls_list=line.strip().split('\t')[2:]
        for cls in cls_list:
            gt_mat[count,int(cls)]=True
        count=count+1
    return gt_mat

def apcal(gt, cls, scores):
#    scores=np.loadtxt(score_file,usecols=(cls,))
    si=scores.argsort()[::-1]
    tp=(gt[si]>0).astype('Float32')
    fp=(gt[si]<=0).astype('Float32')

    fp=np.cumsum(fp)
    tp=np.cumsum(tp)
    rec=tp/np.sum(gt>0)
    prec=tp/(fp+tp)

    ap=0
    for t in range(0,11,1):
        tt=t*0.1
        p_ind=prec[rec>=tt]
        if len(p_ind)>0:
            p=np.max(p_ind)
        else:
            p=0.0
        ap=ap+p/11

    prec2rec2=np.multiply(1-prec,1-prec)+np.multiply(1-rec,1-rec)
    bestind=np.argmin(prec2rec2)
    scores.sort()
    threshold=scores[::-1][bestind]
    bestprec=prec[bestind]
    bestrec=rec[bestind]

    return (ap,threshold,bestprec,bestrec)

if __name__ == '__main__':
    mapcal(r'I:\Image_20170227_zhaomeng_n64\testThreshold\log_total.txt',r'I:\Image_20170227_zhaomeng_n64\testThreshold\imListVal_gt.txt',r'I:\Image_20170227_zhaomeng_n64\testThreshold\map_result.txt')
