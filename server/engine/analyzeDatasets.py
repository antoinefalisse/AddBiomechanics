import os
import shutil
import json
import nimblephysics as nimble
import numpy as np

path_my_datasets = '/home/clarkadmin/Documents/myDatasets_Antoine'
path_main = os.getcwd()
path_server = os.path.dirname(path_main)
path_data = os.path.join(path_server, 'data')

# Generic data
subject_data = {'massKg': 68,
                'heightM': 1.6,
                'sex': 'unknowm',
                'skeletonPreset': 'custom'}

# Pick dataset
dataset = 'cmu_dataset'

if dataset == 'cmu_dataset':
    
    marker_set_fixed = ['C7', 'T10', 'CLAV', 'STRN', 'RELB', 'RWRA', 'RWRB',
                        'LELB', 'LWRA', 'LWRB', 'RFWT', 'LFWT', 'RBWT', 'LBWT',
                        'RKNE', 'RANK', 'RHEE', 'RTOE', 'RMT5', 
                        'LKNE', 'LANK', 'LHEE', 'LTOE', 'LMT5']
    
    path_original_dataset = os.path.join(path_my_datasets, dataset)
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    # Loop over subjects
    with open('README.txt', 'w') as f:
        for subject in os.listdir(path_clean_dataset):
        # subject = '90'
            if os.path.isdir(os.path.join(path_original_dataset, subject)):
                print("Processing subject {}".format(subject))
                
                path_subject = os.path.join(path_clean_dataset, subject)
                path_trials = os.path.join(path_subject, 'trials')
                
                for trial in os.listdir(path_trials):
                    print("Processing trial {}".format(trial))
                    path_c3d = os.path.join(path_trials, trial, 'markers.c3d')
                    c3dFile: nimble.biomechanics.C3D = nimble.biomechanics.C3DLoader.loadC3D(
                        path_c3d)
                    markerTrial = c3dFile.markerTimesteps
                    
                    if len(markerTrial) == 0:
                        f.write('For subject {}, trial {}, no marker data'.format(subject, trial))
                        continue
                    
                    if len(markerTrial) > 20:
                        max_f = 20
                    else:
                        max_f = len(markerTrial)
                        
                    max_frames = np.zeros((max_f,))
                    for c_f in range(max_f):
                        count = 0                   
                        for c_m in marker_set_fixed:
                            if c_m in list(markerTrial[c_f].keys()):
                                count += 1
                        max_frames[c_f] = count
                    max_max_frames = int(np.max(max_frames))
                    
                    if max_max_frames != 24:
                        f.write('For subject {}, trial {}, different marker set'.format(subject, trial))
                        f.write("\n")
            f.write("\n")