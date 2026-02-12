#!/bin/zsh

# Go to project folder
echo 'Go to project folder'
cd .

echo 'Activate virtual environment'
# Activate virtual environment
source venv/bin/activate

echo 'Run'
# Run the Python app
python textToSpeech.py