#!/bin/bash
for n in 011 012 013 014 015 016 018 019 020 021 022 023 025 026 028 029 031 032 033 034 036 038 039 040 041 042 043 045 050 051;
do
	# if [ ! -d "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cmu_dataset/$n/osim_results" ]; then	
		# sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cmu_dataset/$n/osim_results "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cmu_dataset/$n"
		# sshpass -p 'Stanford!' scp clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cmu_dataset/$n/_results.json "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cmu_dataset/$n"
	# fi
	
	sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cycling_dataset/P$n/osim_results "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cycling_anthony_cleaned/P$n"
	
	sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cycling_dataset/P$n/_results.json "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cycling_anthony_cleaned/P$n/osim_results"
done