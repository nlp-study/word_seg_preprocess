'''
Created on 2016年7月29日

@author: Zhang Xiulong
'''
import hashlib

def generate_md5_by_line(line,line_numb):
    src = line + str(line_numb)
    src = src.encode('utf_8')
    m2 = hashlib.md5()   
    m2.update(src)   
    return m2.hexdigest()

def generate_md5_by_pure_line(line):
    src = line.encode('utf_8')
    m2 = hashlib.md5()   
    m2.update(src)   
    return m2.hexdigest()

if __name__ == '__main__':
    pass