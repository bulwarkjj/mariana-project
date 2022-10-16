""" 
Script to check/create dir on host machine to hold plotly graphs and metrics

maintainer: Matthew Moroge
"""

import os

#desktop_dir = 'C:\\Users\\"%USERNAME%"\\Desktop\\report-metrics'
desktop_dir = os.path.join(os.getcwd(), "Desktop")

print(desktop_dir)

def create_dir():
    """ 
    Method to check if dir exists, if not than creates one
    """

    if not os.path.exists(desktop_dir):
        os.makedirs(desktop_dir)