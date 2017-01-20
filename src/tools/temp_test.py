'''
Created on 2016年7月19日

@author: Zhang Xiulong
'''
from tools.list_operation import *

def temp_test(input_path):
    test_corpus = read_list(input_path)
    line_1 = test_corpus[0]
    line_2 = test_corpus[1]
    
    line_list_1 = line_1.split(',')
    line_list_2 = line_2.split(',')
    
    if len(line_list_1) != len(line_list_2):
        print('is not same size')
        
    for i in range(len(line_list_1)):
        term_1 = line_list_1[i]
        term_2 = line_list_2[i]
        if term_1 != term_2:
            print(term_1 ,"    ", term_2)
            
    
if __name__ == '__main__':
    input_path = '../../result_data/temp.txt'
    temp_test(input_path)