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
dataset = 'pitching_dataset'

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
                
elif dataset == 'multimodal_walking_dataset':
    
    # processed_subjects = ['Sub_01', 'Sub_02', 'Sub_03', 'Sub_04', 'Sub_05', 'Sub_06', 'Sub_07', 'Sub_08', 'Sub_09', 'Sub_10']
    
    marker_set_fixed = ['R_IAS', 'L_IAS', 'R_IPS', 'L_IPS', 'R_FLE', 'R_FAL', 'R_FM1',
                        'R_FM2', 'R_FM5', 'R_FCC', 'L_FLE', 'L_FAL', 'L_FM1', 'L_FM2',
                        'L_FM5', 'L_FCC', 'R_SAE', 'L_SAE', 'CV7', 
                        'TV10', 'SJN', 'SXS', 'R_HLE', 'R_HME', 'R_RSP', 'R_UHE', 'L_HLE',
                        'L_HME', 'L_RSP', 'L_UHE', ]
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    # with open('Report_rmses_cycling.txt', 'w') as f:
    subjects = []
    for subject in os.listdir(path_clean_dataset):
        
        if '20' not in subject:
            continue
        subjects.append(subject)
        
        # if subject in processed_subjects:
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
            
            os.listdir(pathIK)
            
            # Bug in csv, quick fix.
            tmp0 = pd.read_csv(pathMarkerError, header=None, nrows=1)
            tmp1 = tmp0.loc[0, :].values.tolist()            
            tmp2 = pd.read_csv(pathMarkerError, header=None, nrows=1, skiprows=1)
            tmp3 = tmp2.loc[0, :].values.tolist()            
            headers = tmp1 + tmp3            
            data = pd.read_csv(pathMarkerError, header=None, skiprows=2)            
            marker_error_all = pd.DataFrame(data=data.to_numpy(), columns=(headers))
            
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
            
elif dataset == 'parameter_estimation_dataset':
    
    # processed_subjects = ['Sub_01', 'Sub_02', 'Sub_03', 'Sub_04', 'Sub_05', 'Sub_06', 'Sub_07', 'Sub_08', 'Sub_09', 'Sub_10']
    
    marker_set_fixed = ['RASI', 'LASI', 'CLAV', 'RSHO', 'LSHO', 'RKNE', 'RANK',
                        'RTOE', 'RHEE', 'RLatFoot', 'LKNE', 'LANK', 'LTOE', 'LHEE',
                        'LLatFoot', 'RPSI', 'LPSI', 'SACR', 'C7', 
                        'T10', 'STRN', 'RELB', 'LELB', 'RWRA', 'RWRB', 'LWRA', 'LWRB']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    # with open('Report_rmses_cycling.txt', 'w') as f:
    subjects = []
    for subject in os.listdir(path_clean_dataset):
        
        if 'sub_' not in subject:
            continue
        subjects.append(subject)
        
        # if subject in processed_subjects:
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
            
            os.listdir(pathIK)
            
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
            
elif dataset == 'running_leuven1_dataset':
    
    # processed_subjects = ['Sub_01', 'Sub_02', 'Sub_03', 'Sub_04', 'Sub_05', 'Sub_06', 'Sub_07', 'Sub_08', 'Sub_09', 'Sub_10']
    
    marker_set_fixed = ['STRN', 'RSHO', 'LSHO', 'C7', 'CLAV', 'RELB', 'LELB',
                        'RASI', 'LASI', 'RKNE', 'RANK', 'RHEE', 'LKNE', 'LANK',
                        'LHEE', 'LPSI', 'RPSI', 'LMTP5', 'LMTP1', 
                        'RMTP5', 'RMTP1', 'RHAND', 'LHAND', 'RTOE', 'LTOE']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    # with open('Report_rmses_cycling.txt', 'w') as f:
    subjects = []
    for subject in os.listdir(path_clean_dataset):
        
        if 'sub_' not in subject:
            continue
        subjects.append(subject)
        
        # if subject in processed_subjects:
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
            
            os.listdir(pathIK)
            
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
                        
            # Exclude statics - bad with the few arm markers
            if 'static' in file:                
                pathFile = os.path.join(pathIK, file[:-4] + '_ik.mot')
                pathFileError = os.path.join(pathIK, file[:-4] + '_ik_error_larger_25mm.mot')
                if not os.path.exists(pathFileError):
                    pathFileEnd = os.path.join(pathIK, file[:-4] + '_ik_exclude.mot')
                    if not os.path.exists(pathFileEnd):
                        os.rename(pathFile, pathFileEnd)
                
        if count == len(os.listdir(pathC3D)):
            print('Only bad trials for subject {}'.format(subject))
            # f.write("Only bad trials for subject {}\n".format(subject))
                
            test = 1
                
