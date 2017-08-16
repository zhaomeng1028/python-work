imlist = open(r"I:\Image_20170227_zhaomeng_n64\imlist_clean.zmeng.imgnet.20170213.txt",'w')
synsetlist = open(r"I:\Image_20170227_zhaomeng_n64\synset_subset.zmeng.imgnet.20170213.txt",'w')

imdir = r"I:\Image_20170227_zhaomeng_n64\image_selected_vendor_n64"

suffix = '_'

for file in glob.glob(imdir + '\\' + '*'):
    file = file.split('\\')[-1]
    if not file.endswith(suffix):
        synsetlist.write(file + '\n')
        for ims in glob.glob(imdir + '\\' + file + '\\' + '*.JPEG'):
            im = ims.split('\\')[-1]
            im = im.split('_')
            if len(im)>2 and im[1].startswith('n'):
                im_write = ims
            imlist.write(file + '/' + ims.split('\\')[-1] + '\n')