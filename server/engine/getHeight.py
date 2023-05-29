import os
import dataman
import numpy as np

path_main = os.getcwd()
path_server = os.path.dirname(path_main)
path_data = os.path.join(path_server, 'data')

dataset = 'totalcapture_2'

if dataset == 'totalcapture_2':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('s4_acting3' in file):
            pathStatic = os.path.join(path_dataset, file, 'trials', 'static', 'markers.trc')
            trc_file = dataman.TRCFile(pathStatic)
            
            
            top_head = np.max(trc_file.marker('ARIEL')[:,1])
            print(top_head)
            # left_toe = np.min(trc_file.marker('LTOE')[:,1])
            # right_toe = np.min(trc_file.marker('RTOE')[:,1])
            # toe = np.min([left_toe,right_toe]) - 
            




