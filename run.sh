#!/bin/bash

# Install Python
apt-get update
apt-get install -y python3 python3-pip

# Install required packages from requirements.txt
 pip3 install -r <DEPENDENCIES_FILES>

# Run the Flask application
export FLASK_APP=app
flask run -h 0.0.0.0