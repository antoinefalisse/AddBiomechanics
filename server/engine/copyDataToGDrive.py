# Copy back opencap results for further analysis

import os
import shutil


path_main = os.getcwd()
path_server = os.path.dirname(path_main)
path_data = os.path.join(path_server, 'data')

dataset = 'opencap_dataset_video'
    
if dataset == 'opencap_dataset':

    path_dataset_end = 'C:/MyDriveSym/Projects/mobilecap/Data'
    path_dataset = os.path.join(path_data, dataset)

    # Subjects are folders in path_dataset starting with subject
    subjects = []
    for file in os.listdir(path_dataset):
        if ('subject' in file):
            subjects.append(file)
    
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathSubjectEnd = os.path.join(path_dataset_end, subject, 'OpenSimData', 'Mocap', 'Addbiomechanics')
        os.makedirs(pathSubjectEnd, exist_ok=True)

        # Copy model
        pathModel = os.path.join(pathSubject, 'osim_results', 'Models', 'optimized_scale_and_markers.osim')
        pathModelFolderEnd = os.path.join(pathSubjectEnd, 'Model', 'LaiArnold2107_OpenCapMocap')
        # Delete pathModelFolderEnd if it exists
        if os.path.exists(pathModelFolderEnd):
            shutil.rmtree(pathModelFolderEnd)
        os.makedirs(pathModelFolderEnd, exist_ok=True)
        pathModelEnd = os.path.join(pathModelFolderEnd, 'optimized_scale_and_markers.osim')
        shutil.copyfile(pathModel, pathModelEnd)

        # Copy IK results
        pathIK = os.path.join(pathSubject, 'osim_results', 'IK')
        pathIKFolderEnd = os.path.join(pathSubjectEnd, 'IK', 'LaiArnold2107_OpenCapMocap')
        # Delete pathIKFolderEnd if it exists
        if os.path.exists(pathIKFolderEnd):
            shutil.rmtree(pathIKFolderEnd)
        os.makedirs(pathIKFolderEnd, exist_ok=True)
        for file in os.listdir(pathIK):
            if ('.mot' in file):
                pathIKFile = os.path.join(pathIK, file)
                pathIKFileEnd = os.path.join(pathIKFolderEnd, file)
                # Replace _ik.mot by .mot
                pathIKFileEnd = pathIKFileEnd.replace('_ik.mot', '.mot')
                shutil.copyfile(pathIKFile, pathIKFileEnd)

if dataset == 'opencap_dataset_video':

    poseDetector = 'OpenPose_1x1008_4scales'
    cameraSetup = '2-cameras'
    augmenter_model = 'v0.15'

    path_dataset_end = 'C:/MyDriveSym/Projects/mobilecap/Data'
    path_dataset = os.path.join(path_data, dataset + '_' + poseDetector + '_' + cameraSetup + '_' + augmenter_model)

    # Subjects are folders in path_dataset starting with subject
    subjects = []
    for file in os.listdir(path_dataset):
        if ('subject' in file):
            subjects.append(file)
    
    for subject in subjects:
        pathSubject = os.path.join(path_dataset, subject)
        pathSubjectEnd = os.path.join(path_dataset_end, subject, 'OpenSimData', 'Video', poseDetector, cameraSetup, augmenter_model, 'Addbiomechanics')
        os.makedirs(pathSubjectEnd, exist_ok=True)

        # Copy model
        pathModel = os.path.join(pathSubject, 'osim_results', 'Models', 'optimized_scale_and_markers.osim')
        pathModelFolderEnd = os.path.join(pathSubjectEnd, 'Model', 'LaiArnold2107_OpenCapVideo')
        # Delete pathModelFolderEnd if it exists
        if os.path.exists(pathModelFolderEnd):
            shutil.rmtree(pathModelFolderEnd)
        os.makedirs(pathModelFolderEnd, exist_ok=True)
        pathModelEnd = os.path.join(pathModelFolderEnd, 'optimized_scale_and_markers.osim')
        shutil.copyfile(pathModel, pathModelEnd)

        # Copy IK results
        pathIK = os.path.join(pathSubject, 'osim_results', 'IK')
        pathIKFolderEnd = os.path.join(pathSubjectEnd, 'IK', 'LaiArnold2107_OpenCapVideo')
        # Delete pathIKFolderEnd if it exists
        if os.path.exists(pathIKFolderEnd):
            shutil.rmtree(pathIKFolderEnd)
        os.makedirs(pathIKFolderEnd, exist_ok=True)
        for file in os.listdir(pathIK):
            if ('.mot' in file):
                pathIKFile = os.path.join(pathIK, file)
                pathIKFileEnd = os.path.join(pathIKFolderEnd, file)
                # Replace _ik.mot by .mot
                pathIKFileEnd = pathIKFileEnd.replace('_ik.mot', '.mot')
                shutil.copyfile(pathIKFile, pathIKFileEnd)








