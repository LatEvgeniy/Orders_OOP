from logging_and_config_and_database.database_provider_MySQL import database_provider_MySQL

class database_provider_MySQL_decorator:
   @staticmethod 
   def get_instance(): 
       if not database_provider_MySQL.__instance__: 
           database_provider_MySQL() 
       return database_provider_MySQL.__instance__ 