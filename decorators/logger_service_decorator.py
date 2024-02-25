from logging_and_config_and_database.logger_service import logger_service

class logger_service_decorator:
   @staticmethod 
   def get_instance(): 
       if not logger_service.__instance__: 
           logger_service() 
       return logger_service.__instance__ 