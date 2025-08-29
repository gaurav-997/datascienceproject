import os
from src.datascience.utils import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):  # we are getting this from entity 
        self.config = config
        
        """ we can add different data trnasformation technique such as Scalar , PCA and all 
        we can also perform all EDA in ML cycle here before passing this data to model training
        here data is already cleaned so we will go with train test split """
        
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path) # getting this data from entity
        
        # spliting the data into training and test sets ( 0.75,0.25 ) split 
        train,test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv") ,index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
        
        logger.info("splited data into training and test set ")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)