elif dataset == 'running_leuven2_dataset':
    
    # processed_subjects = ['Sub_01', 'Sub_02', 'Sub_03', 'Sub_04', 'Sub_05', 'Sub_06', 'Sub_07', 'Sub_08', 'Sub_09', 'Sub_10']
    
    marker_set_fixed = ['STRN', 'RSHO', 'LSHO', 'C7', 'T10', 'CLAV', 'RELB', 'LELB', 'RWRA', 'RWRB', 'LWRB', 'LWRA',
                        'RASI', 'LASI', 'RKNE', 'RANK', 'RHEE', 'LKNE', 'LANK',
                        'LHEE', 'LPSI', 'RPSI', 'LMTP5', 'LMTP1', 
                        'RMTP5', 'RMTP1', 'RELBM', 'LELBM']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    # with open('Report_rmses_cycling.txt', 'w') as f:
    subjects = []
    for subject in os.listdir(path_clean_dataset):
        
        if 'sub_' not in subject:
            continue
        subjects.append(subject)
        
        # if subject in processed_subjects:
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
            
            os.listdir(pathIK)
            
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
                        
            # # Exclude statics - bad with the few arm markers
            # if 'static' in file:                
            #     pathFile = os.path.join(pathIK, file[:-4] + '_ik.mot')
            #     pathFileError = os.path.join(pathIK, file[:-4] + '_ik_error_larger_25mm.mot')
            #     if not os.path.exists(pathFileError):
            #         pathFileEnd = os.path.join(pathIK, file[:-4] + '_ik_exclude.mot')
            #         if not os.path.exists(pathFileEnd):
            #             os.rename(pathFile, pathFileEnd)
                
        if count == len(os.listdir(pathC3D)):
            print('Only bad trials for subject {}'.format(subject))
            # f.write("Only bad trials for subject {}\n".format(subject))
                
            test = 1
            
elif dataset == 'inclined_walking_dataset':
    
    # processed_subjects = ['Sub_01', 'Sub_02', 'Sub_03', 'Sub_04', 'Sub_05', 'Sub_06', 'Sub_07', 'Sub_08', 'Sub_09', 'Sub_10']
    
    marker_set_fixed = ['RACR', 'LACR', 'T10', 'XYPH', 'RASIS', 'LASIS', 'RPSIS', 'LPSIS', 'RLEK', 'RLM', 'RHEE', 'RTOE', 'RMT5',
                        'LLEK', 'LLM', 'LHEE', 'LTOE', 'LMT5']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    # with open('Report_rmses_cycling.txt', 'w') as f:
    subjects = []
    for subject in os.listdir(path_clean_dataset):
        
        if 'sub' not in subject:
            continue
        
        if 'subject_09' in subject or 'subject_12' in subject:
            continue
        
        subjects.append(subject)
        
        
        
        # if subject in processed_subjects:
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
            
            os.listdir(pathIK)
            
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
                        
            # # Exclude statics - bad with the few arm markers
            # if 'static' in file:                
            #     pathFile = os.path.join(pathIK, file[:-4] + '_ik.mot')
            #     pathFileError = os.path.join(pathIK, file[:-4] + '_ik_error_larger_25mm.mot')
            #     if not os.path.exists(pathFileError):
            #         pathFileEnd = os.path.join(pathIK, file[:-4] + '_ik_exclude.mot')
            #         if not os.path.exists(pathFileEnd):
            #             os.rename(pathFile, pathFileEnd)
                
        if count == len(os.listdir(pathC3D)):
            print('Only bad trials for subject {}'.format(subject))
            # f.write("Only bad trials for subject {}\n".format(subject))
                
            test = 1
            
