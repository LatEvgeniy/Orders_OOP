import os
import Constant_values_for_orders as const
import configparser

class config_service:
    __instance__ = None 

    def __init__(self):      
        if config_service.__instance__ is None: 
            config_service.__instance__ = self 
        else: 
            raise Exception(const.MORE_ONE_INSTANCE_EXCEPTION_MESSAGE) 
       
    def read_config_data(self):
        if(not os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)), const.CONFIG_FILE_NAME))):
            print(const.FILE_NOT_FOUND_MESSAGE % const.CONFIG_FILE_NAME)
            exit(1)
        config_data = configparser.ConfigParser()
        try:     
            config_data.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), const.CONFIG_FILE_NAME ))  
        except:
            print(const.INCORRECT_CONFIG_DATA_MESSAGE % const.CONFIG_FILE_NAME)
            exit(1)    
        self.__parse_config_data(config_data)

    def __parse_config_data(self, config_data):
        try: 
            self.__logger_config = [config_data['LOG']['LEVEL'], config_data['LOG']['LOG_FILE_NAME']]                
            
            database_config = {
                "host": config_data['DATABASE']['DATABASE_HOST'], "user": config_data['DATABASE']['DATABASE_USER'],
                "password": config_data['DATABASE']['DATABASE_PASSWORD'], "database": config_data['DATABASE']['DATABASE_NAME']
                }

            self.__database_config = [database_config, config_data['DATABASE']['TABLE_NAME']]
                   
            self.__order_config = [
                int(config_data['NUMBER_OF_ROWS']['RED_ZONE_ROWS']), 
                int(config_data['NUMBER_OF_ROWS']['GREEN_ZONE_ROWS']),
                int(config_data['NUMBER_OF_ROWS']['BLUE_ZONE_ROWS'])
                ]    
            for number in self.__order_config:
                if (number <= 0):
                    print(const.INCORRECT_CONFIG_ROW_NUMBERS % const.CONFIG_FILE_NAME)
                    exit(1)                    
        except:
            print(const.INCORRECT_OR_NO_CONFIG_DATA_MESSAGE % const.CONFIG_FILE_NAME)
            exit(1)

    def get_database_config(self):
        return self.__database_config 
    
    def get_logger_config(self):
        return self.__logger_config
    
    def get_order_config(self):
        return self.__order_config