'''
Created on 2016年6月21日

@author: Zhang Xiulong
'''
import shutil 
import os

def copy_file(source_file,target_file):
    if not os.path.exists(source_file):
        print('copy file failure,source file is not exist!')
    shutil.copy(source_file,  target_file)
    
def dirlist(path, allfile):  
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:  
            allfile.append(filepath)  
    return allfile  
     
if __name__ == '__main__':
    source_file = 'd:/test.txt'
    target_file = 'd:/test_1.txt'
    copy_file(source_file,target_file)