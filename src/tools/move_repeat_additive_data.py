'''
Created on 2016年8月23日

@author: Zhang Xiulong
'''
from tools.list_operation import *
from tools.text_process import *

def move_repeat_corpus(input_corpus_path,output_corpus_path):
    input_corpus_list = read_list(input_corpus_path)
    _check_conflict_corpus(input_corpus_list)
    _move_repeat_corpus(input_corpus_list,output_corpus_path)
    
def _check_conflict_corpus(input_corpus_list):
    content_topic_map = {}
    for line in input_corpus_list:
        split_list = split_line_2_list(line,"\t",2)
        topic_name = split_list[0]
        content = split_list[1]
        if content in content_topic_map : 
            temp_topic = content_topic_map[content]
            if temp_topic != topic_name:
                print('conflict in two lines:')
                print(line)
                print(temp_topic + '\t' + content)
                print('exit')
                exit()
        else:
            content_topic_map[content] = topic_name
            
def _move_repeat_corpus(input_corpus_list,output_corpus_path):
    content_topic_map = {}
    for line in input_corpus_list:
        split_list = split_line_2_list(line,"\t",2)
        topic_name = split_list[0]
        content = split_list[1]
        if content in content_topic_map : 
            print('repeat content:',content)
            continue
        else:
            content_topic_map[content] = topic_name
    
    with codecs.open(output_corpus_path, 'w', 'utf-8') as write_file:
        for content in content_topic_map:
            topic = content_topic_map[content]
            line = topic + '\t' + content
            write_file.write(line + '\r\n')
    
    
        
        
    
if __name__ == '__main__':
    input_corpus_path = '../../data/total/additive_server_corpus.txt'
    output_corpus_path = '../../data/total/additive_server_corpus_clean.txt'
    move_repeat_corpus(input_corpus_path,output_corpus_path)
    