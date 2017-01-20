'''
Created on 2016年7月14日

@author: Zhang Xiulong
'''
from tools.list_operation import *

def build_standard_check_corpus(topic_list_path,raw_corpus_path,output_path):
    topic_list = read_list(topic_list_path)
    raw_corpus_list = read_list(raw_corpus_path)
    move_repeat_corpus_list = []
    topic_corpus_map = {}
    
    topic_name = ''
    temp_corpus_list = []
    for line in raw_corpus_list:
        line = line.strip()
        if line in topic_list:
            if len(temp_corpus_list) != 0:
                if topic_name in topic_corpus_map:
                    print('>>>>>format error!exit!<<<<<')
                    exit()
                topic_corpus_map[topic_name] = temp_corpus_list
            topic_name  = line
            temp_corpus_list = []
            continue
        temp_corpus_list.append(line)
        if line in move_repeat_corpus_list:
            print('>>>>>repeat corpus<<<<<')
            print('line:',line)
            print('>>>>>exit<<<<<')
        move_repeat_corpus_list.append(line)
            
    with codecs.open(output_path,'w','utf-8') as write_file:
        for key in topic_corpus_map:
            lines = topic_corpus_map[key]
            for line in lines:
                write_file.write(key + '\t' + line + '\r\n')
    
    print('build_standard_check_corpus ok')
    

if __name__ == '__main__':
    topic_list_path = '../../data/total/svm_topic_list.txt'
    raw_corpus_path = '../../data/standard_test_case.txt'
    output_path = '../../corpus/standard_check_case.txt'
    build_standard_check_corpus(topic_list_path,raw_corpus_path,output_path)
    