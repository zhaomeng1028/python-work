imdir = r"C:\Users\zhaom\Desktop\lajixiang"
tag = 'n03256032_'
date = '20170309'
count = 1

for ims in glob.glob(imdir + '\\' + '*.JPEG'):
    src = imdir + '\\' + ims.split('\\')[-1]
    dst = imdir + '\\' + tag + date + str(count) + '.JPEG'
    if not os.path.exists(dst):
        os.rename(src,dst)
    else:
        count +=1
        dst = imdir + '\\' + tag + date + str(count) + '.JPEG'
        while (os.path.exists(dst)):
            count += 1
            dst = imdir + '\\' + tag + date + str(count) + '.JPEG'
        os.rename(src, dst)
    count += 1