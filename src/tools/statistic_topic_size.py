'''
Created on 2016年7月5日

@author: Zhang Xiulong
'''
import os
from tools.list_operation import *

def calculate_topic_size(input_folder,statistic_result_path):
    all_corpus = []
    topic_size_map = {}
    files = os.listdir(input_folder)
    for sub_file in files:
        sub_path = input_folder + os.sep + sub_file
        temp_list = read_list(sub_path)
        all_corpus += temp_list
    
    for line in all_corpus:
        line = line.strip()
        line_list = line.split('\t')
        if len(line_list) != 3:
            print('>>>>>Error:line format is illegal!<<<<<')
            print('line:',line)
            print('>>>>>exit<<<<<')
            exit()
        topic_name  = line_list[0]
        if topic_name in  topic_size_map:
            topic_size_map[topic_name] += 1
        else:
            topic_size_map[topic_name] = 1
        
    write_sorted_str_int_map(topic_size_map,statistic_result_path)
        
        
    
if __name__ == '__main__':
    input_folder = '../../corpus/tag_data'
    statistic_result_path = '../../result_data/statistic_topic_size.txt'
    calculate_topic_size(input_folder,statistic_result_path)
    
    
    
    
    