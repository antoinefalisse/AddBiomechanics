# sed -i 's/\r//' copy_data.sh


# for n in subject2 subject3 subject4 subject5 subject6 subject7 subject8 subject9 subject10 subject11;
# do
# 	if [ ! -d "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/opencap_dataset/$n/_results.json" ]; then	
# 		sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/opencap_dataset/$n/_results.json "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/opencap_dataset/$n/"
# 		sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/opencap_dataset/$n/osim_results "/mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/opencap_dataset/$n/"
# 	fi	
# done;

# dataset="hamner2013"
# for n in subject01 subject02 subject03 subject04 subject08 subject10 subject11 subject17 subject19 subject20;
# # for n in Subject1
# do
#     mkdir -p "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/${dataset}/$n/osim_results_cleaned"
#     sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/${dataset}/$n/osim_results/* "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/${dataset}/$n/osim_results_cleaned"
# done;

# dataset="hamner2013"
# for n in subject01 #subject02 subject03 subject04 subject08 subject10 subject11 subject17 subject19 subject20;
# # for n in Subject1
# do
#     mkdir -p "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/${dataset}/Processed_raja_2/$n/osim_results_cleaned"
#     sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/${dataset}/$n/osim_results/* "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/${dataset}/Processed_raja_2/$n/osim_results_cleaned"
# done;

# dataset="karate_dataset"
# for n in B0369-S01 #subject02 subject03 subject04 subject08 subject10 subject11 subject17 subject19 subject20;
# # for n in Subject1
# do
#     mkdir -p "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/${dataset}/test/$n/osim_results"
#     sshpass -p 'Stanford!' scp -r clarkadmin@171.65.102.146:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/${dataset}/$n/osim_results/* "/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/${dataset}/test/$n/osim_results"
# done;

dataset="totalcapture"
for n in s1 s2 #subject02 subject03 subject04 subject08 subject10 subject11 subject17 subject19 subject20;
# for n in Subject1
do
    mkdir -p "/mnt/g/My Drive/Projects/TomVW_IMU/TotalCapture/trc/$n/osim_results"
    sshpass -p 'Stanford!1' scp -r clarkadmin@171.65.102.45:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/${dataset}/$n/osim_results/* "/mnt/g/My Drive/Projects/TomVW_IMU/TotalCapture/trc/$n/osim_results"
done;


# # # Copy data to Linux machine
# dataset="totalcapture"
# sshpass -p 'Stanford!1' scp -r /mnt/c/Users/antoi/Documents/MyRepositories/AddBiomechanics/server/data/$dataset/* "clarkadmin@171.65.102.45:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/$dataset/"