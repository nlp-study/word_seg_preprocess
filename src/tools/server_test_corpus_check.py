'''
Created on 2016年8月5日

@author: Zhang Xiulong
'''
from tools.list_operation import *
from tools.text_process import *

def _check_corpus_repeat_content(input_path):
    content_topic_map = {}
    corpus_list = read_list(input_path)
    for line in corpus_list:
        line_list = split_line_2_list_with_token(line,"\t",2,'server test corpus split')
        content = line_list[1]
        topic_name = line_list[0]
        if content in content_topic_map:
            pref_topic_name = content_topic_map[content]
            if topic_name != pref_topic_name:
                print(topic_name, pref_topic_name,content)
        else:
            content_topic_map[content] = topic_name
    print('repeat check ok!')

def _check_old_new_corpus(input_corpus_new,input_cropus_old,output_corpus_path):
    corpus_list_new = read_list(input_corpus_new)
    corpus_list_old = read_list(input_cropus_old)
    
    different_corpus_set = set(corpus_list_new) - set(corpus_list_old)
    different_corpus_list = list(different_corpus_set)
    different_corpus_list.sort()
    write_list(different_corpus_list, output_corpus_path)
    print('old new corpus check ok!')
    
    

if __name__ == '__main__':
    input_path = '../../data/total/additive_server_corpus.txt'
    output_path = '../../result_data/server_test_log/different_corpus_check.txt'
    new_corpus_path = '../../result_data/server_test_log/new_error_case.txt'
    _check_corpus_repeat_content(input_path)
    _check_old_new_corpus(new_corpus_path,input_path,output_path)
    
    
    