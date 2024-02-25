from logging_and_config_and_database.config_service import config_service

class config_service_decorator:
   @staticmethod 
   def get_instance(): 
       if not config_service.__instance__: 
           config_service() 
       return config_service.__instance__ 