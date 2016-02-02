#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Bruce Chen'

import csv
import numpy as np


csv_file_obj = csv.reader(open('train.csv','r'))
header = next(csv_file_obj)

data = []
for row in csv_file_obj:
    data.append(row)
data=np.array(data)

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survived = number_survived/number_passengers

women_only_stats = data[0::,4]=='female'
men_only_stats = data[0::,4]!='female'

women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)

proportion_women_survived = np.sum(women_onboard)/np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard)/np.size(men_onboard)

print('Proportion of women who survived is %s' % proportion_women_survived)
print('Proportion of men who survived is %s' % proportion_men_survived)

test_file = open('test.csv','r')
test_file_obj = csv.reader(test_file)
header = next(test_file_obj)

prediction_file = open('genderbasemodel.csv','w')
prediction_file_obj = csv.writer(prediction_file)

prediction_file_obj.writerow(['PassengerId','Survived'])
for row in test_file_obj:
    if row[3] == 'female':
        prediction_file_obj.writerow([row[0],'1'])
    else:
        prediction_file_obj.writerow([row[0],'0'])
test_file.close()
prediction_file.close()
