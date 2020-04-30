# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 01:12:46 2020

@author: Shivam
"""
import cv2
import os
import pydicom
import glob

inputdir = './'
outdir = './'

f = 'tryimage.dcm'

ds = pydicom.read_file(inputdir+f)
img = ds.pixel_array
cv2.imwrite(outdir+f.replace('.dcm','.jpg'),img)
