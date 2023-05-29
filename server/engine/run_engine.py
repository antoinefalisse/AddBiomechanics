import os
from engine import processLocalSubjectFolder

path_main = os.getcwd()
path_server = os.path.dirname(path_main)
path_data = os.path.join(path_server, 'data')

dataset = 'totalcapture_openpose_v0.45'
    
if dataset == 'opencap_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('subject' in file):
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

elif dataset == 'opencap_dataset_video':

    poseDetector = 'OpenPose_1x1008_4scales'
    cameraSetup = '2-cameras'
    augmenter_model = 'v0.15'

    path_dataset = os.path.join(path_data, dataset + '_' + poseDetector + '_' + cameraSetup + '_' + augmenter_model)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('subject' in file):
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
            
    subjects_nonProcessed = ['subject2']

    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        try:
            processLocalSubjectFolder(pathSubject)
        except:
            pass
        
    test=1

elif dataset == 'balance_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('Subj' in file):
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

elif dataset == 'toeheel_walking_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('Subj' in file):
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

elif dataset == 'hamner2013':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('subject' in file):
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

elif dataset == 'karate_dataset':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('B0' in file):
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

elif dataset == 'totalcapture_2':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('s' in file):
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
            
    # subjects_nonProcessed = ['s4_acting3', 's4_freestyle1', 's4_freestyle3', 's4_rom3', 's4_walking2']
    subjects_nonProcessed = [
        # 's2_acting1', 's2_acting2', 's2_acting3',
          's2_freestyle1',
                             's2_freestyle2', 's2_freestyle3', 's2_rom1', 's2_rom2', 's2_rom3',
                             's2_walking1', 's2_walking2', 's2_walking3']
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        try:
            processLocalSubjectFolder(pathSubject)
        except:
            pass
        
    test=1

elif dataset == 'totalcapture_openpose_v0.45':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('s' in file):
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
            
    # subjects_nonProcessed = ['s4_acting3', 's4_freestyle1', 's4_freestyle3', 's4_rom3', 's4_walking2']
    # subjects_nonProcessed = [
        # 's2_acting1', 's2_acting2', 's2_acting3',
        #   's2_freestyle1',
        #                      's2_freestyle2', 's2_freestyle3', 's2_rom1', 's2_rom2', 's2_rom3',
        #                      's2_walking1', 's2_walking2', 's2_walking3']
    for subject in subjects_nonProcessed:
        print("Processing {}".format(subject))
        pathSubject = os.path.join(path_dataset, subject)
        try:
            processLocalSubjectFolder(pathSubject)
        except:
            pass
        
    test=1