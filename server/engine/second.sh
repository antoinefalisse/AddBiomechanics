#!/bin/bash
sshpass -p 'Stanford!' scp -r clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cycling_dataset/P020/osim_results '/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cycling_anthony_cleaned/P020'

sshpass -p 'Stanford!' scp clarkadmin@171.65.103.222:Documents/MyRepositories_Antoine/AddBiomechanics/server/data/cycling_dataset/P020/_results.json '/mnt/g/My Drive/Projects/openpose-augmenter/Data_opensim/cycling_anthony_cleaned/P020'
