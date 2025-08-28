import os
import yaml
from src.datascience.utils import logger
import json
import joblib  # used to save models in joblib format 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
#  ensure_anotation will try to match the data type otherwise it will throw error , e.g without ensure anotation 3*"2" = '222' 
# but wiht ensure enotation both should be interger 


def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """ here we read the yaml file if file is empty then return empty file value error else return config box type"""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"{yaml_file} content loaded successfully")
            return ConfigBox(content) # here we load yaml file as dict if some error will be their it will be handled by configBox ( its for our easyness )
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations 
def create_directories(path_to_directories: list , verbose = True):
    """ from the list of path of directories create directories if already present ignore it """
    try:
        for path in path_to_directories:
            os.makedirs(path,exist_ok=True)
            if verbose:
                logger.info(f"created dir at path {path}")
    except Exception as e:
        raise e
   
#  save and laod json  
@ensure_annotations 
def save_json(path: Path, data: dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"data is saved into {path}")
    
@ensure_annotations 
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"data is loaded successfully in path {path}")
    return ConfigBox(content)

#  save and load binary 
@ensure_annotations 
def save_bin(data: Any,path: Path):
    """ save the binary file , data to be saved as binary file in the given path"""
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file is saved into {path}")
    
@ensure_annotations 
def load_bin(path:Path) -> Any:
    "load the binary data and return any data stored in the file  "
    data = joblib.load(path)
    logger.info(f"Binary data is loaded successfully in {path}")
    return data