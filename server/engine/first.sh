#!/bin/bash
for n in 61 20 126 03 90 16 139 75 07 43 115 89 10 93 79 73 46 34 76 123 88 25 140 70 37 84 08 11 118 128 107 134 24;
do
    sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cmu_dataset/$n/osim_results "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cmu_dataset/$n"
    sshpass -p 'Stanford!' scp clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cmu_dataset/$n/_results.json "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cmu_dataset/$n"
done

