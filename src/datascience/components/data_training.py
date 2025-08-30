import os
from src.datascience.utils import logger
from sklearn.linear_model import ElasticNet
import joblib
import pandas as pd
from src.datascience.entity.config_entity import DataTrainingConfig

# read the data and train it using trian test split 
class DataTraining:
    def __init__(self,config:DataTrainingConfig):  # we are getting this from configuration
        self.config = config
        
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)  # train_data_path is comming from self.config and which is present in DataTrainingConfig
        test_data = pd.read_csv(self.config.train_data_path)
        
        train_x = train_data.drop([self.config.target_column],axis=1)
        test_x = test_data.drop([self.config.target_column],axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]
        
        lr = ElasticNet(alpha= self.config.alpha ,l1_ratio= self.config.l1_ratio,random_state= 42)
        lr.fit(train_x,train_y)
        
        #  after training dump the file in joblib
        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))