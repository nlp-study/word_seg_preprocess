'''
Created on 2016年6月21日

@author: Zhang Xiulong
'''
from tools.list_operation import *

list_path = '../../data/team_tag_process/tag_answer.txt'
temp_list = read_list(list_path)
print('size of list:',len(temp_list))
temp_list = set(temp_list)
print('size of list:',len(temp_list))

