#!/bin/bash
git clone https://github.com/icoxfog417/number_recognizer /root/number_recognizer
source /opt/miniconda3/envs/ml_env/bin/activate ml_env
cd /root/number_recognizer/machines/number_recognizer
ipython notebook --profile=nbserver &
cd /root/number_recognizer/
python server.py
