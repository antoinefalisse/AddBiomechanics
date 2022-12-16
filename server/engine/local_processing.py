import os
from engine import processLocalSubjectFolder
from engine_local import processLocalSubjectFolder_local
from engine_testing import processLocalSubjectFolder_testing


path_main = os.getcwd()
path_server = os.path.dirname(path_main)
path_data = os.path.join(path_server, 'data')


dataset = 'pitching_dataset'

if dataset == 'cmu_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file)
            subjects.append(file)
        except:
            pass
    
    marker_set_fixed = ['C7', 'T10', 'CLAV', 'STRN', 'RELB', 'RWRA', 'RWRB',
                        'LELB', 'LWRA', 'LWRB', 'RFWT', 'LFWT', 'RBWT', 'LBWT',
                        'RKNE', 'RANK', 'RHEE', 'RTOE', 'RMT5', 
                        'LKNE', 'LANK', 'LHEE', 'LTOE', 'LMT5']
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
    print(subjects_Processed)
    print(len(subjects_Processed))
    print(subjects_nonProcessed)
    print(len(subjects_nonProcessed))
    
    # for subject in subjects_nonProcessed[1:]:
    subject = '150'
    print("Processing {}".format(subject))
    pathSubject = os.path.join(path_dataset, subject)
    processLocalSubjectFolder_local(pathSubject, marker_set_fixed=marker_set_fixed)
    
elif dataset == 'cycling_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file[1:])
            subjects.append(file)
        except:
            pass
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    print(subjects_Processed)
    print(len(subjects_Processed))
    print(subjects_nonProcessed)
    print(len(subjects_nonProcessed))
    
    for subject in subjects_nonProcessed:
    # subject = 'P003'
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        processLocalSubjectFolder(pathSubject)
        
elif dataset == 'balance_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file[4:])
            subjects.append(file)
        except:
            pass
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        processLocalSubjectFolder(pathSubject)
        
elif dataset == 'myer_dataset':

    folders = ['PreTesting_2017_fall_VR', 'PreTesting_2017_summer_VR', 
           'PreTesting_2018_summer_VR', 'PreTesting_2019_fall_VR', 
           'PreTesting_2019_summer_VR']
    
    session = folders[4]

    path_dataset = os.path.join(path_data, dataset, session)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file[-3:])
            subjects.append(file)
        except:
            pass
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        processLocalSubjectFolder(pathSubject)

elif dataset == 'hamstrings_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file[4:])
            subjects.append(file)
        except:
            pass
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        processLocalSubjectFolder(pathSubject)

elif dataset == 'multimodal_walking_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file[4:])
            subjects.append(file)
        except:
            pass
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        processLocalSubjectFolder(pathSubject)

elif dataset == 'parameter_estimation_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file[4:])
            subjects.append(file)
        except:
            pass
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        processLocalSubjectFolder(pathSubject)

elif dataset == 'running_leuven1_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file[4:])
            subjects.append(file)
        except:
            pass
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        processLocalSubjectFolder(pathSubject)

elif dataset == 'running_leuven2_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file[4:])
            subjects.append(file)
        except:
            pass
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        processLocalSubjectFolder(pathSubject)
        
elif dataset == 'inclined_walking_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file[8:])
            subjects.append(file)
        except:
            pass
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        processLocalSubjectFolder(pathSubject)

elif dataset == 'toeheel_walking_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        try:
            idx_file = int(file[7:])
            subjects.append(file)
        except:
            pass
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        processLocalSubjectFolder(pathSubject)

elif dataset == 'pitching_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if 'w' in file:
            subjects.append(file)
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed[:1]:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        try:
            processLocalSubjectFolder(pathSubject)
        except:
            pass
        
    test=1

elif dataset == 'karate_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if 'B0' in file:
            subjects.append(file)
    
    print(subjects)
    print(len(subjects))
    subjects_Processed = []
    subjects_nonProcessed = []
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathJson = os.path.join(pathSubject, '_results.json')
        if os.path.exists(pathJson):
            subjects_Processed.append(subject)
        else:
            subjects_nonProcessed.append(subject)
            
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        try:
            processLocalSubjectFolder(pathSubject)
        except:
            pass
        
    test=1