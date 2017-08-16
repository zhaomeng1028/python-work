import urllib
import socket

# #####get image
# x = 1
# page = 0
# socket.setdefaulttimeout(5.0)
# while (page<=1000):
#     fileurl= open(r"C:\Users\zhaom\Desktop\url\fileurl.txt",'w')
#     url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E4%BC%9A%E8%AE%AE%20%E6%8A%95%E5%BD%B1&pn=" + str(page) + "&gsm=0"
#     imgcontent = urllib.urlopen(url).read()
#     fileurl.write(imgcontent)
#     # urllist = re.findall(r'src="(http.+?\.jpg)"', imgcontent, re.I)
#     urllist = re.findall(r'"objURL":"(http.+?\.JPG)"', imgcontent, re.I)
#     # urllist = re.findall(r'href="(http.+?\.jpg)"', imgcontent, re.I)
#
#     if not urllist:
#         print 'not found...'
#     else:
#         filepath = r'C:\Users\zhaom\Desktop\img\ppt2'
#         if os.path.exists(filepath) is False:
#             os.mkdir(filepath)
#         for imgurl in urllist:
#             # print imgurl
#             temp = filepath + '\%s.jpg' % x
#             print  x
#             try:
#                 urllib.urlretrieve(imgurl, temp)
#                 x += 1
#             except IOError as e:  # 如果找不到，好像会引发IOError。
#                 print("download ", imgurl, "/nerror:", e)
#             print("Done:%s Copy to:%s" % (imgurl, temp))
#
#     page+=60