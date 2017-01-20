'''
Created on 2016年7月5日

@author: Zhang Xiulong
'''
from tools.list_operation import *
from tools.text_process import *

def _list_compare(list_1,list_2):
    different_unit = set(list_1) ^ set(list_2)
    print('****different_unit size:',len(different_unit))
    print('\n'.join(different_unit))
    more_unit = set(list_1) - set(list_2)
    print('****more_unit size:',len(more_unit))
    print('\n'.join(more_unit))  
    omit_unit = set(list_2) - set(list_1)
    print('****omit_unit size:',len(omit_unit))
    print('\n'.join(omit_unit))  
    
    different_unit_list = list(different_unit)
    more_unit_list = list(more_unit)
    omit_unit_list = list(omit_unit)
    different_unit_list.sort()
    more_unit_list.sort()
    omit_unit_list.sort()
    
    return different_unit_list,more_unit_list,omit_unit_list

def list_compare(input_list_1,input_list_2,different_str_path,omit_str_path,more_str_path):
    list_1 = read_list(input_list_1)
    list_2 = read_list(input_list_2)
    different_unit_list,more_unit_list,omit_unit_list = _list_compare(list_1,list_2)
    write_list(different_unit_list,different_str_path)
    write_list(more_unit_list,more_str_path)
    write_list(omit_unit_list,omit_str_path)
    
    
    
def error_corpus_compare(error_id_1,corpus_1,error_id_2,corpus_2,different_str_path,omit_str_path,more_str_path):
    error_id_1_list = read_list(error_id_1)
    error_id_2_list = read_list(error_id_2)
    corpus_l_list = read_list(corpus_1)
    corpus_2_list = read_list(corpus_2)
    
    compare_1_list = []
    compare_2_list = []
    
    for error_id in error_id_1_list:
        error_id = int(error_id)
        line = corpus_l_list[error_id]
        topic_name,corpus_line,md5 = split_line_2_list_with_token(line,'\t',3,'error_1')
        md5 = md5.strip()
        compare_1_list.append(md5)
        
    for error_id in error_id_2_list:
        error_id = int(error_id)
        line = corpus_2_list[error_id]
        topic_name,corpus_line,md5 = split_line_2_list_with_token(line,'\t',3,'error_1')
        md5 = md5.strip()
        compare_2_list.append(md5)
        
    
    different_unit = set(compare_1_list) ^ set(compare_2_list)
    print('****different_unit size:',len(different_unit))
#     print('\n'.join(different_unit))
    more_unit = set(compare_1_list) - set(compare_2_list)
    print('****more_unit size:',len(more_unit))
#     print('\n'.join(more_unit))  
    omit_unit = set(compare_2_list) - set(compare_1_list)
    print('****omit_unit size:',len(omit_unit))
#     print('\n'.join(omit_unit))  
    
    different_unit_list = list(different_unit)
    more_unit_list = list(more_unit)
    omit_unit_list = list(omit_unit)
    different_unit_list.sort()
    more_unit_list.sort()
    omit_unit_list.sort()
    write_list(different_unit_list,different_str_path)
    write_list(more_unit_list,more_str_path)
    write_list(omit_unit_list,omit_str_path)

def _compare_corpus_list(corpus_path_1,corpus_path_2,omit_str_path,more_str_path):
    md5_corpus_map = {}
    md5_list_1 = []
    md5_list_2 = []
    corpus_list_1 = read_list(corpus_path_1)
    corpus_list_2 = read_list(corpus_path_2)
    for line in corpus_list_1:
        topic_name,content,md5 = split_line_2_list_with_token(line,'\t',3,"split corpus 1 ")
        md5 = md5.strip()
        if md5 in md5_list_1:
            print('>>>>>Error:md5 repeated<<<<<')
            print('line:',line)
#             print('>>>>>exit<<<<<')
#             exit()
        md5_corpus_map[md5] = line
        md5_list_1.append(md5)
        
    for line in corpus_list_2:
        topic_name,content,md5 = split_line_2_list_with_token(line,'\t',3,"split corpus 1 ")
        md5 = md5.strip()
        if md5 in md5_list_2:
            print('>>>>>Error:md5 repeated<<<<<')
            print('line:',line)
#             print('>>>>>exit<<<<<')
#             exit()
        md5_corpus_map[md5] = line
        md5_list_2.append(md5)

    different_unit_list,more_unit_list,omit_unit_list = _list_compare(md5_list_1,md5_list_2)
    more_corpus_list = []
    omit_corpus_list = []
    
    for md5 in more_unit_list:
        line = md5_corpus_map[md5]
        more_corpus_list.append(line)
     
    for md5 in omit_unit_list:
        line = md5_corpus_map[md5]
        omit_corpus_list.append(line)
         
    write_list(more_corpus_list,more_str_path)
    write_list(omit_corpus_list,omit_str_path)
    
    

def simple_compare():
    input_list_1 = '../../result_data/change_data_structure/db_with_answer_topic_name.txt'
    input_list_2 = '../../data/total/svm_topic_list.txt'
   
    
    different_str_path = '../../result_data/list_compare/different_str.txt'
    omit_str_path = '../../result_data/list_compare/omit_str.txt'
    more_str_path = '../../result_data/list_compare/more_str.txt'
    list_compare(input_list_1,input_list_2,different_str_path,omit_str_path,more_str_path)
    
    
def complex_compare():
    #     input_list_1 = '../../result_data/list_compare/1.txt'
#     input_list_2 = '../../result_data/list_compare/2.txt'
    error_id_1 = '../../result_data/libsvm/error_id.txt'
    error_id_2 = '../../result_data/result_analysis/error_id.txt'
    
    corpus_1 = '../../data/libsvm/train_corpus.txt'
    corpus_2 = '../../data/result_analysis/classification_corpus.txt'
    
    different_str_path = '../../result_data/list_compare/different_str.txt'
    omit_str_path = '../../result_data/list_compare/omit_str.txt'
    more_str_path = '../../result_data/list_compare/more_str.txt'
#     list_compare(input_list_1,input_list_2,different_str_path,omit_str_path,more_str_path)
    error_corpus_compare(error_id_1,corpus_1,error_id_2,corpus_2,different_str_path,omit_str_path,more_str_path)
    

def compare_corpus_list():
    corpus_path_1 = '../../result_data/list_compare/classification_corpus_1.txt'
    corpus_path_2 = '../../result_data/list_compare/classification_corpus_2.txt'
    omit_str_path = '../../result_data/list_compare/omit_str.txt'
    more_str_path = '../../result_data/list_compare/more_str.txt'
    _compare_corpus_list(corpus_path_1,corpus_path_2,omit_str_path,more_str_path)
    
    
if __name__ == '__main__':
    simple_compare()
    
    