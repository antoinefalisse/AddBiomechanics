import os
import shutil
import json
# import nimblephysics as nimble
import numpy as np
import pandas as pd
import opensim

path_main = os.getcwd()
# path_server = os.path.dirname(path_main)
# path_data = os.path.join(path_server, 'data')

dataDir = 'C:/MyDriveSym/Projects/openpose-augmenter/Data_opensim/'

# Pick dataset
dataset = 'cmu_dataset'

if dataset == 'cmu_dataset':
    
    # processed_subjects = ['01']
    
    processed_subjects = [
        '105', '21', '114', '82', '33', '02', '133', '103', 
        '141', '39', '17', '104', '01', '56', '111', '41', 
        '38', '23', '125', '143', '64', '49', '127', '45',
        '06', '91', '35', '61', '20', '126', '03', '90', 
        '16', '139', '75', '07', '43', '31', '115', '89',
        '10', '93', '32', '79', '73', '132', '46', '29', 
        '34', '54', '76', '123', '88', '83', '25', '142', 
        '140', '70', '15', '37', 
        '84', '08', '11', '55', 
        '113', '26', '80', '78', '102', '118', '128', '107',
        '19', '14', '134', '24', '77', '62', '87', '18', 
        '124', '42', '135', '40', '05', '94', '122', '137', 
        '09', '36', '136', '47', '63', '108', '13', '144', 
        '12', '28', '74', '27', '131', '22', '30', '86', 
        '120', '85', '60', '106']
    
    markers = ['LMT5', 'LFHD']
    
    path_clean_dataset = os.path.join(dataDir, dataset)
    os.makedirs(path_clean_dataset, exist_ok=True)
    
    demographics = {}
    
    # Loop over subjects
    count = 0
    count1 = 0
    # print(os.listdir(path_clean_dataset))
    for subject in os.listdir(path_clean_dataset):
        if subject in processed_subjects:
            pathSubject = os.path.join(path_clean_dataset, subject)            
            pathResults = os.path.join(pathSubject, 'osim_results')
            pathModel = os.path.join(pathResults, 'Models', 'optimized_scale_and_markers.osim')
            pathPK = os.path.join(pathResults, 'Models', 'PK')
            os.makedirs(pathPK, exist_ok=True)
            # Compute height using marker data    
            opensim.Logger.setLevelString('error')
            model = opensim.Model(pathModel)
            model.initSystem()
            marketSet = model.get_MarkerSet() 
            # Settings.
            pathGenericSetupFile = 'Setup_PK_generic.xml'    
            pathMotionFile = os.path.join(path_main, 'static.mot')
            ATool = opensim.AnalyzeTool(pathGenericSetupFile, False)
            ATool.setName("PK_" + subject)
            ATool.setModelFilename(pathModel)   
            ATool.setStartTime(0)
            ATool.setFinalTime(0.075)               
            ATool.setResultsDir(pathPK)
            ATool.setCoordinatesFileName(pathMotionFile)
            pathSetupFile = os.path.join(pathPK, "Setup_PK_static.xml")
            # Analyses.
            analysisSet = ATool.getAnalysisSet()
            PK = analysisSet.get("PointKinematics")  
            # Adjust settings of the "first" PK.
            cObj0 = opensim.PointKinematics.safeDownCast(PK)
            cObj0.setStartTime(0)
            cObj0.setEndTime(0.075)
            cObj0.setBody(marketSet.get(markers[0]).getParentFrame())                
            cObj0.setRelativeToBody(model.get_ground())
            cObj0.setPointName(markers[0])
            cObj0.setPoint(marketSet.get(markers[0]).get_location())
            # Clone and adjust settings for the remaining PKs.               
            for marker in markers[1:]:    
                cObj_iter = cObj0.clone()
                cObj_iter.setStartTime(0)
                cObj_iter.setEndTime(0.075)              
                cObj_iter.setBody(marketSet.get(marker).getParentFrame())                
                cObj_iter.setRelativeToBody(model.get_ground())
                cObj_iter.setPointName(marker)
                cObj_iter.setPoint(marketSet.get(marker).get_location())                
                analysisSet.adoptAndAppend(cObj_iter)
            # Print setup files.
            ATool.printToXML(pathSetupFile)
            # Run tool.
            cmd = 'opensim-cmd run-tool {}'.format(pathSetupFile)
            os.system(cmd)
            
            # Remove useless files
            positions = {}
            for marker in markers:
                pathAcc = os.path.join(pathPK, 'PK_{}_PointKinematics_{}_acc.sto'.format(subject, marker))
                pathVel = os.path.join(pathPK, 'PK_{}_PointKinematics_{}_vel.sto'.format(subject, marker))
                os.remove(pathAcc)
                os.remove(pathVel)
                
                # Import position file
                pathPos = os.path.join(pathPK, 'PK_{}_PointKinematics_{}_pos.sto'.format(subject, marker))
                table = opensim.TimeSeriesTable(pathPos)
                positions[marker] = table.getMatrix().to_numpy()[0, :]
                
            # Add 7cm for distance between top markers and top of head, roughly.
            height = np.round(positions[markers[1]][1] - positions[markers[0]][1] + 0.07 ,2)
            print(height)        
            
            # Weight (kinda random based on ideal weight formula with noise)
            # Ideal weight based on height, D.R. Miller Formula (1983)
            # Male:     56.2 kg + 1.41 kg per inch (0.0254m) over 5 feet (1.524m)
            # Female:   53.1 kg + 1.36 kg per inch over 5 feet
            # one inch: 2.54cm
            # 5 feet: 1.524m
            
            if height > 1.524:
                weight = 54.65 + 1.385*((height-1.524)/0.0254)
                # Add 20% variability
                weight += (weight * (np.random.uniform(-1.0,1.0,1)*0.2))
                print(np.round(weight[0], 1))
            else:
                print('Warning: short person')
                
            demographics[subject] = {'height': height,
                                     'weight': np.round(weight[0], 1)}
