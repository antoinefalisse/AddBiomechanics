import nimblephysics as nimble
import os
import numpy as np
        
def numpy2TRC(f, data, headers, fc=50.0, t_start=0.0, units="m"):
    
    header_mapping = {}
    for count, header in enumerate(headers):
        header_mapping[count+1] = header 
        
    # Line 1.
    f.write('PathFileType  4\t(X/Y/Z) %s\n' % os.getcwd())
    
    # Line 2.
    f.write('DataRate\tCameraRate\tNumFrames\tNumMarkers\t'
                'Units\tOrigDataRate\tOrigDataStartFrame\tOrigNumFrames\n')
    
    num_frames=data.shape[0]
    num_markers=len(header_mapping.keys())
    
    # Line 3.
    f.write('%.1f\t%.1f\t%i\t%i\t%s\t%.1f\t%i\t%i\n' % (
            fc, fc, num_frames,
            num_markers, units, fc,
            1, num_frames))
    
    # Line 4.
    f.write("Frame#\tTime\t")
    for key in sorted(header_mapping.keys()):
        f.write("%s\t\t\t" % format(header_mapping[key]))

    # Line 5.
    f.write("\n\t\t")
    for imark in np.arange(num_markers) + 1:
        f.write('X%i\tY%s\tZ%s\t' % (imark, imark, imark))
    f.write('\n')
    
    # Line 6.
    f.write('\n')

    for frame in range(data.shape[0]):
        f.write("{}\t{:.8f}\t".format(frame,(frame)/fc+t_start))

        for key in sorted(header_mapping.keys()):
            f.write("{:.8f}\t{:.8f}\t{:.8f}\t".format(data[frame,0+(key-1)*3], data[frame,1+(key-1)*3], data[frame,2+(key-1)*3]))
        f.write("\n")  


def getTRCfromC3D(path: str, pathOutputFile=None):
    
    c3dFile: nimble.biomechanics.C3D = nimble.biomechanics.C3DLoader.loadC3D(path)
    nimble.biomechanics.C3DLoader.fixupMarkerFlips(c3dFile)
    markers = c3dFile.markers
    markerTimesteps = c3dFile.markerTimesteps
    time = c3dFile.timestamps
    
    marker_data = np.zeros((len(time), len(markers)*3))
    for m, marker in enumerate(markers):
        for i in range(len(time)):
            if marker in markerTimesteps[i]:
                marker_data[i,m*3:(m+1)*3] = markerTimesteps[i][marker]
                
    data_rate = np.round(np.mean(1/np.diff(time)),2)
                
    if pathOutputFile is None:
        pathOutputFile = path[:-4] + '.trc'
    print(pathOutputFile)
    with open(pathOutputFile, "w") as f:
        numpy2TRC(f, marker_data, markers, fc=data_rate, t_start=time[0])

if __name__ == "__main__":
    
    path_my_datasets = '/home/clarkadmin/Documents/myDatasets_Antoine'
    
    dataset = 'tennis_dataset'

    path_dataset = os.path.join(path_my_datasets, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('sub' in file):
            subjects.append(file)
            
    subjects = ['sub_01', 'sub_02','sub_03','sub_04','sub_05','sub_06','sub_07','sub_08','sub_09','sub_10','sub_11','sub_12']
    for subject in subjects:
        print("Processing {}".format(subject))
        path_subject = os.path.join(path_dataset, subject)
        for file in os.listdir(path_subject):            
            if '.c3d' in file:            
                path_file = os.path.join(path_subject, file)
                pathOutputFile = path_file[:-4] + '_nimble.trc'
                getTRCfromC3D(path_file, pathOutputFile)
        
    test=1

