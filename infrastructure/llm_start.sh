#!/bin/bash

# running with https://hub.docker.com/r/pytorch/pytorch/ docker image

# Update and Upgrade Ubuntu System
sudo apt update && sudo apt upgrade -y

# Install Anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
bash Anaconda3-2020.11-Linux-x86_64.sh -b -p $HOME/anaconda3
echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

conda init bash
source ~/.bashrc

# Create a conda environment for deep learning
conda create --name deep-learning python=3.11 -y
conda activate deep-learning

# Fine tunning from source https://mer.vin/2024/01/finetuning-open-source-llm-for-beginners/
# pip install pandas datasets ludwig "ludwig[llm]" matplotlib peft auto-gptq optimum
