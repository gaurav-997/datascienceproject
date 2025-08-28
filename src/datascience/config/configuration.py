from src.datascience.constants import *
from src.datascience.utils.common import read_yaml,create_directories

from src.datascience.entity.config_entity import (DataIngestionConfig,DataValidationConfig)

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


#  here we will interlink the config.yaml and entity (data types )
    def get_data_ingestion_config(self)-> DataIngestionConfig:   #  DataIngestionConfig is form config_entity dataclass
        config=self.config.data_ingestion   # this is the key we are reading from config.yaml 
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir

        )
        return data_ingestion_config
    
    def validate_data_validation_config(self) ->DataValidationConfig:
        config= self.config.data_validation    # self.filename.key_value
        schema = self.schema.COLUMNS   # schema is the all column names 
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )
        return data_validation_config