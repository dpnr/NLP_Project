#!/bin/bash 
source activate py3
python nlpProject.py testset1/testset1-input.txt
perl score-ie.pl testR.txt testset1/testset1-anskeys.txt
