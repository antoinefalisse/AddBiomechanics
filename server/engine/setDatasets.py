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
                
elif dataset == 'cycling':
    
    infoSubjects = {'P003': {'massKg': 76.5,
                             'heightM': 1.78,
                             'sex': 'female'},
                    'P004': {'massKg': 102.3,
                             'heightM': 1.83,
                             'sex': 'male'},
                    'P005': {'massKg': 60.6,
                             'heightM': 1.62,
                             'sex': 'female'},
                    'P006': {'massKg': 92.3,
                             'heightM': 1.82,
                             'sex': 'male'},
                    'P007': {'massKg': 68.1,
                             'heightM': 1.72,
                             'sex': 'female'},
                    'P008': {'massKg': 66,
                             'heightM': 1.57,
                             'sex': 'female'},
                    'P009': {'massKg': 75.7,
                             'heightM': 1.79,
                             'sex': 'male'},
                    'P010': {'massKg': 74.2,
                             'heightM': 1.71,
                             'sex': 'male'},
                    'P011': {'massKg': 64.2,
                             'heightM': 1.68,
                             'sex': 'male'},
                    'P012': {'massKg': 61.1,
                             'heightM': 1.66,
                             'sex': 'female'},
                    'P013': {'massKg': 64.1,
                             'heightM': 1.58,
                             'sex': 'female'},
                    'P014': {'massKg': 66,
                             'heightM': 1.69,
                             'sex': 'female'},
                    'P015': {'massKg': 90.8,
                             'heightM': 1.95,
                             'sex': 'male'},
                    'P016':  {'massKg': 92.1,
                             'heightM': 1.78,
                             'sex': 'female'},
                    'P018': {'massKg': 79.4,
                             'heightM': 1.88,
                             'sex': 'male'},
                    'P019': {'massKg': 86,
                             'heightM': 1.87,
                             'sex': 'male'},
                    'P020': {'massKg': 68.8,
                             'heightM': 1.65,
                             'sex': 'male'},
                    'P021': {'massKg': 66.5,
                             'heightM': 1.73,
                             'sex': 'male'},
                    'P022': {'massKg': 59.7,
                             'heightM': 1.66,
                             'sex': 'female'},
                    'P023': {'massKg': 76.1,
                             'heightM': 1.80,
                             'sex': 'male'},
                    'P025': {'massKg': 75.6,
                             'heightM': 1.71,
                             'sex': 'male'},
                    'P026': {'massKg': 61.1,
                             'heightM': 1.64,
                             'sex': 'female'},
                    'P027': {'massKg': 70.5,
                             'heightM': 1.72,
                             'sex': 'male'},
                    'P028': {'massKg': 81.9,
                             'heightM': 1.81,
                             'sex': 'male'},
                    'P029': {'massKg': 89.3,
                             'heightM': 1.84,
                             'sex': 'male'},
                    'P031': {'massKg': 54.2,
                             'heightM': 1.63,
                             'sex': 'female'},
                    'P032':  {'massKg': 91.5,
                             'heightM': 1.84,
                             'sex': 'male'},
                    'P033': {'massKg': 66.1,
                             'heightM': 1.67,
                             'sex': 'female'},
                    'P034': {'massKg': 65.8,
                             'heightM': 1.73,
                             'sex': 'female'},
                    'P036': {'massKg': 56.7,
                             'heightM': 1.60,
                             'sex': 'female'},
                    'P038': {'massKg': 79.9,
                             'heightM': 1.88,
                             'sex': 'male'},
                    'P039': {'massKg': 63.2,
                             'heightM': 1.76,
                             'sex': 'male'},
                    'P040': {'massKg': 78,
                             'heightM': 1.57,
                             'sex': 'female'},
                    'P041': {'massKg': 57.1,
                             'heightM': 1.69,
                             'sex': 'female'},
                    'P042': {'massKg': 90.8,
                             'heightM': 1.84,
                             'sex': 'male'},
                    'P043': {'massKg': 74.5,
                             'heightM': 1.80,
                             'sex': 'male'},
                    'P045': {'massKg': 91.3,
                             'heightM': 1.81,
                             'sex': 'male'}}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
    
    
    