import os
import sys # import this for customexception
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # use this create class variables in short


#inputs are given under the dataingestionconfig
# Dataclass - Decorator is amazing if we use the decorator, you don't have the use the init method-
#-having decorator you can directly define the class variables. 
# you can define the configentity as different file, but having in data ingestion file is easier to understand

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    
#If we define functions other than variables in class then use __init__ method
class DataIngestion:
    def __init__(self):
        # creating new variable called ingestion_config that will consist of three values listed above
        # as soon as calling DataIngestion class that will automatically execute the three variables listed
        self.ingestion_config = DataIngestionConfig()
    # Initiate_data_ingestion function will read the file from database
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')
            
            #in order to create the path, we need to use the os.makedirs
            #Inside the makedirs you have to combine the directory pathname(os.path.dirname)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            # to save this file as raw data path
            df.to_csv(self.ingestion_config.raw_data_path,index=False, header=True)
            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Ingestion of the data is completed')
            
            return (
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
                
            )
            
        except Exception as e:
            logging.info("Wrong error")
            raise CustomException(e, sys)

if __name__ =='__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion