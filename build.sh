#!/bin/bash
set -e

# Install Python 3.11
yum install -y python3.11 python3.11-pip

# Install dependencies
pip3.11 install -r requirements.txt

# Run migrations
python3.11 manage.py migrate

# Create superuser
python3.11 manage.py create_superuser_on_deploy

# Collect static files
python3.11 manage.py collectstatic --noinput --clear