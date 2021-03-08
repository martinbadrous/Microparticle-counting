#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:53:00 2021

@author: mscv
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['8.565','8.585','8.605','8.625','8.645','8.665']
Contour = [6, 22, 74, 54, 20, 2]
HOUGH = [14, 35, 85, 67, 19,4]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Contour, width, label='Contour')
rects2 = ax.bar(x + width/2, HOUGH, width, label='Hough')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('No. of Detected Particles')
ax.set_xlabel('Focal Points in MilliMeter')
ax.set_title('Count of detected particles using the two Methods')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
#ax.set_xlim([xmi,xmax])
ax.set_ylim([0,95])

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()