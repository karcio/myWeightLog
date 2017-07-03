#!/usr/bin/python
'''
Created on 3 Jul 2017

@author: crystal
'''

import argparse
import csv
import datetime


parser = argparse.ArgumentParser()
parser.add_argument("location", action="store", help="provide location for csv file")
args = parser.parse_args()

def title():
    print('Weight v 0.1')
    print('====================')
    

def insertData():
    weight = input('Insert weight: ')
    
    print('done ...')
    
    with open(args.location + 'weight.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['{:%Y-%m-%d}'.format(datetime.datetime.now()), weight])
    
title()
insertData()