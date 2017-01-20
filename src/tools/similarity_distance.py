'''
Created on 2016年6月3日

@author: Zhang Xiulong
'''

def edit_distance(A,B):
    len_A = len(A) + 1
    len_B = len(B) + 1
    if len_A == 1:
        return len_B -1
    if len_B == 1:
        return len_A -1
    matrix = [range(len_A) for x in range(len_B)]
    for i in range(1,len_B):
        matrix[i][0] = i
    for i in range(1,len_B):
        for j in range(1,len_A):
            deletion = matrix[i-1][j]+1
            insertion = matrix[i][j-1]+1
            substitution = matrix[i-1][j-1]
            if B[i-1] != A[j-1]:
                substitution += 1
            matrix[i][j] = min(deletion,insertion,substitution)
    return matrix[len_B-1][len_A-1]



def normal_leven(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
    #create matrix
    matrix = [0 for n in range(len_str1 * len_str2)]
    #init x axis
    for i in range(len_str1):
      matrix[i] = i
    #init y axis
    for j in range(0, len(matrix), len_str1):
      if j % len_str1 == 0:
        matrix[j] = j // len_str1
    
    for i in range(1, len_str1):
      for j in range(1, len_str2):
        if str1[i-1] == str2[j-1]:
          cost = 0
        else:
          cost = 1
        matrix[j*len_str1+i] = min(matrix[(j-1)*len_str1+i]+1,
                      matrix[j*len_str1+(i-1)]+1,
                      matrix[(j-1)*len_str1+(i-1)] + cost)
    
    return matrix[-1]


#!/usr/bin/env python 
# find an LCS (Longest Common Subsequence). 
# *public domain* 
 
def find_lcs_len(s1, s2): 
  m = [ [ 0 for x in s2 ] for y in s1 ] 
  for p1 in range(len(s1)): 
    for p2 in range(len(s2)): 
      if s1[p1] == s2[p2]: 
        if p1 == 0 or p2 == 0: 
          m[p1][p2] = 1
        else: 
          m[p1][p2] = m[p1-1][p2-1]+1
      elif m[p1-1][p2] < m[p1][p2-1]: 
        m[p1][p2] = m[p1][p2-1] 
      else:                             # m[p1][p2-1] < m[p1-1][p2] 
        m[p1][p2] = m[p1-1][p2] 
  return m[-1][-1] 
 
def find_lcs(s1, s2): 
  # length table: every element is set to zero. 
  m = [ [ 0 for x in s2 ] for y in s1 ] 
  # direction table: 1st bit for p1, 2nd bit for p2. 
  d = [ [ None for x in s2 ] for y in s1 ] 
  # we don't have to care about the boundery check. 
  # a negative index always gives an intact zero. 
  for p1 in range(len(s1)): 
    for p2 in range(len(s2)): 
      if s1[p1] == s2[p2]: 
        if p1 == 0 or p2 == 0: 
          m[p1][p2] = 1
        else: 
          m[p1][p2] = m[p1-1][p2-1]+1
        d[p1][p2] = 3                   # 11: decr. p1 and p2 
      elif m[p1-1][p2] < m[p1][p2-1]: 
        m[p1][p2] = m[p1][p2-1] 
        d[p1][p2] = 2                   # 10: decr. p2 only 
      else:                             # m[p1][p2-1] < m[p1-1][p2] 
        m[p1][p2] = m[p1-1][p2] 
        d[p1][p2] = 1                   # 01: decr. p1 only 
  (p1, p2) = (len(s1)-1, len(s2)-1) 
  # now we traverse the table in reverse order. 
  s = [] 
  while 1: 
    print(p1,p2) 
    c = d[p1][p2] 
    if c == 3: s.append(s1[p1]) 
    if not ((p1 or p2) and m[p1][p2]): break
    if c & 2: p2 -= 1
    if c & 1: p1 -= 1
  s.reverse() 
  return ''.join(s) 
 




if __name__ == '__main__':
    A = "DDDDDDdD"
    B = "DFDAFADFD66DDEDDF"
    print(edit_distance(A,B))
    
   
    
    
    
    
    
    