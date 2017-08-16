# synset_file = r"I:\ImageNet_new\synset.txt"
# badimg_list = open('I:\ImageNet_new\\badImg.txt','w')
# for line in open(synset_file,'r'):
#     line = line.strip()
#     imdir = r"I:\ImageNet_new" + '\\' + line
#     ims = glob.glob(imdir + '\\' + '*.JPEG')
#     for im in ims:
#         badimg_list.write(im.split('\\')[-1] + '\n')