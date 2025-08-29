from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_training import DataTraining
from src.datascience.utils import logger
from pathlib import Path

STAGE_NAME="Data Training Stage"

class DataTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_training(self):
        config = ConfigurationManager()
        data_training_config = config.traing_data_training_config()
        data_training = DataTraining(config= data_training_config)
        data_training.train()
        
