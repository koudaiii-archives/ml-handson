#!/bin/bash
git clone https://github.com/icoxfog417/scikit-learn-notebook.git /root/scikit-learn-notebook
source /opt/miniconda3/envs/ml_env/bin/activate ml_env
cd /root/scikit-learn-notebook
ipython notebook --profile=nbserver 
