# sed -i 's/\r//' copy_data.sh


# for n in subject2 subject3 subject4 subject5 subject6 subject7 subject8 subject9 subject10 subject11;
# do
# 	if [ ! -d "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/opencap_dataset/$n/_results.json" ]; then	
# 		sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/opencap_dataset/$n/_results.json "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/opencap_dataset/$n/"
# 		sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/opencap_dataset/$n/osim_results "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/opencap_dataset/$n/"
# 	fi	
# done;

# dataset="toeheel_walking_dataset"
# for n in Subject2 Subject3 Subject4 Subject5 Subject6 Subject7 Subject8 Subject9 Subject10 Subject11 Subject12 Subject13 Subject14 Subject15 Subject16 Subject17 Subject18 Subject19 Subject20 Subject21 Subject22 Subject23 Subject24 Subject25 Subject26 Subject27 Subject28 Subject29 Subject30 Subject31 Subject32 Subject33 Subject34 Subject35 Subject36 Subject37 Subject38 Subject39 Subject40 Subject41 Subject42 Subject43 Subject44 Subject45 Subject46 Subject47 Subject48 Subject49 Subject50;
# # for n in Subject1
# do
#     mkdir -p "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/${dataset}/$n/osim_results_cleaned"
#     sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/${dataset}/$n/osim_results/* "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/${dataset}/$n/osim_results_cleaned"
# done;

# Copy data to Linux machine
dataset="hamner2013"
sshpass -p 'Stanford!' scp -r /mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/$dataset/* "clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/$dataset/"