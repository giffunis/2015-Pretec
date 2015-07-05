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

# Metrics for Micropost module
echo "Generating metrics for Microposts module..."
pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric microposts/views.py microposts/models.py > pymetrics/microposts.txt
pylint -d C0103,E1101 -f html microposts/ > pylint/microposts.html

# Cleaning temp files...
echo "Cleaning temp files..."
rm -f metricData.*
