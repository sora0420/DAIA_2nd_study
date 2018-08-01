import csv
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from itertools import chain

train_payment = pd.read_csv('train_payment.csv')
train_label1 = pd.read_csv('train_label.csv')

#print(train_payment._getitem_column('acc_id')[0])
list = []
list1 = []
list2 = []
list3 = []
test = open("aaaa.csv", 'w')
for i in range(80000):
    list.append(train_payment._getitem_column('acc_id')[i])
    list1.append(train_payment._getitem_column('payment_week')[i])
    list2.append(train_payment._getitem_column('payment_amount')[i])

#list1, list2를 1~8로 잘라서 묶기
#for i in range(0,80000,8):
for i in range(0,80000,8):
    x = np.array([["%d"%(list1[i]),list2[i]],
                   [list1[i+1], list2[i+1]],
                   [list1[i+2], list2[i+2]],
                    [list1[i+3], list2[i+3]],
                    [list1[i+4], list2[i+4]],
                    [list1[i+5], list2[i+5]],
                    [list1[i+6], list2[i+6]],
                    [list1[i+7], list2[i+7]]])
    list3.append(x)

dic1 = {}

for i in range(len(list3)):
    dic1[list[i+7]] = list3[i]
    test.write(str(dic1))
test.close()

testfile = open("aaaa.csv", 'r')
aa = testfile.read()
print("aa print",aa)