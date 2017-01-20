'''
Created on 2016年5月5日

@author: Zhang Xiulong
'''
import codecs
from tools.list_operation import *

def trans_word_freq_2_doc(input_path,output_path):
    word_freq_map = {}
    processed_word_freq_map = {}
    generated_str = []
    max_value = 0
    min_value = 0
    read_file = codecs.open(input_path,'r','utf-8')
    for line in read_file:
        line = line.strip()
        if len(line) == 0:
            continue
        line_list = line.split('\t')
        word = line_list[0]
        freq = int(line_list[1])
        word_freq_map[word] = freq
    print('word_freq_map size:',len(word_freq_map))
    read_file.close()
    
    sorted_freq_words = sorted(word_freq_map.items(), key=lambda d:d[1], reverse = True)
    print(dict)
    
    for i in range(len(sorted_freq_words)):
        word_iterm = sorted_freq_words[i]
        processed_word_freq_map[word_iterm[0]] = len(sorted_freq_words) - i
    
#     print(processed_word_freq_map)
#     temp_processed_word_freq_map = sorted(processed_word_freq_map.items(), key=lambda d:d[1], reverse = True)
#     print('temp_processed_word_freq_map:',temp_processed_word_freq_map)
    
    
#     value_list = list(word_freq_map.values())
#     value_list.sort()
#     print(value_list)
#     min_value = value_list[0]
#     max_value = value_list[-1]
#     
#     for key in word_freq_map:
#         value =  word_freq_map[key]
#         value = value - min_value + 1
#         multiple = value / 100
#         processed_word_freq_map[key] += int(multiple)

    write_sorted_str_int_map(processed_word_freq_map,'../../result_data/temp.txt')
    temp_processed_word_freq_tulp = sorted(processed_word_freq_map.items(), key=lambda d:d[1], reverse = True)
    
    for i in range(len(temp_processed_word_freq_tulp)):
        temp_item = temp_processed_word_freq_tulp[i]
        word = temp_item[0]
        freq = int(temp_item[1])
        if i%100 == 0:
            print('index:',i)
        for j in range(freq):
            generated_str.append(word)
    print('length of generated_str:',len(generated_str))
    print('last one generated_str:',generated_str[-3:-1])
    
    write_file = codecs.open(output_path,'w','utf-8')
    line_str = ''
    for i in range(len(generated_str)):
        line_str += generated_str[i] + ' '
        if i % 50 == 0:
            write_file.write(line_str + '\n')
            line_str = ''
    write_file.write(line_str + '\n')
    write_file.close()

def check_word_freq_correct(file_path_1,file_path_2):
    check_list_1 = read_list(file_path_1)
    check_list_2 = read_list(file_path_2)
    if len(check_list_1) != len(check_list_2):
        print('>>>>Error,two check list is not same length!,Exit<<<<<')
        exit()
    for i in range(len(check_list_1)):
        line_1 = check_list_1[i]
        word_1 = line_1.split('\t')[0]
        line_2 = check_list_2[i]
        word_2 = line_2.split('\t')[0]   
        if word_1 != word_2:
            print(word_1,word_2,' is not same!')
                 
    

if __name__ == '__main__':
    input_path = '../../result_data/cleaned_wrod_freq.txt'
    output_path = '../../result_data/wrod_freq_2_doc.txt'
    trans_word_freq_2_doc(input_path,output_path)
    check_word_freq_correct(input_path,output_path)