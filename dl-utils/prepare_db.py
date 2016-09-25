# !/usr/bin/python
# @Author - Nrupatunga

from __future__ import division
from listpaths import list_images
import os
import random
import pudb

def shuffle(filepath):
    '''shuffle the contents of the file
        @params:
        --------
            - filepath(string) :: required :: path to the text file containing list of image filenames
        return:
        -------
            - new shuffled file with  name "filepath_shuffle.txt"
    '''
    with open(filepath, 'r') as f:
        data = [(random.random(), line) for line in f]

    data.sort()
    root       = '/'.join(filepath.split('/')[:-1])
    filename   = filepath.split('/')[-1]
    fname, ext = filename.split('.')
    fname_shuf = ''.join([fname, '_shuffle', '.', ext])
    path_shuf  = os.path.join(root, fname_shuf)
    with open(path_shuf, 'w') as f:
        for _, line in data:
            f.write(line)
    

def num_lines(filepath): 
    '''find the number of lines in the file
        @params:
        --------
            - filepath(string) :: required :: path to the text file containing list of image filenames
        return:
        -------
            - length of the file
    '''
    with open(filepath, 'r') as f:
        for i, l in enumerate(f):
            pass
        return i+1


def split_db(filepath, train = 80, test = 10, val = 10):
    ''' split data into train test and validation 
        NOTE: This API is written keeping caffe's ImageDataLayer in mind, please free to modify for your convenience 
        @params:
        --------
            - filepath(string) :: required :: path to the text file containing list of image filenames
            - train(int)       :: optional :: percentage of images in each directory to be in the train set
            - test(int)        :: optional :: percentage of images in each directory to be in the test set
            - val(int)         :: optional :: percentage of images in each directory to be in the validation set
        return:
        -------
            - None
        usage:
        ------
            -----------------snippet-----------------
            >>>split_db('your/path/to/textfile')
            >>>split_db('your/path/to/textfile', train=70, test = 10, val = 20)
            ---------------------------------------------------------------------------
    '''
    flength   = num_lines(filepath)
    train_num = (train*flength)//100
    test_num  = (test*flength)//100 
    val_num   = flength - train_num - test_num

    root        = '/'.join(filepath.split('/')[:-1])
    filename    = filepath.split('/')[-1]
    fname, ext  = filename.split('.')
    fname_train = ''.join([fname, '_train', '.', ext])
    fname_test  = ''.join([fname, '_test', '.', ext])
    fname_val   = ''.join([fname, '_val', '.', ext])

    path_train = os.path.join(root, fname_train)
    path_test  = os.path.join(root, fname_test)
    path_val   = os.path.join(root, fname_val)

    countLines = 0
    with open(filepath, 'r') as f, open(path_train, 'w') as ftrain, open(path_test, 'w') as ftest, open(path_val, 'w') as fval:
        for line in f: 
            if countLines <= train_num: 
                ftrain.write(line)
            elif countLines <= (train_num + test_num):
                ftest.write(line)
            else:
                fval.write(line)
            countLines = countLines + 1

    print('Split: Total={}, Train={}, Test={}, Val={}'.format(flength, train_num, test_num, val_num))
    print(path_train, path_test, path_val)

def prepare_db(dirpath, train = 80, test = 10, val = 10): 
    ''' prepare data, split data into train test and validation 
        NOTE: This API is written keeping caffe's ImageDataLayer in mind, please free to modify for your convenience 
        @params:
        --------
            - path(string) :: required :: path to the directory containing images/directory with sub-dirs containing images
            - train(int)   :: optional :: percentage of images in each directory to be in the train set
            - val(int)     :: optional :: percentage of images in each directory to be in the validation set
            - test(int)    :: optional ::  percentage of images in each directory to be in the test set
        return:
        -------
            - four new files are written in dirpath, 
                eg.: xyz.txt, xyz_train.txt, xyz_test.txt, xyz_val.txt
        usage:
        ------
            -----------------Snippet-1-----------------
            >>>prepare_db('your/path/to/dirs')
            >>>prepare_db('your/path/to/dirs', train=70, val = 10, test = 20)
            ---------------------------------------------------------------------------
    '''
    folder, files, label, count = [], [], 1, 0

    assert os.path.isdir(dirpath)
    print('Scanning Image files .. Please wait..')
    for root, dirs, _ in os.walk(dirpath):
        newfolder = root.rstrip('/').split('/')[-1]
        if newfolder not in folder:
            folder.append(newfolder)
            if count:
                label = label + 1
                count = 0

        newfile = ''.join([root.rstrip('/'), '/', folder[-1], '.txt'])
        with open(newfile, 'w') as f:
            for img in sorted(list_images(root), key=lambda k: random.random()):
                f.write(''.join([img, ' ', str(label), '\n']))
                count = count + 1
            if not count:
                os.remove(newfile)
            else:
                files.append(newfile)

    print('Done!')
    print('files written {}'.format(files))
    for f in files:
        split_db(f)
    
if __name__ == '__main__':
    # prepare_db('/home/nrupatunga/NThere/Caffe-WS/BlurDetection-CNN/data/')
    # shuffle('/home/nrupatunga/NThere/Caffe-WS/BlurDetection-CNN/data/data_split/train/train.txt')
    # shuffle('/home/nrupatunga/NThere/Caffe-WS/BlurDetection-CNN/data/data_split/train/train_shuffle.txt')
    # shuffle('/home/nrupatunga/NThere/Caffe-WS/BlurDetection-CNN/data/data_split/test/test_shuffle.txt')
    # shuffle('/home/nrupatunga/NThere/Caffe-WS/BlurDetection-CNN/data/data_split/val/val.txt')
    shuffle('/home/nrupatunga/NThere/Caffe-WS/BlurDetection-CNN/data/data_split/val/val_shuffle.txt')
