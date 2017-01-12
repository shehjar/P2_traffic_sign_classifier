# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 18:21:08 2017

@author: admin
"""
import cv2
import pickle, os
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas
newDataFolder = os.path.join(os.getcwd(),'new_traffic_signs')
with open(os.path.join(newDataFolder,'new_signs.p'), 'rb') as file:
    newData = pickle.load(file)
    
#print(newData)
new_X_test = newData['data']
new_y_test = newData['labels']

n_newData = new_X_test.shape[0]
name_Dict = {}
with open(os.path.join(os.getcwd(),'signnames.csv'),'r') as csvfile:
    classData = csv.DictReader(csvfile)
    for row in classData:
        index = int(row['ClassId'])
        name = row['SignName']
        name_Dict[index] = name