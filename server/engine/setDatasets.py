import os
import shutil
import json
import pandas as pd
import numpy as np

path_main = os.getcwd()
path_server = os.path.dirname(path_main)
path_data = os.path.join(path_server, 'data')

# Generic data
subject_data = {'massKg': 68,
                'heightM': 1.6,
                'sex': 'unknowm',
                'skeletonPreset': 'custom'}

# Pick dataset
dataset = 'karate_dataset'

def strip(y):
    return y.replace(" ", "")

if dataset == 'cmu_dataset':
    
    subjects_to_process = ['150']
    
    path_my_datasets = '/home/clarkadmin/Documents/myDatasets_Antoine'
    path_original_dataset = os.path.join(path_my_datasets, dataset)
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if not subject in subjects_to_process:
                continue
            
            print('Processing subject {}'.format(subject))
            
            # Create new subject folder
            path_subject = os.path.join(path_clean_dataset, subject)
            os.makedirs(path_subject, exist_ok=True)
    
            # Copy generic model
            path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
            path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
            shutil.copy2(path_generic_model, path_generic_model_end)
            
            # Dump generic demographics
            outfile = os.path.join(path_subject, '_subject.json')
            with open(outfile, "w") as outfile:
                json.dump(subject_data, outfile)
                
            # Re-organize marker data            
            os.makedirs(path_subject, exist_ok=True)
            path_original_subject = os.path.join(path_original_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')
            os.makedirs(path_trials, exist_ok=True)
            for file in os.listdir(path_original_subject):
                if not '.c3d' in file:
                    continue
                
                path_trial = os.path.join(path_trials, file[:-4])
                os.makedirs(path_trial, exist_ok=True)
                
                path_generic_c3d = os.path.join(path_original_subject, file)
                path_generic_c3d_end = os.path.join(path_trial, 'markers.c3d')
                shutil.copy2(path_generic_c3d, path_generic_c3d_end)
                
elif dataset == 'cycling_dataset':
    
    infoSubjects = {'P003': {'massKg': 76.5,
                             'heightM': 1.78,
                             'sex': 'female',
                             'model': 'normal'},
                    'P004': {'massKg': 102.3,
                             'heightM': 1.83,
                             'sex': 'male',
                             'model': 'noUl'},
                    'P005': {'massKg': 60.6,
                             'heightM': 1.62,
                             'sex': 'female',
                             'model': 'normal'},
                    'P006': {'massKg': 92.3,
                             'heightM': 1.82,
                             'sex': 'male',
                             'model': 'noRad'},
                    'P007': {'massKg': 68.1,
                             'heightM': 1.72,
                             'sex': 'female',
                             'model': 'normal'},
                    'P008': {'massKg': 66,
                             'heightM': 1.57,
                             'sex': 'female',
                             'model': 'noRad'},
                    'P009': {'massKg': 75.7,
                             'heightM': 1.79,
                             'sex': 'male',
                             'model': 'exclude'},
                    'P010': {'massKg': 74.2,
                             'heightM': 1.71,
                             'sex': 'male',
                             'model': 'exclude'},
                    'P011': {'massKg': 64.2,
                             'heightM': 1.68,
                             'sex': 'male',
                             'model': 'normal'},
                    'P012': {'massKg': 61.1,
                             'heightM': 1.66,
                             'sex': 'female',
                             'model': 'noUl'},
                    'P013': {'massKg': 64.1,
                             'heightM': 1.58,
                             'sex': 'female',
                             'model': 'noRad'},
                    'P014': {'massKg': 66,
                             'heightM': 1.69,
                             'sex': 'female',
                             'model': 'noRad'},
                    'P015': {'massKg': 90.8,
                             'heightM': 1.95,
                             'sex': 'male',
                             'model': 'noUl'},
                    'P016':  {'massKg': 92.1,
                             'heightM': 1.78,
                             'sex': 'female',
                             'model': 'noRad'},
                    'P018': {'massKg': 79.4,
                             'heightM': 1.88,
                             'sex': 'male',
                             'model': 'normal'},
                    'P019': {'massKg': 86,
                             'heightM': 1.87,
                             'sex': 'male',
                             'model': 'noUl'},
                    'P020': {'massKg': 68.8,
                             'heightM': 1.65,
                             'sex': 'male',
                             'model': 'normal'},
                    'P021': {'massKg': 66.5,
                             'heightM': 1.73,
                             'sex': 'male',
                             'model': 'normal'},
                    'P022': {'massKg': 59.7,
                             'heightM': 1.66,
                             'sex': 'female',
                             'model': 'noUl'},
                    'P023': {'massKg': 76.1,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    'P025': {'massKg': 75.6,
                             'heightM': 1.71,
                             'sex': 'male',
                             'model': 'noUl'},
                    'P026': {'massKg': 61.1,
                             'heightM': 1.64,
                             'sex': 'female',
                             'model': 'noRad'},
                    'P027': {'massKg': 70.5,
                             'heightM': 1.72,
                             'sex': 'male',
                             'model': 'exclude'},
                    'P028': {'massKg': 81.9,
                             'heightM': 1.81,
                             'sex': 'male',
                             'model': 'noRad'},
                    'P029': {'massKg': 89.3,
                             'heightM': 1.84,
                             'sex': 'male',
                             'model': 'normal'},
                    'P031': {'massKg': 54.2,
                             'heightM': 1.63,
                             'sex': 'female',
                             'model': 'normal'},
                    'P032':  {'massKg': 91.5,
                             'heightM': 1.84,
                             'sex': 'male',
                             'model': 'noUl'},
                    'P033': {'massKg': 66.1,
                             'heightM': 1.67,
                             'sex': 'female',
                             'model': 'noRad'},
                    'P034': {'massKg': 65.8,
                             'heightM': 1.73,
                             'sex': 'female',
                             'model': 'noRad'},
                    'P036': {'massKg': 56.7,
                             'heightM': 1.60,
                             'sex': 'female',
                             'model': 'noUl'},
                    'P038': {'massKg': 79.9,
                             'heightM': 1.88,
                             'sex': 'male',
                             'model': 'noUl'},
                    'P039': {'massKg': 63.2,
                             'heightM': 1.76,
                             'sex': 'male',
                             'model': 'noRad'},
                    'P040': {'massKg': 78,
                             'heightM': 1.57,
                             'sex': 'female',
                             'model': 'normal'},
                    'P041': {'massKg': 57.1,
                             'heightM': 1.69,
                             'sex': 'female',
                             'model': 'normal'},
                    'P042': {'massKg': 90.8,
                             'heightM': 1.84,
                             'sex': 'male',
                             'model': 'noUl'},
                    'P043': {'massKg': 74.5,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    'P045': {'massKg': 91.3,
                             'heightM': 1.81,
                             'sex': 'male',
                             'model': 'noRad'},
                    'P050': {'massKg': 81.9,
                             'heightM': 1.81,
                             'sex': 'male',
                             'model': 'noRad'},
                    'P051': {'massKg': 79.9,
                             'heightM': 1.88,
                             'sex': 'male',
                             'model': 'noUl'}}
    
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/cycling_anthony_cleaned'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if infoSubjects[subject]['model'] == 'exclude':
                print('Exclude subject {}'.format(subject))
                continue
            
            # Create new subject folder
            path_subject = os.path.join(path_clean_dataset, subject)
            os.makedirs(path_subject, exist_ok=True)
    
            # Copy generic model
            if infoSubjects[subject]['model'] == 'normal':
                path_generic_model = os.path.join(path_original_dataset, 'Model_markers.osim')
            elif infoSubjects[subject]['model'] == 'noUl':
                path_generic_model = os.path.join(path_original_dataset, 'Model_markers_noUl.osim')
            elif infoSubjects[subject]['model'] == 'noRad':
                path_generic_model = os.path.join(path_original_dataset, 'Model_markers_noRad.osim')
            else:
                raise ValueError("not existing")
            path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
            shutil.copy2(path_generic_model, path_generic_model_end)
            
            # Dump generic demographics
            outfile = os.path.join(path_subject, '_subject.json')
            subject_data = {'massKg': infoSubjects[subject]['massKg'],
                            'heightM': infoSubjects[subject]['heightM'],
                            'sex': infoSubjects[subject]['sex'],
                            'skeletonPreset': 'custom'}
            with open(outfile, "w") as outfile:
                json.dump(subject_data, outfile)
                
            # Re-organize marker data            
            path_original_subject = os.path.join(path_original_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')
            path_trial = os.path.join(path_trials, 'trial')
            os.makedirs(path_trial, exist_ok=True)
            
            path_generic_trc = os.path.join(path_original_subject, 'marker_data_cut_adjusted.trc')
            path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
            shutil.copy2(path_generic_trc, path_generic_trc_end)
            
elif dataset == 'balance_dataset':
    
    infoSubjects = {'Subj03': {'massKg': 79.1,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    'Subj04': {'massKg': 63.1,
                             'heightM': 1.78,
                             'sex': 'male',
                             'model': 'normal'},
                    'Subj05': {'massKg': 70.6,
                             'heightM': 1.79,
                             'sex': 'male',
                             'model': 'normal'},
                    'Subj06': {'massKg': 58.2,
                             'heightM': 1.65,
                             'sex': 'male',
                             'model': 'normal'},
                    'Subj07': {'massKg': 68.8,
                             'heightM': 1.75,
                             'sex': 'male',
                             'model': 'normal'},
                    'Subj08': {'massKg': 60.3,
                             'heightM': 1.63,
                             'sex': 'male',
                             'model': 'normal'}}
    
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/balance_dataset_cleaned'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if infoSubjects[subject]['model'] == 'exclude':
                print('Exclude subject {}'.format(subject))
                continue
            
            # Create new subject folder
            path_subject = os.path.join(path_clean_dataset, subject)
            os.makedirs(path_subject, exist_ok=True)
    
            # Copy generic model
            if infoSubjects[subject]['model'] == 'normal':
                path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
            else:
                raise ValueError("not existing")
            path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
            shutil.copy2(path_generic_model, path_generic_model_end)
            
            # Dump generic demographics
            outfile = os.path.join(path_subject, '_subject.json')
            subject_data = {'massKg': infoSubjects[subject]['massKg'],
                            'heightM': infoSubjects[subject]['heightM'],
                            'sex': infoSubjects[subject]['sex'],
                            'skeletonPreset': 'custom'}
            with open(outfile, "w") as outfile:
                json.dump(subject_data, outfile)
                
            # Re-organize marker data            
            path_original_subject = os.path.join(path_original_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')
            
            
            os.makedirs(path_trials, exist_ok=True)
            for file in os.listdir(path_original_subject):
                if not '.trc' in file:
                    continue
                
                path_trial = os.path.join(path_trials, file[:-4])
                os.makedirs(path_trial, exist_ok=True)
                
                path_generic_trc = os.path.join(path_original_subject, file)
                path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                shutil.copy2(path_generic_trc, path_generic_trc_end)
            
elif dataset == 'myer_dataset':
    
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/myer_dataset_cleaned'
    
    # path_original_dataset = 'C:/MyDriveSym/Projects/openpose-augmenter/Data_opensim/myer_dataset'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    pathDemographics = os.path.join(path_original_dataset, 'demographics.xlsx')
    
    demographics = pd.read_excel(pathDemographics, engine='openpyxl')

    folders = ['PreTesting_2017_fall_VR', 'PreTesting_2017_summer_VR', 
               'PreTesting_2018_summer_VR', 'PreTesting_2019_fall_VR', 
               'PreTesting_2019_summer_VR']
    
    for folder in folders:
        pathFolder = os.path.join(path_original_dataset, folder)
        
        for subject in os.listdir(pathFolder):
            if os.path.isdir(os.path.join(pathFolder, subject)):
                
                pathSubject = os.path.join(pathFolder, subject)                
                
                # Get mass and height
                ID = subject.split("_")[0].lower()                
                massKg = demographics.loc[demographics['ID'].str.lower() == ID.lower()]['Weight'].to_numpy()[0]
                heightM = demographics.loc[demographics['ID'].str.lower() == ID.lower()]['Height'].to_numpy()[0]/100
                
                infoSubject = {'massKg': massKg,
                               'heightM': heightM}
                
                # Create new subject folder
                # subject_clean = ID
                path_subject = os.path.join(path_clean_dataset, folder, subject)
                os.makedirs(path_subject, exist_ok=True)
        
                # Copy generic model
                if "_VR" in folder:
                    modelName = 'model_markers.osim'
                else:
                    modelName = 'model_markers_noArms.osim'

                path_generic_model = os.path.join(path_original_dataset, modelName)
                path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
                shutil.copy2(path_generic_model, path_generic_model_end)
                
                # Dump demographics
                outfile = os.path.join(path_subject, '_subject.json')
                subject_data = {'massKg': infoSubject['massKg'],
                                'heightM': infoSubject['heightM'],
                                'sex': 'unknowm',
                                'skeletonPreset': 'custom'}
                with open(outfile, "w") as outfile:
                    json.dump(subject_data, outfile)
                    
                # Re-organize marker data            
                path_original_subject = os.path.join(pathFolder, subject)
                path_trials = os.path.join(path_subject, 'trials')
                
                
                os.makedirs(path_trials, exist_ok=True)
                for file in os.listdir(path_original_subject):
                    if not '.trc' in file:
                        continue
                    
                    path_trial = os.path.join(path_trials, file[:-12])
                    os.makedirs(path_trial, exist_ok=True)
                    
                    path_generic_trc = os.path.join(path_original_subject, file)
                    path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                    shutil.copy2(path_generic_trc, path_generic_trc_end)
                    
elif dataset == 'hamstrings_dataset':
    
    infoSubjects = {'Sub_01': {'massKg': 64.1,
                             'heightM': 1.70,
                             'sex': 'male',
                             'model': 'normal'},
                    'Sub_02': {'massKg': 65.5,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    'Sub_03': {'massKg': 82.0,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    'Sub_04': {'massKg': 69.5,
                             'heightM': 1.70,
                             'sex': 'male',
                             'model': 'normal'},
                    'Sub_05': {'massKg': 70.0,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    'Sub_06': {'massKg': 69.0,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    'Sub_07': {'massKg': 74.0,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    'Sub_08': {'massKg': 84.5,
                             'heightM': 1.90,
                             'sex': 'male',
                             'model': 'normal'},
                    'Sub_09': {'massKg': 70.0,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    'Sub_10': {'massKg': 95.5,
                             'heightM': 2.00,
                             'sex': 'male',
                             'model': 'normal'}}
    
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/hamstrings_dataset'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if infoSubjects[subject]['model'] == 'exclude':
                print('Exclude subject {}'.format(subject))
                continue
            
            # Create new subject folder
            path_subject = os.path.join(path_clean_dataset, subject)
            os.makedirs(path_subject, exist_ok=True)
    
            # Copy generic model
            if infoSubjects[subject]['model'] == 'normal':
                path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
            else:
                raise ValueError("not existing")
            path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
            shutil.copy2(path_generic_model, path_generic_model_end)
            
            # Dump generic demographics
            outfile = os.path.join(path_subject, '_subject.json')
            subject_data = {'massKg': infoSubjects[subject]['massKg'],
                            'heightM': infoSubjects[subject]['heightM'],
                            'sex': infoSubjects[subject]['sex'],
                            'skeletonPreset': 'custom'}
            with open(outfile, "w") as outfile:
                json.dump(subject_data, outfile)
                
            # Re-organize marker data            
            path_original_subject = os.path.join(path_original_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')
            
            
            os.makedirs(path_trials, exist_ok=True)
            for file in os.listdir(path_original_subject):
                if not '.trc' in file:
                    continue
                
                path_trial = os.path.join(path_trials, file[:-4])
                os.makedirs(path_trial, exist_ok=True)
                
                path_generic_trc = os.path.join(path_original_subject, file)
                path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                shutil.copy2(path_generic_trc, path_generic_trc_end)
                
elif dataset == 'multimodal_walking_dataset':
    
    infoSubjects = {'2014001': {'massKg': 67.0,
                             'heightM': 1.66,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014002': {'massKg': 65.4,
                             'heightM': 1.64,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014003': {'massKg': 50.0,
                             'heightM': 1.56,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014004': {'massKg': 72.5,
                             'heightM': 1.77,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014005': {'massKg': 73.5,
                             'heightM': 1.83,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014006': {'massKg': 73.0,
                             'heightM': 1.76,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014007': {'massKg': 65.0,
                             'heightM': 1.69,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014008': {'massKg': 57.1,
                             'heightM': 1.66,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014009': {'massKg': 86.0,
                             'heightM': 1.88,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014011': {'massKg': 63.4,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014013': {'massKg': 61.3,
                             'heightM': 1.70,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014014': {'massKg': 92.0,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014015': {'massKg': 67.0,
                             'heightM': 1.58,
                             'sex': 'female',
                             'model': 'normal'},
                    # Data is in 2014016 folder, demo is 2015016. I assume they match
                    '2014016': {'massKg': 76.0, # here
                             'heightM': 1.69,
                             'sex': 'female',
                             'model': 'normal'},                    
                    '2014019': {'massKg': 73.8,
                             'heightM': 1.76,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014022': {'massKg': 59.8,
                             'heightM': 1.71,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014024': {'massKg': 87.5,
                             'heightM': 1.92,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014025': {'massKg': 80.5,
                             'heightM': 1.66,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014029': {'massKg': 89.9,
                             'heightM': 1.89,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014030': {'massKg': 60.7,
                             'heightM': 1.70,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014031': {'massKg': 67.2,
                             'heightM': 1.77,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014033': {'massKg': 63.5,
                             'heightM': 1.60,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014034': {'massKg': 89.6,
                             'heightM': 1.84,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014040': {'massKg': 56.5,
                             'heightM': 1.55,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014046': {'massKg': 61.8,
                             'heightM': 1.65,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014048': {'massKg': 61.5,
                             'heightM': 1.64,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014049': {'massKg': 72.2,
                             'heightM': 1.74,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014050': {'massKg': 61.9,
                             'heightM': 1.64,
                             'sex': 'female',
                             'model': 'normal'},
                    '2014051': {'massKg': 88.0,
                             'heightM': 1.91,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014052': {'massKg': 79.5,
                             'heightM': 1.82,
                             'sex': 'male',
                             'model': 'normal'},
                    '2014053': {'massKg': 62.8,
                             'heightM': 1.72,
                             'sex': 'female',
                             'model': 'normal'},
                    '2015002': {'massKg': 74.0,
                             'heightM': 1.74,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015003': {'massKg': 87.2,
                             'heightM': 1.77,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015004': {'massKg': 62.0,
                             'heightM': 1.70,
                             'sex': 'female',
                             'model': 'normal'},
                    '2015005': {'massKg': 89.4,
                             'heightM': 1.90,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015007': {'massKg': 60.2,
                             'heightM': 1.66,
                             'sex': 'female',
                             'model': 'normal'},                    
                    '2015013': {'massKg': 73.0,
                             'heightM': 1.69,
                             'sex': 'female',
                             'model': 'normal'},
                    '2015015': {'massKg': 68.0,
                             'heightM': 1.73,
                             'sex': 'female',
                             'model': 'normal'},
                    '2015017': {'massKg': 60.5,
                             'heightM': 1.67,
                             'sex': 'female',
                             'model': 'normal'},
                    '2015020': {'massKg': 95.0,
                             'heightM': 1.79,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015021': {'massKg': 58.0,
                             'heightM': 1.69,
                             'sex': 'female',
                             'model': 'normal'},
                    '2015026': {'massKg': 51.5,
                             'heightM': 1.71,
                             'sex': 'female',
                             'model': 'normal'},
                    '2015027': {'massKg': 65.5,
                             'heightM': 1.72,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015030': {'massKg': 86.0,
                             'heightM': 1.87,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015032': {'massKg': 50.8,
                             'heightM': 1.72,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015035': {'massKg': 81.5,
                             'heightM': 1.77,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015037': {'massKg': 66.1,
                             'heightM': 1.76,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015041': {'massKg': 74.8,
                             'heightM': 1.88,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015042': {'massKg': 98.0,
                             'heightM': 1.83,
                             'sex': 'male',
                             'model': 'normal'},
                    '2015043': {'massKg': 74.0,
                             'heightM': 1.78,
                             'sex': 'male',
                             'model': 'normal'}}
    
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/multimodal_walking_dataset'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if infoSubjects[subject]['model'] == 'exclude':
                print('Exclude subject {}'.format(subject))
                continue
            
            # Create new subject folder
            path_subject = os.path.join(path_clean_dataset, subject)
            os.makedirs(path_subject, exist_ok=True)
    
            # Copy generic model
            if infoSubjects[subject]['model'] == 'normal':
                path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
            else:
                raise ValueError("not existing")
            path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
            shutil.copy2(path_generic_model, path_generic_model_end)
            
            # Dump generic demographics
            outfile = os.path.join(path_subject, '_subject.json')
            subject_data = {'massKg': infoSubjects[subject]['massKg'],
                            'heightM': infoSubjects[subject]['heightM'],
                            'sex': infoSubjects[subject]['sex'],
                            'skeletonPreset': 'custom'}
            with open(outfile, "w") as outfile:
                json.dump(subject_data, outfile)
                
            # Re-organize marker data            
            path_original_subject = os.path.join(path_original_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')
            
            
            os.makedirs(path_trials, exist_ok=True)
            for file in os.listdir(path_original_subject):
                if not '.trc' in file:
                    continue
                
                path_trial = os.path.join(path_trials, file[:-4])
                os.makedirs(path_trial, exist_ok=True)
                
                path_generic_trc = os.path.join(path_original_subject, file)
                path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                shutil.copy2(path_generic_trc, path_generic_trc_end)
                
elif dataset == 'parameter_estimation_dataset':
    
    infoSubjects = {'sub_00': {'massKg': 64.8,
                             'heightM': 1.76,
                             'sex': 'male',
                             'model': 'normal'},
                    'sub_01': {'massKg': 65.5,
                             'heightM': 1.78,
                             'sex': 'male',
                             'model': 'normal'},
                    'sub_02': {'massKg': 71.7,
                             'heightM': 1.73,
                             'sex': 'female',
                             'model': 'normal'},
                    'sub_03': {'massKg': 70.8,
                             'heightM': 1.80,
                             'sex': 'male',
                             'model': 'normal'},
                    'sub_04': {'massKg': 64.2,
                             'heightM': 1.69,
                             'sex': 'female',
                             'model': 'normal'},
                    'sub_05': {'massKg': 60.1,
                             'heightM': 1.70,
                             'sex': 'female',
                             'model': 'normal'},
                    'sub_06': {'massKg': 73.6,
                             'heightM': 1.75,
                             'sex': 'male',
                             'model': 'normal'},
                    'sub_07': {'massKg': 66.3,
                             'heightM': 1.78,
                             'sex': 'male',
                             'model': 'normal'},
                    'sub_08': {'massKg':81.0,
                             'heightM': 1.77,
                             'sex': 'male',
                             'model': 'normal'},
                    'sub_09': {'massKg': 78.4,
                             'heightM': 1.90,
                             'sex': 'male',
                             'model': 'normal'},
                    'sub_10': {'massKg': 73.4,
                             'heightM': 1.75,
                             'sex': 'female',
                             'model': 'normal'}}
    
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/parameter_estimation_dataset'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if infoSubjects[subject]['model'] == 'exclude':
                print('Exclude subject {}'.format(subject))
                continue
            
            # Create new subject folder
            path_subject = os.path.join(path_clean_dataset, subject)
            os.makedirs(path_subject, exist_ok=True)
    
            # Copy generic model
            if infoSubjects[subject]['model'] == 'normal':
                path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
            else:
                raise ValueError("not existing")
            path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
            shutil.copy2(path_generic_model, path_generic_model_end)
            
            # Dump generic demographics
            outfile = os.path.join(path_subject, '_subject.json')
            subject_data = {'massKg': infoSubjects[subject]['massKg'],
                            'heightM': infoSubjects[subject]['heightM'],
                            'sex': infoSubjects[subject]['sex'],
                            'skeletonPreset': 'custom'}
            with open(outfile, "w") as outfile:
                json.dump(subject_data, outfile)
                
            # Re-organize marker data            
            path_original_subject = os.path.join(path_original_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')
            
            
            os.makedirs(path_trials, exist_ok=True)
            for file in os.listdir(path_original_subject):
                if not '.trc' in file:
                    continue
                
                path_trial = os.path.join(path_trials, file[:-4])
                os.makedirs(path_trial, exist_ok=True)
                
                path_generic_trc = os.path.join(path_original_subject, file)
                path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                shutil.copy2(path_generic_trc, path_generic_trc_end)
                
elif dataset == 'running_leuven1_dataset':
    
    infoSubjects = {'sub_00': {'massKg': 59.3,
                             'heightM': 1.68,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_01': {'massKg': 74.9,
                             'heightM': 1.89,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_02': {'massKg': 65.3,
                             'heightM': 1.74,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_03': {'massKg': 67.8,
                             'heightM': 1.77,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_04': {'massKg': 66.8,
                             'heightM': 1.82,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_05': {'massKg': 66.7,
                             'heightM': 1.78,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_06': {'massKg': 66.5,
                             'heightM': 1.79,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_07': {'massKg': 89.7,
                             'heightM': 1.96,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_08': {'massKg': 77.3,
                             'heightM': 1.88,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_09': {'massKg': 71.6,
                             'heightM': 1.91,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_10': {'massKg': 59.0,
                             'heightM': 1.70,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_11': {'massKg': 70.9,
                             'heightM': 1.81,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_12': {'massKg': 74.4,
                             'heightM': 1.82,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_13': {'massKg': 57.1,
                             'heightM': 1.61,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_14': {'massKg': 68.5,
                             'heightM': 1.80,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_15': {'massKg': 71.8,
                             'heightM': 1.77,
                             'sex': 'unknown',
                             'model': 'normal'}}
    
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/running_leuven1_dataset'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if infoSubjects[subject]['model'] == 'exclude':
                print('Exclude subject {}'.format(subject))
                continue
            
            # Create new subject folder
            path_subject = os.path.join(path_clean_dataset, subject)
            os.makedirs(path_subject, exist_ok=True)
    
            # Copy generic model
            if infoSubjects[subject]['model'] == 'normal':
                path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
            else:
                raise ValueError("not existing")
            path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
            shutil.copy2(path_generic_model, path_generic_model_end)
            
            # Dump generic demographics
            outfile = os.path.join(path_subject, '_subject.json')
            subject_data = {'massKg': infoSubjects[subject]['massKg'],
                            'heightM': infoSubjects[subject]['heightM'],
                            'sex': infoSubjects[subject]['sex'],
                            'skeletonPreset': 'custom'}
            with open(outfile, "w") as outfile:
                json.dump(subject_data, outfile)
                
            # Re-organize marker data            
            path_original_subject = os.path.join(path_original_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')
            
            
            os.makedirs(path_trials, exist_ok=True)
            for file in os.listdir(path_original_subject):
                if not '.trc' in file:
                    continue
                
                path_trial = os.path.join(path_trials, file[:-4])
                os.makedirs(path_trial, exist_ok=True)
                
                path_generic_trc = os.path.join(path_original_subject, file)
                path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                shutil.copy2(path_generic_trc, path_generic_trc_end)
                
elif dataset == 'running_leuven2_dataset':
    
    infoSubjects = {'sub_00': {'massKg': 82.7,
                             'heightM': 1.83,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_01': {'massKg': 49.4,
                             'heightM': 1.68,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_02': {'massKg': 69.1,
                             'heightM': 1.81,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_03': {'massKg': 63.7,
                             'heightM': 1.74,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_04': {'massKg': 49.4,
                             'heightM': 1.67,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_05': {'massKg': 76.1,
                             'heightM': 1.78,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_06': {'massKg': 63.4,
                             'heightM': 1.72,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_07': {'massKg': 59.2,
                             'heightM': 1.72,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_08': {'massKg': 80.3,
                             'heightM': 1.84,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_09': {'massKg': 61.7,
                             'heightM': 1.82,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_10': {'massKg': 64.6,
                             'heightM': 1.77,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_11': {'massKg': 63.8,
                             'heightM': 1.76,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_12': {'massKg': 77.4,
                             'heightM': 1.88,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_13': {'massKg': 68.0,
                             'heightM': 1.85,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_14': {'massKg': 78.7,
                             'heightM': 1.87,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_15': {'massKg': 70.5,
                             'heightM': 1.85,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_16': {'massKg': 66.3,
                             'heightM': 1.74,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_17': {'massKg': 71.6,
                             'heightM': 1.81,
                             'sex': 'unknown',
                             'model': 'normal'},
                    'sub_18': {'massKg': 90.7,
                             'heightM': 1.93,
                             'sex': 'unknown',
                             'model': 'normal'}}
    
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/running_leuven2_dataset'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if infoSubjects[subject]['model'] == 'exclude':
                print('Exclude subject {}'.format(subject))
                continue
            
            # Create new subject folder
            path_subject = os.path.join(path_clean_dataset, subject)
            os.makedirs(path_subject, exist_ok=True)
    
            # Copy generic model
            if infoSubjects[subject]['model'] == 'normal':
                path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
            else:
                raise ValueError("not existing")
            path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
            shutil.copy2(path_generic_model, path_generic_model_end)
            
            # Dump generic demographics
            outfile = os.path.join(path_subject, '_subject.json')
            subject_data = {'massKg': infoSubjects[subject]['massKg'],
                            'heightM': infoSubjects[subject]['heightM'],
                            'sex': infoSubjects[subject]['sex'],
                            'skeletonPreset': 'custom'}
            with open(outfile, "w") as outfile:
                json.dump(subject_data, outfile)
                
            # Re-organize marker data            
            path_original_subject = os.path.join(path_original_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')
            
            
            os.makedirs(path_trials, exist_ok=True)
            for file in os.listdir(path_original_subject):
                if not '.trc' in file:
                    continue
                
                path_trial = os.path.join(path_trials, file[:-4])
                os.makedirs(path_trial, exist_ok=True)
                
                path_generic_trc = os.path.join(path_original_subject, file)
                path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                shutil.copy2(path_generic_trc, path_generic_trc_end)
                
elif dataset == 'toeheel_walking_dataset':
    
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/toeheel_walking_dataset'
    # path_original_dataset = 'C:/MyDriveSym/Projects/openpose-augmenter/Data_opensim/toeheel_walking_dataset'

    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    pathDemographics = os.path.join(path_original_dataset, 'demographics.xlsx')
    
    demographics = pd.read_excel(pathDemographics, engine='openpyxl')
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
        
            if not 'Subject' in subject:
                continue
            
            # Create new subject folder
            path_subject = os.path.join(path_clean_dataset, subject)
            os.makedirs(path_subject, exist_ok=True)
            
            # Get mass and height
            ID = subject.split("_")[0].lower()
            
            code_list = list(demographics['Code'].str.lower())
            code_list = [strip(i) for i in code_list]
            
            massKg = np.round(demographics.loc[code_list.index(ID.lower())]['Weight'],1)
            heightM = np.round(demographics.loc[code_list.index(ID.lower())]['Height']/100,2)
            
            gender = demographics.loc[code_list.index(ID.lower())]['Gender']
            if strip(gender) == 'M':
                sex = 'male'
            elif strip(gender) == 'F':
                sex = 'female'
            else:
                raise ValueError('Gender issue')            
    
            # Copy generic model
            path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
            path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
            shutil.copy2(path_generic_model, path_generic_model_end)
            
            # Dump generic demographics
            outfile = os.path.join(path_subject, '_subject.json')
            subject_data = {'massKg': massKg,
                            'heightM': heightM,
                            'sex': sex,
                            'skeletonPreset': 'custom'}
            with open(outfile, "w") as outfile:
                json.dump(subject_data, outfile)
                
            # Re-organize marker data            
            path_original_subject = os.path.join(path_original_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')
            
            
            os.makedirs(path_trials, exist_ok=True)
            for file in os.listdir(path_original_subject):
                if not '.trc' in file:
                    continue
                
                path_trial = os.path.join(path_trials, file[:-4])
                os.makedirs(path_trial, exist_ok=True)
                
                path_generic_trc = os.path.join(path_original_subject, file)
                path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                shutil.copy2(path_generic_trc, path_generic_trc_end)
                
elif dataset == 'inclined_walking_dataset':
    
    infoSubjects = {'subject_01': {'massKg': 86,
                             'heightM': 1.85,
                             'sex': 'male',
                             'model': 'normal'},
                    'subject_02': {'massKg': 77,
                             'heightM': 1.78,
                             'sex': 'female',
                             'model': 'normal'},
                    'subject_03': {'massKg': 52,
                             'heightM': 1.70,
                             'sex': 'male',
                             'model': 'normal'},
                    'subject_04': {'massKg': 73,
                             'heightM': 1.68,
                             'sex': 'male',
                             'model': 'normal'},
                    'subject_05': {'massKg': 86,
                             'heightM': 1.73,
                             'sex': 'male',
                             'model': 'normal'},
                    'subject_06': {'massKg': 54,
                             'heightM': 1.60,
                             'sex': 'female',
                             'model': 'normal'},
                    'subject_07': {'massKg': 59,
                             'heightM': 1.63,
                             'sex': 'female',
                             'model': 'normal'},
                    'subject_08': {'massKg': 57,
                             'heightM': 1.73,
                             'sex': 'female',
                             'model': 'normal'},
                    'subject_09': {'massKg': 58,
                             'heightM': 1.70,
                             'sex': 'male',
                             'model': 'normal'},
                    'subject_10': {'massKg': 66,
                             'heightM': 1.70,
                             'sex': 'female',
                             'model': 'normal'},
                    'subject_11': {'massKg': 76,
                             'heightM': 1.88,
                             'sex': 'male',
                             'model': 'normal'},
                    'subject_12': {'massKg': 70,
                             'heightM': 1.78,
                             'sex': 'male',
                             'model': 'normal'},
                    'subject_13': {'massKg': 56,
                             'heightM': 1.69,
                             'sex': 'female',
                             'model': 'normal'}}
    
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/inclined_walking_dataset'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if infoSubjects[subject]['model'] == 'exclude':
                print('Exclude subject {}'.format(subject))
                continue
            
            # Create new subject folder
            path_subject = os.path.join(path_clean_dataset, subject)
            os.makedirs(path_subject, exist_ok=True)
    
            # Copy generic model
            if infoSubjects[subject]['model'] == 'normal':
                path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
            else:
                raise ValueError("not existing")
            path_generic_model_end = os.path.join(path_subject, 'unscaled_generic.osim')
            shutil.copy2(path_generic_model, path_generic_model_end)
            
            # Dump generic demographics
            outfile = os.path.join(path_subject, '_subject.json')
            subject_data = {'massKg': infoSubjects[subject]['massKg'],
                            'heightM': infoSubjects[subject]['heightM'],
                            'sex': infoSubjects[subject]['sex'],
                            'skeletonPreset': 'custom'}
            with open(outfile, "w") as outfile:
                json.dump(subject_data, outfile)
                
            # Re-organize marker data            
            path_original_subject = os.path.join(path_original_dataset, subject)
            path_trials = os.path.join(path_subject, 'trials')            
            
            os.makedirs(path_trials, exist_ok=True)
            for file in os.listdir(path_original_subject):
                if not '.trc' in file:
                    continue
                
                path_trial = os.path.join(path_trials, file[:-4])
                os.makedirs(path_trial, exist_ok=True)
                
                path_generic_trc = os.path.join(path_original_subject, file)
                path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                shutil.copy2(path_generic_trc, path_generic_trc_end)
                
elif dataset == 'pitching_dataset':
    
    infoSubjects = {'S1': {'massKg': 54.6,
                             'heightM': 1.65,
                             'sex': 'female',
                             'model': 'normal'},
                    'S2': {'massKg': 54.8,
                             'heightM': 1.60,
                             'sex': 'female',
                             'model': 'normal'},
                    'S3': {'massKg': 56.6,
                             'heightM': 1.62,
                             'sex': 'female',
                             'model': 'normal'},
                    'S4': {'massKg': 57.1,
                             'heightM': 1.59,
                             'sex': 'female',
                             'model': 'normal'},
                    'S5': {'massKg': 73.1,
                             'heightM': 1.65,
                             'sex': 'female',
                             'model': 'normal'},
                    'S6': {'massKg': 51.1,
                             'heightM': 1.60,
                             'sex': 'female',
                             'model': 'normal'},
                    'S7': {'massKg': 48.7,
                             'heightM': 1.55,
                             'sex': 'female',
                             'model': 'normal'}}
    
    # path_original_dataset = 'C:/MyDriveSym/Projects/openpose-augmenter/Data_opensim/pitching_dataset'
    path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/pitching_dataset'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if infoSubjects[subject]['model'] == 'exclude':
                print('Exclude subject {}'.format(subject))
                continue
            
            # Create new subject folder
            # path_subject = os.path.join(path_clean_dataset, subject)
            
            
            for session in os.listdir(os.path.join(path_original_dataset, subject)):          
                if not 'w' in session:
                    continue
                
                pathSubjectSession = os.path.join(path_clean_dataset, subject + '_' + session)
                os.makedirs(pathSubjectSession, exist_ok=True)
        
                # Copy generic model
                if infoSubjects[subject]['model'] == 'normal':
                    path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
                else:
                    raise ValueError("not existing")
                path_generic_model_end = os.path.join(pathSubjectSession, 'unscaled_generic.osim')
                shutil.copy2(path_generic_model, path_generic_model_end)
                
                # Dump generic demographics
                outfile = os.path.join(pathSubjectSession, '_subject.json')
                subject_data = {'massKg': infoSubjects[subject]['massKg'],
                                'heightM': infoSubjects[subject]['heightM'],
                                'sex': infoSubjects[subject]['sex'],
                                'skeletonPreset': 'custom'}
                with open(outfile, "w") as outfile:
                    json.dump(subject_data, outfile)
                    
                # Re-organize marker data            
                path_original_subject = os.path.join(path_original_dataset, subject, session)
                path_trials = os.path.join(pathSubjectSession, 'trials')            
                
                os.makedirs(path_trials, exist_ok=True)
                for file in os.listdir(path_original_subject):
                    if not '_trimmed.trc' in file:
                        continue
                    
                    path_trial = os.path.join(path_trials, file[:-12])
                    os.makedirs(path_trial, exist_ok=True)
                    
                    path_generic_trc = os.path.join(path_original_subject, file)
                    path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                    shutil.copy2(path_generic_trc, path_generic_trc_end)
                    
elif dataset == 'karate_dataset':
    
    infoSubjects = {
        'B0367': {'model': 'exclude'},
        'B0368': {'model': 'exclude'},
        'B0369': {
            'massKg': 88,
            'heightM': 1.82,
            'sex': 'male',
            'model': 'normal'},
        'B0370': {
            'massKg': 71,
            'heightM': 1.78,
            'sex': 'male',
            'model': 'normal'},
        'B0371': {
            'massKg': 78,
            'heightM': 1.72,
            'sex': 'male',
            'model': 'normal'},
        'B0372': {
            'massKg': 74,
            'heightM': 1.72,
            'sex': 'male',
            'model': 'normal'},
        'B0373': {
            'massKg': 62,
            'heightM': 1.68,
            'sex': 'female',
            'model': 'normal'},
        'B0374': {
            'massKg': 42,
            'heightM': 1.50,
            'sex': 'male',
            'model': 'normal'},
        'B0375': {
            'massKg': 45,
            'heightM': 1.52,
            'sex': 'female',
            'model': 'normal'},
        'B0376': {
            'massKg': 35,
            'heightM': 1.43,
            'sex': 'female',
            'model': 'normal'},
        'B0377': {
            'massKg': 44,
            'heightM': 1.54,
            'sex': 'male',
            'model': 'normal'},
        'B0378': {
            'massKg': 49,
            'heightM': 1.56,
            'sex': 'male',
            'model': 'normal'},
        'B0379': {
            'massKg': 35,
            'heightM': 1.45,
            'sex': 'male',
            'model': 'normal'},
        'B0380': {
            'massKg': 30,
            'heightM': 1.44,
            'sex': 'male',
            'model': 'normal'},
        'B0381': {
            'massKg': 50,
            'heightM': 1.61,
            'sex': 'male',
            'model': 'normal'},
        'B0382': {
            'massKg': 86,
            'heightM': 1.82,
            'sex': 'male',
            'model': 'normal'},
        'B0383': {
            'massKg': 36,
            'heightM': 1.42,
            'sex': 'male',
            'model': 'normal'},
        'B0384': {
            'massKg': 44,
            'heightM': 1.51,
            'sex': 'male',
            'model': 'normal'},
        'B0385': {
            'massKg': 42,
            'heightM': 1.50,
            'sex': 'female',
            'model': 'normal'},
        'B0386': {
            'massKg': 45,
            'heightM': 1.52,
            'sex': 'female',
            'model': 'normal'},
        'B0387': {
            'massKg': 52,
            'heightM': 1.58,
            'sex': 'female',
            'model': 'normal'},
        'B0388': {
            'massKg': 54,
            'heightM': 1.57,
            'sex': 'female',
            'model': 'normal'},
        'B0389': {
            'massKg': 52,
            'heightM': 1.53,
            'sex': 'female',
            'model': 'normal'},
        'B0391': {
            'massKg': 80,
            'heightM': 1.80,
            'sex': 'male',
            'model': 'normal'},
        'B0392': {
            'massKg': 118,
            'heightM': 1.92,
            'sex': 'male',
            'model': 'normal'},
        'B0393': {
            'massKg': 40,
            'heightM': 1.60,
            'sex': 'male',
            'model': 'normal'},
        'B0394': {
            'massKg': 30,
            'heightM': 1.42,
            'sex': 'male',
            'model': 'normal'},
        'B0395': {
            'massKg': 45,
            'heightM': 1.58,
            'sex': 'male',
            'model': 'normal'},
        'B0396': {
            'massKg': 47,
            'heightM': 1.64,
            'sex': 'female',
            'model': 'normal'},
        'B0398': {
            'massKg': 62,
            'heightM': 1.76,
            'sex': 'female',
            'model': 'normal'},
        'B0399': {
            'massKg': 70,
            'heightM': 1.66,
            'sex': 'female',
            'model': 'normal'},
        'B0400': {
            'massKg': 35,
            'heightM': 1.50,
            'sex': 'male',
            'model': 'normal'},
        'B0401': {
            'massKg': 39,
            'heightM': 1.52,
            'sex': 'male',
            'model': 'normal'},
        'B0402': {
            'massKg': 34,
            'heightM': 1.50,
            'sex': 'male',
            'model': 'normal'},
        'B0403': {
            'massKg': 32,
            'heightM': 1.43,
            'sex': 'male',
            'model': 'normal'},
        'B0404': {
            'massKg': 67,
            'heightM': 1.63,
            'sex': 'female',
            'model': 'normal'},
        'B0405': {
            'massKg': 62,
            'heightM': 1.62,
            'sex': 'female',
            'model': 'normal'}}
    
    path_original_dataset = 'C:/MyDriveSym/Projects/openpose-augmenter/Data_opensim/karate_dataset'
    # path_original_dataset = '/home/clarkadmin/Documents/myDatasets_Antoine/karate_dataset'
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
            if subject not in infoSubjects:
                continue
            
            if infoSubjects[subject]['model'] == 'exclude':
                print('Exclude subject {}'.format(subject))
                continue
                        
            # Create new subject folder
            # path_subject = os.path.join(path_clean_dataset, subject)
                        
            c_session = 1
            for session in os.listdir(os.path.join(path_original_dataset, subject)):          
                if not subject in session:
                    continue
                
                pathSubjectSession = os.path.join(path_clean_dataset, subject + '_S0' + str(c_session))
                os.makedirs(pathSubjectSession, exist_ok=True)
        
                # Copy generic model
                if infoSubjects[subject]['model'] == 'normal':
                    path_generic_model = os.path.join(path_original_dataset, 'model_markers.osim')
                else:
                    raise ValueError("not existing")
                path_generic_model_end = os.path.join(pathSubjectSession, 'unscaled_generic.osim')
                shutil.copy2(path_generic_model, path_generic_model_end)
                
                # Dump generic demographics
                outfile = os.path.join(pathSubjectSession, '_subject.json')
                subject_data = {'massKg': infoSubjects[subject]['massKg'],
                                'heightM': infoSubjects[subject]['heightM'],
                                'sex': infoSubjects[subject]['sex'],
                                'skeletonPreset': 'custom'}
                with open(outfile, "w") as outfile:
                    json.dump(subject_data, outfile)
                    
                # Re-organize marker data            
                path_original_subject = os.path.join(path_original_dataset, subject, session)
                path_trials = os.path.join(pathSubjectSession, 'trials')            
                
                os.makedirs(path_trials, exist_ok=True)
                for file in os.listdir(path_original_subject):
                    if not '_cleaned.trc' in file:
                        continue
                    
                    path_trial = os.path.join(path_trials, file[:-12])
                    os.makedirs(path_trial, exist_ok=True)
                    
                    path_generic_trc = os.path.join(path_original_subject, file)
                    path_generic_trc_end = os.path.join(path_trial, 'markers.trc')
                    shutil.copy2(path_generic_trc, path_generic_trc_end)
                    
                c_session += 1
