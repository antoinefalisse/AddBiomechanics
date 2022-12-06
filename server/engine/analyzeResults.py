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
dataset = 'hamstrings_dataset'

if dataset == 'cmu_dataset':
    
    # processed_subjects = [
    #     '105', '21', '114', '82', '33', '02', '133', '103', 
    #     '141', '39', '17', '104', '01', '56', '111', '41', 
    #     '38', '23', '125', '143', '64', '49', '127', '45',
    #     '06', '91', '35', '61', '20', '126', '03', '90', 
    #     '16', '139', '75', '07', '43', '31', '115', '89',
    #     '10', '93', '32', '79', '73', '132', '46', '29', 
    #     '34', '54', '76', '123', '88', '83', '25', '142', 
    #     '140', '70', '15', '37', 
    #     '84', '08', '11', '55', 
    #     '113', '26', '80', '78', '102', '118', '128', '107',
    #     '19', '14', '134', '24', '77', '62', '87', '18', 
    #     '124', '42', '135', '40', '05', '94', '122', '137', 
    #     '09', '36', '136', '47', '63', '108', '13', '144', 
    #     '12', '28', '74', '27', '131', '22', '30', '86', 
    #     '120', '85', '60', '106', '138', '150']
    
    processed_subjects = ['138', '150']
    
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
        for subject in processed_subjects:
            if subject in processed_subjects:
                print("Processing subject {}".format(subject))
                
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
                    
                    if not '.c3d' in file:
                        continue
                    
                    # Check marker error
                    filename = file[:-4] + '_ik_per_marker_error_report.csv'
                    pathMarkerError = os.path.join(pathIK, filename)
                    marker_error_all = pd.read_csv(pathMarkerError)
                    
                    marker_error = np.zeros((marker_error_all.shape[0], len(marker_set_fixed)))
                    
                    for m, marker in enumerate(marker_set_fixed):
                        if marker in marker_error_all:
                            marker_error[:, m] = marker_error_all[marker]
                        else:
                            print("Marker {} not in csv report".format(marker))
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
                        f.write("Mean error for subject {}, trial {} is {} mm\n".format(subject, file[:-4], np.round(marker_error_metrics['mean_all'], 4)*1000))
                        count += 1
                        # rename file
                        pathFile = os.path.join(pathIK, file[:-4] + '_ik.mot')
                        pathFile2 = os.path.join(pathIK, file[:-4] + '_ik_error_larger_3cm.mot')
                        pathFileEnd = os.path.join(pathIK, file[:-4] + '_ik_error_larger_25mm.mot')
                        if os.path.exists(pathFile):
                            os.rename(pathFile, pathFileEnd)
                        else:
                            os.rename(pathFile2, pathFileEnd)
                        
                if count == len(os.listdir(pathC3D)):
                    print('Only bad trials for subject {}'.format(subject))
                    f.write("Only bad trials for subject {}\n".format(subject))
                        
                    test = 1
                    
                    
elif dataset == 'cycling_anthony_cleaned':
    
    processed_subjects = ['P003', 'P004', 'P005', 'P006', 'P007', 'P008', 'P011',
                          'P012', 'P013', 'P014', 'P015', 'P016', 'P018', 'P019', 
                          'P020', 'P021', 'P022', 'P023', 'P025', 'P026', 'P028', 
                          'P029', 'P031', 'P032', 'P033', 'P034', 'P036', 'P038',
                          'P039', 'P040', 'P041', 'P042', 'P043', 'P045', 'P050',
                          'P051']
    
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
                    
                    
elif dataset == 'balance_dataset_cleaned':
    
    processed_subjects = ['Subj03', 'Subj04', 'Subj05', 'Subj06', 'Subj07', 'Subj08']
    
    # marker_set_fixed = ['C7', 'T10', 'CLAV', 'STRN', 'RELB', 'RWRA', 'RWRB',
    #                     'LELB', 'LWRA', 'LWRB', 'RFWT', 'LFWT', 'RBWT', 'LBWT',
    #                     'RKNE', 'RANK', 'RHEE', 'RTOE', 'RMT5', 
    #                     'LKNE', 'LANK', 'LHEE', 'LTOE', 'LMT5']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    # with open('Report_rmses_cycling.txt', 'w') as f:
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
                
