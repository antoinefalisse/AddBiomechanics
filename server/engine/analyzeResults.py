import os
import shutil
import json
# import nimblephysics as nimble
import numpy as np
import pandas as pd

path_main = os.getcwd()
# path_server = os.path.dirname(path_main)
# path_data = os.path.join(path_server, 'data')

dataDir = 'C:/MyDriveSym/Projects/openpose-augmenter/Data_opensim/'

# Pick dataset
dataset = 'cycling_anthony_cleaned'

if dataset == 'cmu_dataset':
    
    # processed_subjects = ['01']
    
    processed_subjects = ['105', '21', '114', '82', '33', '02', '133', '103',
                          '141', '39', '104', '01', '56', '111', '38', '23',
                          '125', '143', '64', '49', '127', '45', '06', '35',
                          '61', '20', '126', '03', '90', '16', '139', '75',
                          '07', '43', '115', '89', '10', '93', '79', '73',
                          '46', '34', '76', '123', '88', '25', '140', '70',
                          '37', '84', '08', '11', '118', '128', '107', '134',
                          '24']
    
    marker_set_fixed = ['C7', 'T10', 'CLAV', 'STRN', 'RELB', 'RWRA', 'RWRB',
                        'LELB', 'LWRA', 'LWRB', 'RFWT', 'LFWT', 'RBWT', 'LBWT',
                        'RKNE', 'RANK', 'RHEE', 'RTOE', 'RMT5', 
                        'LKNE', 'LANK', 'LHEE', 'LTOE', 'LMT5']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    with open('Report_rmses.txt', 'w') as f:
        for subject in os.listdir(path_clean_dataset):
            if subject in processed_subjects:
                # print("Processing subject {}".format(subject))
                
                pathSubject = os.path.join(path_clean_dataset, subject)            
                pathResults = os.path.join(pathSubject, 'osim_results')
                if not os.path.exists(os.path.join(pathResults, 'Models', 'optimized_scale_and_markers.osim')):
                    os.chdir(pathResults)
                    cmd = 'opensim-cmd run-tool Models/rescaling_setup.xml'
                    os.system(cmd)
                    os.chdir(path_main)
                
                pathC3D = os.path.join(pathResults, 'C3D') 
                pathIK = os.path.join(pathResults, 'IK')
                
                count = 0
                for file in os.listdir(pathC3D):                
                    # Check marker error
                    filename = file[:-4] + '_ik_per_marker_error_report.csv'
                    pathMarkerError = os.path.join(pathIK, filename)
                    marker_error_all = pd.read_csv(pathMarkerError)
                    
                    marker_error = np.zeros((marker_error_all.shape[0], len(marker_set_fixed)))
                    
                    for m, marker in enumerate(marker_set_fixed):
                        marker_error[:, m] = marker_error_all[marker]
                        
                    marker_error_metrics = {}
                    marker_error_metrics['mean_frames'] = np.mean(marker_error, axis=1)
                    marker_error_metrics['std_frames'] = np.std(marker_error, axis=1)
                    marker_error_metrics['mean_all'] = np.mean(marker_error_metrics['mean_frames'])
                    marker_error_metrics['std_frames'] = np.std(marker_error_metrics['mean_frames'])
                    
                    marker_error_metrics['max_frames'] = np.max(marker_error, axis=1)
                    marker_error_metrics['max_all'] = np.max(marker_error_metrics['max_frames'])
                    
                    if marker_error_metrics['mean_all'] > 0.04:
                        print("Mean error for subject {}, trial {} is {} mm".format(subject, file[:-4], np.round(marker_error_metrics['mean_all'], 4)*1000))
                        f.write("Mean error for subject {}, trial {} is {} mm\n".format(subject, file[:-4], np.round(marker_error_metrics['mean_all'], 4)*1000))
                        count += 1
                        
                if count == len(os.listdir(pathC3D)):
                    print('Only bad trials for subject {}'.format(subject))
                        
                    test = 1
                    
                    
