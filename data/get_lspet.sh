#! /bin/bash

# Get Leeds Sport Pose Extended dataset
cd data

wget https://sam.johnson.io/research/lspet_dataset.zip
unzip lspet_dataset.zip
rm lspet_dataset.zip

mkdir lspet
mv images lspet
mv joints.mat lspet
mv README.txt lspet

wget https://sam.johnson.io/research/lspet_dataset_visualized.zip
unzip lspet_dataset_visualized.zip
rm lspet_dataset_visualized.zip
mv visualized lspet

