#! /bin/bash
curl https://covid.ourworldindata.org/data/ecdc/full_data.csv > ~/datax/covid19/full_data.csv

cd ~/datax/covid19

python3 coronavirus.py US World > today.txt
