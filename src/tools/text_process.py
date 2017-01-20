'''
Created on 2016年7月7日

@author: Zhang Xiulong
'''

def split_line_2_list(line,split_token,elimit_size):
    line = line.strip()
    if len(line) == 0:
        return []
    line_list = line.split(split_token)
    if elimit_size!= None and len(line_list) != elimit_size:
        print('>>>>>Error,line format is illegal<<<<<')
        print('line:',line)
        print('>>>>>Exit<<<<<')
        exit()
    return line_list


def split_line_2_list_with_token(line,split_token,elimit_size,token):
    line = line.strip()
    if len(line) == 0:
        return []
    line_list = line.split(split_token)
    if elimit_size!= None and len(line_list) != elimit_size:
        print('>>>>>Error,'+token+' format is illegal<<<<<')
        print('line:',line)
        print('>>>>>Exit<<<<<')
        exit()
    return line_list

if __name__ == '__main__':
    pass