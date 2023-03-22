import os
from engine import processLocalSubjectFolder

path_main = os.getcwd()
path_server = os.path.dirname(path_main)
path_data = os.path.join(path_server, 'data')

dataset = 'opencap_dataset'
    
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
        
    test=1
