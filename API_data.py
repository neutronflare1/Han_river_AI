# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 04:58:36 2023

@author: minchotuna
"""

import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
#import tensorflow.keras as keras
import requests
import os
import json

class HanRiverTempParser:
    file_path = os.path.dirname(os.path.abspath(__file__))
    
    def __init__(self):
        #learn = LearningPattern()
        pass
    
    def data_setting(self):
        url = 'http://openapi.seoul.go.kr:8088/6c715655736e6575343376464a6d44/json/WPOSInformationTime/1/1000/'
        temp_data=requests.get(url)
        json_data = temp_data.json()
        with open(f"{os.path.join(self.file_path, 'data', 'temp_data.json')}", 'w+', encoding="UTF-8") as make_file:
            json.dump(json_data, make_file, ensure_ascii=False, indent="\t")
            
    def load_data(self):
        with open(f"{os.path.join(self.file_path, 'data', 'temp_data.json')}", 'r', encoding="UTF-8") as read_file:
            data = json.load(read_file)
            illiterater = (lambda x : data["WPOSInformationTime"]["row"][i][x] for i in range(1000) if  i % 4 == 0)
            for i in range(1000):
                # 데이터가 너무 많아서 노량진만 타깃으로 정함
                date = [illiterater("MSR_DATE")]
                time = [illiterater("MSR_TIME")]
                temp = [illiterater("W_TEMP")]
            
class LearningPattern:
    def __init__():
        pass
    
