import os
import shutil
import json
import pandas as pd

path_main = os.getcwd()
path_server = os.path.dirname(path_main)
path_data = os.path.join(path_server, 'data')

# Generic data
subject_data = {'massKg': 68,
                'heightM': 1.6,
                'sex': 'unknowm',
                'skeletonPreset': 'custom'}

# Pick dataset
dataset = 'myer_dataset'

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
    
    folders = ['PreTesting_2019_summer']
    
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
                path_generic_model = os.path.join(path_original_dataset, 'model_markers_noArms.osim')
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