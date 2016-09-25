# !/usr/bin/python
# @Author - Nrupatunga

import os
    
def list_images(dirpath):
    ''' list all the image files in the directory 
        @params:
        --------
            - dirpath(string)          :: required : path to the directory/sub-dirs with exts
        @return:
        --------
            - returns list of image files 
    '''
    return list_files(dirpath, exts=['.jpg', '.jpeg', '.png', '.bmp'])

def list_files(path, exts=['.txt']):
    ''' list all the files in the directory 
        @params:
        --------
            - path(string)          :: required : path to the directory/sub-dirs with exts
            - exts(list of strings) :: optional : extensions of files to be listed, default-'.txt'
        @return:
        --------
            - returns list of files 
    '''
    assert(os.path.exists(path))
    path.rstrip('/')
    for f in os.listdir(path):
        if ''.join(['.', f.split('.')[-1].lower()]) in exts: 
            yield os.path.join(path, f)

if __name__ == '__main__':
    imgList = list_images('/home/nrupatunga/Pictures/')
    for img in imgList:
        print(img)
