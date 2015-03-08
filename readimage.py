__author__ = 'origin'

from PIL import Image
import os.path
import glob
import numpy

def getKey( x ):
    return float(x[0])
#def convertjpg(jpgfile,outdir,width=1280,height=720):
#    img=Image.open(jpgfile)
#    print jpgfile
#    #new_img=img.resize((width,height),Image.BILINEAR)
#    #new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
##for jpgfile in glob.glob("C:\Users\origin\Desktop\mysite\media\photo\*.jpg"):
##    convertjpg(jpgfile,"C:\Users\origin\Desktop\mysite\media\save")
#
jp = "./media/photo\\im0001.jpg"
im = os.path.basename(jp)
target_im = im[2:6]
print int(target_im)
#
#print jp.replace('\\','/')
jpgfile = glob.glob("C:\Users\origin\Desktop\mysite\media\photo\*.jpg")
#print jpgfile


fi = open('feature30.txt')
line = fi.readline()
###### read the picture feature ##########
groundTruth = numpy.zeros((30,4096))
j = 0
while line:
    line = line.strip()
    li = line.split('  ')
    groundTruth[j] = li
    for i in range(0,4096):
        groundTruth[j,i] =float(li[i])
#np = numpy.array(list)
    j += 1
    line = fi.readline()
    if j == 30:break

target = groundTruth[0]

g = []

for i in range(0,30):
    s = []
    #s.append(sum(abs(target - groundTruth[i])))
    od = abs(target - groundTruth[i])
    s.append(numpy.dot(od,od))
    s.append(jpgfile[i])
    g.append(s)

for i in range(0,30):
    print g[i]

g.sort(key=getKey)

print " "
for i in range(0,30):
    print g[i]
#s.sort()
#print s

fi.close()