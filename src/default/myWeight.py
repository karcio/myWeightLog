#!/usr/bin/python
'''
Created on 3 Jul 2017

@author: crystal
'''

import csv
import datetime


def title():
    print('Weight v 0.1')
    print('====================')

def insertData():
    weight = input('Insert weight: ')
    
    print('done ...')
    with open('weight.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['{:%Y-%m-%d}'.format(datetime.datetime.now()), weight])
    
title()
insertData()