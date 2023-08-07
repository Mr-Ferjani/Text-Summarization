'''
Install tabnine extension
CI/CD: 
'''

import os
from pathlib import Path
import logging

#logging configuration
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github.com/workflows/.gitkeep",   # Responsible for CI/CD
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componenets/__init__.py", # the constructor is added components folder is it can be considered as a local package where you can import from
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    #convert paths to the format set in the list_of_files
    #This would detect the os used and covert path accordingly
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath) 

    if file_dir != "":
        os.makedirs(file_dir, exist_ok= True)
        logging.info(f"Creating Directory: {file_dir} for the file {filename}")
    
    #If file doesn't exist, create it
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f" Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} is already created")
