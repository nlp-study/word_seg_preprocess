'''
Created on Jan 20, 2017

@author: zhang
'''
def compare_two_files(input_path_1,input_path_2):
    
    tag_char_postion(word_list_1)

def compare_two_lines(word_list_1,word_list_2):
    tag_char_postion(word_list_1)

def tag_char_postion(word_list):
    for term in word_list:
        char_list = list(term)
        char_position_list = [(x,'m') for x in char_list ]
        char_position_list[0][1] = 's'
        char_position_list[0][len(char_position_list)-1] = 'e'

def levenshtein(first,second):  
        if len(first) > len(second):  
            first,second = second,first  
        if len(first) == 0:  
            return len(second)  
        if len(second) == 0:  
            return len(first)  
        first_length = len(first) + 1  
        second_length = len(second) + 1  
        distance_matrix = [range(second_length) for x in range(first_length)]   
        #print distance_matrix  
        for i in range(1,first_length):  
            for j in range(1,second_length):  
                deletion = distance_matrix[i-1][j] + 1  
                insertion = distance_matrix[i][j-1] + 1  
                substitution = distance_matrix[i-1][j-1]  
                if first[i-1] != second[j-1]:  
                    substitution += 1  
                distance_matrix[i][j] = min(insertion,deletion,substitution)  
        print(distance_matrix)  
        return distance_matrix[first_length-1][second_length-1]  
    
if __name__ == '__main__':
    first = 'fafdfafa'
    second = 'fafd12fafa'
    levenshtein(first,second)