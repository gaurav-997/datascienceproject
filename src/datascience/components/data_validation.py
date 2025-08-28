import os
import pandas as pd
from src.datascience.utils import logger
from src.datascience.entity.config_entity import DataValidationConfig

# read the data set and compare it with schema and status to true for correct data 
class DataValidation:
    def __init__(self,config:DataValidationConfig):  # passing class DataValidationConfig from entity as input 
        self.config=config  # internal class variable 
        
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
# read the data and get the column names 
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)

            all_schema = self.config.all_schema.keys()  # this we are getting form configuration manger 

# get the column name from data and schema compare both
            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation status {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation status {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e