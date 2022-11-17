import os
import shutil
import json
# import nimblephysics as nimble
import numpy as np

path_main = os.getcwd()
path_server = os.path.dirname(path_main)
path_data = os.path.join(path_server, 'data')

# Pick dataset
dataset = 'cmu_dataset'

if dataset == 'cmu_dataset':
    
    bad_trials = {'103': ['103_07'],
                  '104': ['104_1','104_55','104_49','104_51','104_47','104_7','104_50','104_18','104_21','104_20','104_23','104_34'],
                  '01': ['01_04','01_06','01_07'],
                  '06': ['06_02'],
                  '03': ['03_02'],
                  '90': ['90_10'],
                  '89': ['89_05','89_04','89_01'],
                  '10': ['10_04'], 
                  '93': ['93_07'],
                  '79': ['79_67','79_77'],
                  '54': ['54_15'],
                  '88': ['88_02']}
    
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    # Loop over subjects
    count = 0
    count1 = 0
    print(os.listdir(path_clean_dataset))
    for subject in os.listdir(path_clean_dataset):
    # subject = '90'
        if os.path.isdir(os.path.join(path_clean_dataset, subject)):
            print("Processing subject {}".format(subject))
            
            if not subject in bad_trials:
                continue
            
            path_subject = os.path.join(path_clean_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')
            
            for trial in os.listdir(path_trials):
                
                if trial in bad_trials[subject]:
                    print('Remove trial {}'.format(trial))
                    # shutil.rmtree(os.path.join(path_trials, trial))
                    count += 1
                    
        if not os.listdir(path_trials):
            print('Remove subject {}'.format(subject))
            # shutil.rmtree(os.path.join(path_clean_dataset, subject))
            count1 += 1
            
    print('Removed {} trials'.format(count))
    print('Removed {} subjects'.format(count1))                