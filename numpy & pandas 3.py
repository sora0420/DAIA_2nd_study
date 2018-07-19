from pandas import Series, DataFrame
import pandas as pd
import numpy as np

char_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

#num_dic = {v for v in enumerate(char_arr)}
#print(num_dic)
#>>{(3, 'd'), (14, 'o'), (22, 'w'),  >>랜덤으로

num_dic = {k:v for v, k in enumerate(char_arr)}
# print(num_dic) >> {'a': 0, 'b': 1, 'c': 2 순서대로
for i in num_dic.values(): #values는 숫자임
    x = np.array([i])
#i = np.eye(26) #단위행렬
#ix = i[x]
#print(ix)

seq_data = ['word', 'wood', 'deep', 'dive', 'cold', 'cool', 'load', 'love', 'kiss', 'kind']

def make_batch(seq_data):
    input_batch = []
    target_batch = []
    seq = seq_data[0]
    for seq in seq_data:
        input = [num_dic[i] for i in seq[:3]] #단어 0~2번째의 숫자를 num_dic a:0~26 숫자위치처럼
        print(input) # [wor] = [22,14,17]
        input_batch.append(np.eye(26)[input]) #단위행렬의 숫자 위치에 1 / 원핫인코딩
        target_batch.append(num_dic[seq[-1]]) #seq_data의 마지막글자의 숫자

        print(input_batch)
        print(target_batch)
    return input_batch, target_batch

if __name__ == "__main__":  # 여기가 main이면 make_batch 실행 / 이게 다른곳에서 import되면 실행x
    input_batch, target_batch = make_batch(seq_data)  # 모듈화