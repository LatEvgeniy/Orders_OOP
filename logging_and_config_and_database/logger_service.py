import os
import logging
import Constant_values_for_orders as const

class logger_service:
    __instance__ = None 

    def __init__(self):      
        if logger_service.__instance__ is None: 
            logger_service.__instance__ = self 
        else: 
            raise Exception(const.MORE_ONE_INSTANCE_EXCEPTION_MESSAGE) 

    def get_logger(self, logging_level, logger_output_file_name):  
        logger = logging.getLogger(__name__)  
        try:
            logger.setLevel(logging_level)
        except:
            print(const.BAD_LOGGING_LEVEL_MESSAGE)
            exit(1)
        file_handler = logging.FileHandler(os.path.join(os.path.dirname(os.path.realpath(__file__)), logger_output_file_name))
        file_handler.setFormatter(logging.Formatter(const.LOGGER_OUTPUT_FORMAT))
        logger.addHandler(file_handler)
        return logger