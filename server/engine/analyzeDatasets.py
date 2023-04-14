import os
import shutil
import json
import numpy as np
import pandas as pd

path_main = os.getcwd()
# path_server = os.path.dirname(path_main)
# path_data = os.path.join(path_server, 'data')

dataDir = 'C:/MyDriveSym/Projects/openpose-augmenter/Data_opensim/'

# Pick dataset
dataset = 'toeheel_walking_dataset'

if dataset == 'toeheel_walking_dataset':    
    marker_set_fixed = ['R_Asis', 'L_Asis', 'Psis', 'R_LatCon', 'R_LatMal', 'R_Toe1', 'R_Meta5', 'R_Heel', 'L_LatCon', 'L_LatMal', 'L_Toe1', 'L_Heel', 'L_Meta5',
                        'R_Should', 'L_Should', 'C7', 'R_Elbow', 'R_Wrist', 'L_Elbow', 'L_Wrist']    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    subjects = []
    for subject in os.listdir(path_clean_dataset):
        
        if 'Subject' not in subject or '.mat' in subject:
            continue
        
        subjects.append(subject)
            
        pathSubject = os.path.join(path_clean_dataset, subject)            
        pathResults = os.path.join(pathSubject, 'osim_results_cleaned')           
            
        pathC3D = os.path.join(pathResults, 'MarkerData') 
        pathIK = os.path.join(pathResults, 'IK')
        
        count = 0
        for file in os.listdir(pathC3D):
            
            if not '.trc' in file:
                continue
            
            # Check marker error            
            filename = file[:-4] + '_marker_errors.csv'
            pathMarkerError = os.path.join(pathIK, filename)
            marker_error_all = pd.read_csv(pathMarkerError)
            
            marker_error = np.zeros((marker_error_all.shape[0], len(marker_set_fixed)))
            
            for m, marker in enumerate(marker_set_fixed):
                if marker in marker_error_all:
                    marker_error[:, m] = marker_error_all[marker]
                else:
                    # print("Marker {} not in csv report".format(marker))
                    marker_error[:, m] = np.nan
                
            marker_error_metrics = {}
            marker_error_metrics['mean_frames'] = np.nanmean(marker_error, axis=1)
            marker_error_metrics['std_frames'] = np.nanstd(marker_error, axis=1)
            marker_error_metrics['mean_all'] = np.nanmean(marker_error_metrics['mean_frames'])
            marker_error_metrics['std_frames'] = np.nanstd(marker_error_metrics['mean_frames'])
            
            marker_error_metrics['max_frames'] = np.max(marker_error, axis=1)
            marker_error_metrics['max_all'] = np.max(marker_error_metrics['max_frames'])
            
            if marker_error_metrics['mean_all'] > 0.025:
                print("Mean error for subject {}, trial {} is {} mm".format(subject, file[:-4], np.round(marker_error_metrics['mean_all'], 4)*1000))
                # f.write("Mean error for subject {}, trial {} is {} mm\n".format(subject, file[:-4], np.round(marker_error_metrics['mean_all'], 4)*1000))
                count += 1
                # rename file
                pathFile = os.path.join(pathIK, file[:-4] + '_ik.mot')
                pathFileEnd = os.path.join(pathIK, file[:-4] + '_ik_error_larger_25mm.mot')
                if not os.path.exists(pathFileEnd):
                    os.rename(pathFile, pathFileEnd)
                
        if count == len(os.listdir(pathC3D)):
            print('Only bad trials for subject {}'.format(subject))
            # f.write("Only bad trials for subject {}\n".format(subject))                
            test = 1