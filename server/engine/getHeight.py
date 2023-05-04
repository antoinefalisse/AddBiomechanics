import os
import dataman

path_main = os.getcwd()
path_server = os.path.dirname(path_main)
path_data = os.path.join(path_server, 'data')

dataset = 'totalcapture_2'

if dataset == 'totalcapture_2':

    path_dataset = os.path.join(path_data, dataset)
    subjects = []
    for file in os.listdir(path_dataset):
        if ('s1_acting1' in file):
            pathStatic = os.path.join(path_dataset, file, 'trials', 'static', 'markers.trc')
            trc_file = dataman.TRCFile(pathStatic)




