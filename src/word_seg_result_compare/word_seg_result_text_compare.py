'''
Created on Jan 20, 2017

@author: zhang
'''
POSITION_BEGAIN = 'B'
POSITION_END = 'E'
POSITION_MIDDLE = 'M'
POSITION_SINGLE = 'S'

from tools.list_operation import read_list
def compare_two_files(input_path_1,input_path_2):
    line_list_1 = read_list(input_path_1)
    line_list_2 = read_list(input_path_2)
    if len(line_list_1) != len(line_list_2):
        print('Error:line size is not equal!exit!')
        exit()
    
    for i in range(len(line_list_1)):
        word_list_1,part_speech_list_1 = get_word_list(line_list_1[i])
        word_list_2,part_speech_list_2 = get_word_list(line_list_2[i])
        is_same_list, not_same_list_1,not_same_list_2 = compare_two_lines_words(word_list_1,word_list_2)
        not_same_word_list_1 = [word_list_1[x] for x in not_same_list_1]
        not_same_word_list_2 = [word_list_2[x] for x in not_same_list_2]
#         print('is_same_list:',is_same_list)
        print('*************************************************************')
        if len(is_same_list) !=0:
            print('not_same_word_list_1:',not_same_word_list_1)
            print('not_same_word_list_2:',not_same_word_list_2)
        else:
            print('two lines is same')
#         print('exit')
#         exit()

def compare_two_lines_words(word_list_1,word_list_2):
    word_position_tag_list_1 = tag_char_postion(word_list_1)
    word_position_tag_list_2 = tag_char_postion(word_list_2)
    if len(word_position_tag_list_1) != len(word_position_tag_list_2):
        print('Error:word size is not equal,exit!')
        print('word_list_1 size:',len(word_list_1))
        print('word_list_1:',word_list_1)
        print('word_list_2 size:',len(word_list_2))
        print('word_list_2 :',word_list_2)
        exit()
        
    is_same_list = [1]*len(word_position_tag_list_1)
    not_same_set_1 = set()
    not_same_set_2 = set()
    for i in range(len(word_position_tag_list_1)):
        word_position_tag_1 = word_position_tag_list_1[i]
        word_position_tag_2 = word_position_tag_list_2[i]
        
        if(word_position_tag_1[0] != word_position_tag_2[0]):
            print('Error:word is not equal!')
        if(word_position_tag_1[1] != word_position_tag_2[1]):
            is_same_list[i] = 0
            not_same_set_1.add(word_position_tag_1[2])
            not_same_set_2.add(word_position_tag_2[2])
            j = i-1
            if is_same_list[j] == 0:
                continue
            if word_position_tag_1[1] ==POSITION_END or word_position_tag_1[1] ==POSITION_MIDDLE:
                is_same_list[j] = 0
                not_same_set_1.add(word_position_tag_list_1[j][2])
                not_same_set_2.add(word_position_tag_list_2[j][2])
#     print(is_same_list)
    not_same_list_1 = list(not_same_set_1)
    not_same_list_2 = list(not_same_set_2)
    not_same_list_1.sort()
    not_same_list_2.sort()
    return is_same_list,not_same_list_1,not_same_list_2
        
    
def get_word_list(line):
    word_list = []
    part_speech_list = []
    word_part_speech_list = line.split(',')
    for word_part_speech in word_part_speech_list:
#         print('word_part_speech:',word_part_speech)
        term_list = word_part_speech.split('/')
        term_list = [term.strip() for term in term_list]
        word = term_list[0]
        part_spech = term_list[1]
        word_list.append(word)
        part_speech_list.append(part_spech)
    return word_list,part_speech_list
        
        

def tag_char_postion(word_list):
    char_position_list = []
    if len(word_list) == 0:
        return char_position_list
    char_position_list = []
    for i in range(len(word_list)):
        term = word_list[i]
        char_list = list(term)
        char_size = len(char_list)
        if char_size == 0:
            continue
        temp_char_position_list = [()]*char_size
        if char_size > 1:
            if char_size > 2:
                temp_char_position_list = [(x,POSITION_MIDDLE,i) for x in char_list ]
            temp_char_position_list[0] = (char_list[0],POSITION_BEGAIN,i)
            temp_char_position_list[char_size-1] = (char_list[char_size-1],POSITION_END,i)
        else:
            temp_char_position_list[0] = (char_list[0],POSITION_SINGLE,i)
        char_position_list += temp_char_position_list
#     print('char_position_list:',char_position_list)
    return char_position_list
        


    
if __name__ == '__main__':
    first = '../../data/result_compare/test_1.txt'
    second = '../../data/result_compare/test_2.txt'
    compare_two_files(first,second)
    
    