elif dataset == 'cycling_anthony_cleaned':
    
    # processed_subjects = ['01']
    
    processed_subjects = ['P020']
    
    # marker_set_fixed = ['C7', 'T10', 'CLAV', 'STRN', 'RELB', 'RWRA', 'RWRB',
    #                     'LELB', 'LWRA', 'LWRB', 'RFWT', 'LFWT', 'RBWT', 'LBWT',
    #                     'RKNE', 'RANK', 'RHEE', 'RTOE', 'RMT5', 
    #                     'LKNE', 'LANK', 'LHEE', 'LTOE', 'LMT5']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    with open('Report_rmses_cycling.txt', 'w') as f:
        for subject in os.listdir(path_clean_dataset):
            if subject in processed_subjects:
                # print("Processing subject {}".format(subject))
                
                pathSubject = os.path.join(path_clean_dataset, subject)            
                pathResults = os.path.join(pathSubject, 'osim_results')
                if not os.path.exists(os.path.join(pathResults, 'Models', 'optimized_scale_and_markers.osim')):
                    os.chdir(pathResults)
                    cmd = 'opensim-cmd run-tool Models/rescaling_setup.xml'
                    os.system(cmd)
                    os.chdir(path_main)
                
                # pathC3D = os.path.join(pathResults, 'C3D') 
                # pathIK = os.path.join(pathResults, 'IK')
                
                # count = 0
                # for file in os.listdir(pathC3D):                
                #     # Check marker error
                #     filename = file[:-4] + '_ik_per_marker_error_report.csv'
                #     pathMarkerError = os.path.join(pathIK, filename)
                #     marker_error_all = pd.read_csv(pathMarkerError)
                    
                #     marker_error = np.zeros((marker_error_all.shape[0], len(marker_set_fixed)))
                    
                #     for m, marker in enumerate(marker_set_fixed):
                #         marker_error[:, m] = marker_error_all[marker]
                        
                #     marker_error_metrics = {}
                #     marker_error_metrics['mean_frames'] = np.mean(marker_error, axis=1)
                #     marker_error_metrics['std_frames'] = np.std(marker_error, axis=1)
                #     marker_error_metrics['mean_all'] = np.mean(marker_error_metrics['mean_frames'])
                #     marker_error_metrics['std_frames'] = np.std(marker_error_metrics['mean_frames'])
                    
                #     marker_error_metrics['max_frames'] = np.max(marker_error, axis=1)
                #     marker_error_metrics['max_all'] = np.max(marker_error_metrics['max_frames'])
                    
                #     if marker_error_metrics['mean_all'] > 0.04:
                #         print("Mean error for subject {}, trial {} is {} mm".format(subject, file[:-4], np.round(marker_error_metrics['mean_all'], 4)*1000))
                #         f.write("Mean error for subject {}, trial {} is {} mm\n".format(subject, file[:-4], np.round(marker_error_metrics['mean_all'], 4)*1000))
                #         count += 1
                        
                # if count == len(os.listdir(pathC3D)):
                #     print('Only bad trials for subject {}'.format(subject))
                        
                #     test = 1
                    
                
                
            
            
            
        #     if not subject in bad_trials:
        #         continue
            
        #     path_subject = os.path.join(path_clean_dataset, subject)
        #     path_trials = os.path.join(path_subject, 'trials')
            
        #     for trial in os.listdir(path_trials):
                
        #         if trial in bad_trials[subject]:
        #             print('Remove trial {}'.format(trial))
        #             # shutil.rmtree(os.path.join(path_trials, trial))
        #             count += 1
                    
        # if not os.listdir(path_trials):
        #     print('Remove subject {}'.format(subject))
        #     # shutil.rmtree(os.path.join(path_clean_dataset, subject))
        #     count1 += 1
            
    # print('Removed {} trials'.format(count))
    # print('Removed {} subjects'.format(count1))                