#!/bin/bash

# Cleaning existing reports and creating the folder
rm -rf pymetrics/
mkdir pymetrics
rm -rf pylint/
mkdir pylint

# Metrics for Usuarios module
echo "Generating metrics for Usuarios  module..."
pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric usuarios/views.py usuarios/models.py > pymetrics/usuarios.txt
pylint -d C0103,E1101 -f html usuarios/ > pylint/Usuarios.html

# Metrics for frontend module
#echo "Generating metrics for frontend module..."
#pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric frontend/views.py frontend/models.py > pymetrics/frontend.txt
#pylint -d C0103,E1101 -f html frontend/ > pylint/frontend.html

# Metrics for Photo module
#echo "Generating metrics for Photo module..."
#pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric Photo/views.py Photo/models.py > pymetrics/Photo.txt
#pylint -d C0103,E1101 -f html Photo/ > pylint/Photo.html

# Metrics for Message module
#echo "Generating metrics for Message module..."
#pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric Message/views.py Message/models.py > pymetrics/Message.txt
#pylint -d C0103,E1101 -f html Message/ > pylint/Message.html

# Metrics for Micropost module
#echo "Generating metrics for Micropost module..."
#pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric Micropost/views.py Micropost/models.py > pymetrics/Micropost.txt
#pylint -d C0103,E1101 -f html Micropost/ > pylint/Micropost.html

# Cleaning temp files...
echo "Cleaning temp files..."
rm -f metricData.*

