import os
import shutil
import json

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
    
    path_original_dataset = os.path.join(path_my_datasets, dataset)
    path_clean_dataset = os.path.join(path_data, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    # Loop over subjects
    for subject in os.listdir(path_original_dataset):
        if os.path.isdir(os.path.join(path_original_dataset, subject)):
            
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
                
    
    
    