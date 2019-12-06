#! /bin/bash

# Get Leeds Sport Pose dataset
wget https://sam.johnson.io/research/lsp_dataset.zip
unzip lsp_dataset.zip
rm lsp_dataset.zip

mkdir lsp
mv images lsp
mv joints.mat lsp
mv visualized lsp
mv README.txt lsp