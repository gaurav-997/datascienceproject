# this is for generic project structure ( here we will make all required files and directories )
import os
from pathlib import Path
import logging

project_name = "datascience"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",  # here we define the constructor bcz with this we can import this project anywhere 
    f"src/{project_name}/components/__init__.py",   # this will be used for different stages of pipeline
    f"src/{project_name}/utils/__init__.py",  # this is used for any common functiontanility ( like logging )
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "DockerFile",
    "requirments.txt",
    "setup.py",
    "resarch/resarch.ipynb",
    "templates/index.html",
    "app.py"
]
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir,filename = os.path.split(file_path)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory {filedir} for file:{filename}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0) :
        with open(file_path,"w") as f:
            pass
            logging.info(f"creating empty file:{file_path}")
    else:
        logging.info(f"file : {file_path} already exists")