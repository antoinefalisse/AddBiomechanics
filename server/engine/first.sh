#!/bin/bash
for n in 083;
# for n in 150;
do
	# if [ ! -d "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cmu_dataset/$n/osim_results" ]; then	
		# sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cmu_dataset/$n/osim_results "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cmu_dataset/$n"
		# sshpass -p 'Stanford!' scp clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cmu_dataset/$n/_results.json "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cmu_dataset/$n"
	# fi
	
	# sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cycling_dataset/P$n/osim_results "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cycling_anthony_cleaned/P$n"
	
	# sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cycling_dataset/P$n/_results.json "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cycling_anthony_cleaned/P$n/osim_results"
	
	# sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/balance_dataset/$n/osim_results "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/balance_dataset_cleaned/$n"
	
	# sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/balance_dataset/$n/_results.json "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/balance_dataset_cleaned/$n/osim_results"
	
	sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/myer_dataset/PreTesting_2017_fall/anmt$n/osim_results "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/myer_dataset_cleaned/PreTesting_2017_fall/ANMT$n_Base_08_17_2017"
	
	
done