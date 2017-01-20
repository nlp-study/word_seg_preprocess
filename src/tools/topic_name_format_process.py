'''
Created on 2016年7月4日

@author: Zhang Xiulong
'''
from tools.list_operation import *

def process_topicName_format(input_path,output_path):
    domain_numb = 0
    topic_numb = 0
    domain_line = "\"Other\","
    topic_list = read_list(input_path)
    domain_topic_map = {}
    for line in topic_list:
        line = line.strip()
        if len(line) == 0:
            continue
        if line.startswith('#'):
            domain_name = line.replace('#','')
            if domain_name in domain_topic_map:
                print('Error,topic_name is repeat!exit')
                exit()
            domain_topic_map[domain_name] = []
            domain_line += "\"" + domain_name + "\","
            continue
        domain_topic_map[domain_name].append(line)
        domain_line.strip(',')
        
    result_list = []  #domain_name tab "topic_name_1","topic_name_2",....
    result_list.append(domain_line)
    for domain_name in domain_topic_map:
        domain_numb += 1
        
        if domain_name == 'Open_Account':
            line = 'var openAccount = new Array('
        elif domain_name == 'Account_Management':
            line = 'var openManagement = new Array('
        elif domain_name == 'Fund_Transaction':
            line = 'var fundTransaction = new Array('
        elif domain_name == 'Current_Bao':
            line = 'var currentBao = new Array('
        elif domain_name == 'Index_Bao':
            line = 'var indexBao = new Array('
        elif domain_name == 'Fixed_Bao':
            line = 'var fixedBao = new Array('
        elif domain_name == 'Zhong_Cai_Suo':
            line = 'var zhongCaiSuo = new Array('
        elif domain_name == 'Form':
            line = 'var form = new Array('
        elif domain_name == 'Super_Transformation':
            line = 'var superTransformation = new Array('
        elif domain_name == 'Enterprise':
            line = 'var enterprise = new Array('
        elif domain_name == 'EastMonmey':
            line = 'var eastmoney = new Array('
        elif domain_name == 'High-End_Financial_Management':
            line = 'var highEndFinance = new Array('
        elif domain_name == 'General':
            line = 'var general = new Array('
        else:
            print('>>>>>Error:domain name is illegal!<<<<<')
            print('domain:',domain_name)
            exit()
        temp_topic_list = domain_topic_map[domain_name]
        for topic_name in temp_topic_list:
            topic_numb += 1
            line += "\"" + topic_name +  "\","
        line = line.rstrip(',')
        line += ');'
        result_list.append(line)
    write_list(result_list,output_path)
    
    print('domain numb:',domain_numb)
    print('topic numb:',topic_numb)
            
        
            
            
    
if __name__ == '__main__':
    input_path = '../../data/domain_topic.txt'
    output_path = '../../result_data/domain_topic.txt'
    process_topicName_format(input_path,output_path)
    