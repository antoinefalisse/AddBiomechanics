# sed -i 's/\r//' copy_data.sh


# for n in subject2 subject3 subject4 subject5 subject6 subject7 subject8 subject9 subject10 subject11;
# do
# 	if [ ! -d "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/opencap_dataset/$n/_results.json" ]; then	
# 		sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/opencap_dataset/$n/_results.json "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/opencap_dataset/$n/"
# 		sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/opencap_dataset/$n/osim_results "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/opencap_dataset/$n/"
# 	fi	
# done;

dataset="balance_dataset"
for n in Subj03 Subj03 Subj03 Subj03 Subj03 Subj03;
do
	if [ ! -d "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/$dataset/$n/_results.json" ]; then	
		sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/$dataset/$n/_results.json "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/$dataset/$n/"
		sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/$dataset/$n/osim_results "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/$dataset/$n/"
	fi	
done;

# Copy data to Linux machine
# dataset="toeheel_walking_dataset"
# sshpass -p 'Stanford!' scp -r /mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/$dataset/* "clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/$dataset/"