elif dataset == 'toeheel_walking_dataset':
    
    # processed_subjects = ['Sub_01', 'Sub_02', 'Sub_03', 'Sub_04', 'Sub_05', 'Sub_06', 'Sub_07', 'Sub_08', 'Sub_09', 'Sub_10']
    
    marker_set_fixed = ['R_Asis', 'L_Asis', 'Psis', 'R_LatCon', 'R_LatMal', 'R_Toe1', 'R_Meta5', 'R_Heel', 'L_LatCon', 'L_LatMal', 'L_Toe1', 'L_Heel', 'L_Meta5',
                        'R_Should', 'L_Should', 'C7', 'R_Elbow', 'R_Wrist', 'L_Elbow', 'l_Wrist']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    # with open('Report_rmses_cycling.txt', 'w') as f:
    subjects = []
    demos = np.zeros((50,2))
    
    count_s = 0
    for subject in os.listdir(path_clean_dataset):
        
        if 'Subject' not in subject or '.mat' in subject:
            continue
        
        subjects.append(subject)        
        
        # if subject in processed_subjects:
            # print("Processing subject {}".format(subject))
            
        pathSubject = os.path.join(path_clean_dataset, subject)            
        pathResults = os.path.join(pathSubject, 'osim_results')
        if not os.path.exists(os.path.join(pathResults, 'Models', 'optimized_scale_and_markers.osim')):
            os.chdir(pathResults)
            cmd = 'opensim-cmd run-tool Models/rescaling_setup.xml'
            os.system(cmd)
            os.chdir(path_main)
            
        pathDemo = os.path.join(pathResults, '_subject.json')
        tmp = open(pathDemo)
        demo = json.load(tmp)
        demos[count_s, 0] = demo['massKg']
        demos[count_s, 1] = demo['heightM']
            
            
        pathC3D = os.path.join(pathResults, 'MarkerData') 
        pathIK = os.path.join(pathResults, 'IK')
        
        count = 0
        for file in os.listdir(pathC3D):
            
            if not '.trc' in file:
                continue
            
            # Check marker error
            filename = file[:-4] + '_ik_per_marker_error_report.csv'
            pathMarkerError = os.path.join(pathIK, filename)
            
            os.listdir(pathIK)
            
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
                        
            # # Exclude statics - bad with the few arm markers
            # if 'static' in file:                
            #     pathFile = os.path.join(pathIK, file[:-4] + '_ik.mot')
            #     pathFileError = os.path.join(pathIK, file[:-4] + '_ik_error_larger_25mm.mot')
            #     if not os.path.exists(pathFileError):
            #         pathFileEnd = os.path.join(pathIK, file[:-4] + '_ik_exclude.mot')
            #         if not os.path.exists(pathFileEnd):
            #             os.rename(pathFile, pathFileEnd)
                
        if count == len(os.listdir(pathC3D)):
            print('Only bad trials for subject {}'.format(subject))
            # f.write("Only bad trials for subject {}\n".format(subject))
                
            test = 1
            
        count_s +=1
        