elif dataset == 'myer_dataset_cleaned':
    
    # sessions = ['PreTesting_2017_fall', 'PreTesting_2017_summer', 'PreTesting_2018_summer', 'PreTesting_2019_fall', 'PreTesting_2019_summer']
    # sessions = ['PreTesting_2017_fall_VR', 'PreTesting_2017_summer_VR', 'PreTesting_2018_summer_VR', 'PreTesting_2019_fall_VR']
    sessions = ['PreTesting_2019_summer_VR']

    
    marker_set_fixed = ['R.Shoulder', 'L.Shoulder', 'Sternum', 'L.ASIS', 'R.ASIS', 'Sacrum', 'R.Knee',
                        'R.Heel', 'R.Toe', 'R.LateralFoot', 'R.PosteriorFoot', 'L.Knee',
                        'L.Heel', 'L.Toe', 'L.LateralFoot', 'L.PosteriorFoot', 'L.Ankle', 'R.Ankle']
    
    marker_set_fixed_VR = ['R.Shoulder', 'L.Shoulder', 'Sternum', 'L.ASIS', 'R.ASIS', 'Sacrum', 'R.Knee',
                        'R.Heel', 'R.Toe', 'R.LateralFoot', 'R.PosteriorFoot', 'L.Knee',
                        'L.Heel', 'L.Toe', 'L.LateralFoot', 'L.PosteriorFoot', 'L.Ankle', 'R.Ankle', 'R.Elbow', 'L.Elbow', 'R.Wrist', 'L.Wrist', 'R.Hand', 'L.MedialHand', 'R.Hand', 'L.MedialHand']
    
    for session in sessions:
        
        pathSession = os.path.join(dataDir, dataset, session)
        
        subjects = []
        for subject in os.listdir(pathSession): 
            
            if not 'anmt' in subject.lower():
                continue
            
            if 'anmt107' in subject.lower():
                continue
            
            pathSubject = os.path.join(pathSession, subject)            
            pathResults = os.path.join(pathSubject, 'osim_results')
            if not os.path.exists(os.path.join(pathResults, 'Models', 'optimized_scale_and_markers.osim')):
                os.chdir(pathResults)
                cmd = 'opensim-cmd run-tool Models/rescaling_setup.xml'
                os.system(cmd)
                os.chdir(path_main)
            
            subjects.append(subject)
            
            pathTRC = os.path.join(pathResults, 'MarkerData')
            pathIK = os.path.join(pathResults, 'IK')
            
            count = 0
            for file in os.listdir(pathTRC):
                
                if not '.trc' in file:
                    continue
                
                if '_VR' in session:
                    marker_set = marker_set_fixed_VR
                else:
                    marker_set = marker_set_fixed
                
                # Check marker error
                filename = file[:-4] + '_ik_per_marker_error_report.csv'
                pathMarkerError = os.path.join(pathIK, filename)
                marker_error_all = pd.read_csv(pathMarkerError)
                
                marker_error = np.zeros((marker_error_all.shape[0], len(marker_set)))
                
                for m, marker in enumerate(marker_set):
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
                    # print("Mean error for subject {}, trial {} is {} mm".format(subject, file[:-4], np.round(marker_error_metrics['mean_all'], 4)*1000))
                    # f.write("Mean error for subject {}, trial {} is {} mm\n".format(subject, file[:-4], np.round(marker_error_metrics['mean_all'], 4)*1000))
                    count += 1
                    # rename file
                    pathFile = os.path.join(pathIK, file[:-4] + '_ik.mot')
                    pathFile2 = os.path.join(pathIK, file[:-4] + '_ik_error_larger_3cm.mot')
                    pathFileEnd = os.path.join(pathIK, file[:-4] + '_ik_error_larger_25mm.mot')
                    if not os.path.exists(pathFileEnd):
                        if os.path.exists(pathFile):
                            os.rename(pathFile, pathFileEnd)
                        else:
                            os.rename(pathFile2, pathFileEnd)
                    
            if count == len(os.listdir(pathTRC)):
                print('Only bad trials for subject {}'.format(subject))
                # f.write("Only bad trials for subject {}\n".format(subject))
                    
                test = 1
                
elif dataset == 'hamstrings_dataset':
    
    processed_subjects = ['Sub_01', 'Sub_02', 'Sub_03', 'Sub_04', 'Sub_05', 'Sub_06', 'Sub_07', 'Sub_08', 'Sub_09', 'Sub_10']
    
    marker_set_fixed = ['RSHO', 'LSHO', 'C7', 'CLAV', 'STRN', 'RELB', 'RWRA',
                        'RWRB', 'LELB', 'LWRA', 'LWRB', 'RASI', 'LASI', 'RPSI',
                        'LPSI', 'RKNE', 'RANK', 'RHEE', 'RTOE', 
                        'LKNE', 'LANK', 'LHEE', 'LTOE']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    # with open('Report_rmses_cycling.txt', 'w') as f:
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
                
                
            pathC3D = os.path.join(pathResults, 'MarkerData') 
            pathIK = os.path.join(pathResults, 'IK')
            
            count = 0
            for file in os.listdir(pathC3D):
                
                if not '.trc' in file:
                    continue
                
                # Check marker error
                filename = file[:-4] + '_ik_per_marker_error_report.csv'
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
                    pathFile2 = os.path.join(pathIK, file[:-4] + '_ik_error_larger_3cm.mot')
                    pathFileEnd = os.path.join(pathIK, file[:-4] + '_ik_error_larger_25mm.mot')
                    if not os.path.exists(pathFileEnd):
                        if os.path.exists(pathFile):
                            os.rename(pathFile, pathFileEnd)
                        else:
                            os.rename(pathFile2, pathFileEnd)
                    
            if count == len(os.listdir(pathC3D)):
                print('Only bad trials for subject {}'.format(subject))
                # f.write("Only bad trials for subject {}\n".format(subject))
                    
                test = 1
                
            
            
        
        
                
                    
                    
                
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