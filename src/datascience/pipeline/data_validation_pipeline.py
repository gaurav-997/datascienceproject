from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation
from src.datascience.utils import logger

STAGE_NAME="Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

# configuration manager has data ( as configuration manager is the combination of config.yaml,schema.yaml and entiy) and componets has compare core logic 
# so we will create both class object and call them 
    def initiate_data_validation(self):
        config=ConfigurationManager()  # creating object for calling class of configuration 
        data_validation_config=config.validate_data_validation_config()  # calling the function 
        data_validation = DataValidation(config=data_validation_config)   # making object for callin DataValidation calss from components it has compare logic 
        data_validation.validate_all_columns() # components calling function


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e