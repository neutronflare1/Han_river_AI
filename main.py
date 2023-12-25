# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 10:41:31 2023

@author: minchotuna
"""

import tkinter as tk

import API_data as data

class DataManager:
    def __init__(self, root):
        self.root = root
        
        
        tempsys = data.HanRiverTempParser()
        tempsys.data_setting()
        
        tempsys.load_data()
        

root = tk.Tk()
DataManager(root)