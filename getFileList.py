import os

def getFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.add(os.path.basename(dir))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, fileList)
    return fileList


s = set([])
list = getFileList('.', s)
fo = open("filelist","wb")
for e in list:
    fo.write(e)
    fo.write("\n")
fo.close()
