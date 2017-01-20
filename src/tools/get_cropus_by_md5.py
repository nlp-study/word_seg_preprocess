'''
Created on 2016年7月18日

@author: Zhang Xiulong
'''
from tools.list_operation import *
from tools.text_process import *

def get_corpus_by_md5(input_md5_path,corpus_path,extract_corpus_path):
    md5_list = read_list(input_md5_path)
    corpus_list = read_list(corpus_path)
    extract_md5_corpus_map = {}
    extract_corpus_list = []
    for line in corpus_list:
        topic_name,corpus_content,md5 = split_line_2_list(line,'\t',3)
        md5 = md5.strip()
        if md5 in md5_list:
            corpus_content = corpus_content.strip()
#             if corpus_content in extract_corpus_list:
#                 continue
            extract_md5_corpus_map[md5] = corpus_content
    for md5 in md5_list:
        content = extract_md5_corpus_map[md5]
        extract_corpus_list.append(content)
    write_list(extract_corpus_list,extract_corpus_path)
    print('extract_md5_corpus_map size:',len(extract_md5_corpus_map))
    print('get_corpus_by_md5 ok!')
    
    
if __name__ == '__main__':
    input_md5_path = '../../result_data/temp.txt'
    corpus_path = '../../corpus/classification_corpus.txt'
    extract_corpus_path = '../../result_data/get_corpus_by_md5.txt'
    get_corpus_by_md5(input_md5_path,corpus_path,extract_corpus_path)
    
    