elif dataset == 'pitching_dataset':
       
    marker_set_fixed = ['RASI', 'LASI', 'RPSI', 'LPSI', 'RFLE', 'RFME', 'RFAL', 'RTAM', 
                   'RFM2', 'RFM5', 'RHEL', 'LFLE', 'LFME', 'LFAL', 'LTAM', 'LFM2', 
                   'LHEL', 'LFM5', 'RSHO', 'LSHO', 'C7', 'RUP1', 'RUP2', 'RUP3', 
                   'RUP4', 'RELL', 'RELM', 'RFR1', 'RFR2', 'RFR3', 'RFR4', 'RWRL', 
                   'RWRM', 'LUP1', 'LUP2', 'LUP3', 'LUP4', 'LELL', 'LELM', 'LFR1',
                   'LFR2', 'LFR3', 'LFR4', 'LWRL', 'LWRM', 'RGT', 'RTHI1', 'RTHI2',
                   'RTHI3', 'RTHI4', 'LGT', 'LTHI1', 'LTHI2', 'LTHI3', 'LTHI4', 'RSK1',
                   'RSK2', 'RSK3', 'RSK4', 'LSK1', 'LSK2', 'LSK3', 'LSK4', 'RILC', 'LILC']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    subjects = ['S' + str(i) for i in range(1,2)]
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    # with open('Report_rmses_cycling.txt', 'w') as f:
    # subjects = []
    for subject in subjects:
        
        if subject not in subjects:
            continue
        
        # subjects.append(subject)        
        
        # if subject in processed_subjects:
            # print("Processing subject {}".format(subject))
            
        pathSubject = os.path.join(path_clean_dataset, subject)

        for session in os.listdir(pathSubject):            
            if not 'w' in session:
                continue
            
            pathSession = os.path.join(pathSubject, session) 


           
            pathResults = os.path.join(pathSession, 'osim_results')
            if os.path.exists(pathResults):
                print(pathResults)
                # shutil.rmtree(pathResults)
            
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
                
                os.listdir(pathIK)
                
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
                            
                # # Exclude statics - bad with the few arm markers
                # if 'static' in file:                
                #     pathFile = os.path.join(pathIK, file[:-4] + '_ik.mot')
                #     pathFileError = os.path.join(pathIK, file[:-4] + '_ik_error_larger_25mm.mot')
                #     if not os.path.exists(pathFileError):
                #         pathFileEnd = os.path.join(pathIK, file[:-4] + '_ik_exclude.mot')
                #         if not os.path.exists(pathFileEnd):
                #             os.rename(pathFile, pathFileEnd)
                    
            if count == len(os.listdir(pathC3D)):
                print('Only bad trials for subject {}'.format(subject))
                # f.write("Only bad trials for subject {}\n".format(subject))
                    
                test = 1
                
elif dataset == 'karate_dataset':
       
    marker_set_fixed = ['LFHD', 'RFHD', 'LBHD', 'RBHD', 'C7', 'T10', 'CLAV', 'STRN', 
                   'RBAK', 'LSHO', 'LUPA', 'LELB', 'LFRM', 'LWRA', 'LWRB', 
                   'LFIN', 'RSHO', 'RUPA', 'RELB', 'RFRM', 'RWRA', 'RWRB', 
                   'RFIN', 'LASI', 'RASI', 'LPSI', 'RPSI', 'LTHI', 'LKNE', 
                   'LTIB', 'LANK', 'LHEE', 'LTOE', 'RTHI', 'RKNE', 'RTIB', 
                   'RANK', 'RHEE', 'RTOE']
    
    subjects1 = ['B03' + str(i) for i in range(69,90)]
    subjects2 = ['B03' + str(i) for i in range(91,97)]
    subjects3 = ['B03' + str(i) for i in range(98,100)]
    subjects4 = ['B040' + str(i) for i in range(0,6)]    
    subjects = subjects1 + subjects2 + subjects3 + subjects4
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    # with open('Report_rmses_cycling.txt', 'w') as f:
    # subjects = []
    for subject in subjects:
        
        # subjects.append(subject)        
        
        # if subject in processed_subjects:
            # print("Processing subject {}".format(subject))
            
        pathSubject = os.path.join(path_clean_dataset, subject)

        for session in os.listdir(pathSubject):            
            if not 'B0' in session:
                continue
            
            pathSession = os.path.join(pathSubject, session) 


           
            pathResults = os.path.join(pathSession, 'osim_results')
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
                
                os.listdir(pathIK)
                
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
                            
                # # Exclude statics - bad with the few arm markers
                # if 'static' in file:                
                #     pathFile = os.path.join(pathIK, file[:-4] + '_ik.mot')
                #     pathFileError = os.path.join(pathIK, file[:-4] + '_ik_error_larger_25mm.mot')
                #     if not os.path.exists(pathFileError):
                #         pathFileEnd = os.path.join(pathIK, file[:-4] + '_ik_exclude.mot')
                #         if not os.path.exists(pathFileEnd):
                #             os.rename(pathFile, pathFileEnd)
                    
            if count == len(os.listdir(pathC3D)):
                print('Only bad trials for subject {}'.format(subject))
                # f.write("Only bad trials for subject {}\n".format(subject))
                    
                test = 1
                          