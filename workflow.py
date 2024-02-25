import Constant_values_for_orders as const
from builders_and_director.order_history_record_builder import order_history_record_builder
from decorators.config_service_decorator import config_service_decorator
from decorators.logger_service_decorator import logger_service_decorator
# from decorators.database_provider_MySQL_decorator import database_provider_MySQL_decorator

class workflow:
    def workflow():
        config_service = config_service_decorator.get_instance()
        config_service.read_config_data()

        logging_level, logging_file_name = config_service.get_logger_config()
        logger_service = logger_service_decorator.get_instance()
        logger = logger_service.get_logger(logging_level, logging_file_name)

        red_row_count, green_row_count, blue_row_count = config_service.get_order_config()    
        logger.info(const.INFO_TASK_MESSAGE, red_row_count, green_row_count, blue_row_count) 
        all_history_records_builder = order_history_record_builder(red_row_count, green_row_count, blue_row_count)
        all_history_records = all_history_records_builder.get_all_orders()
        logger.info(const.INFO_TABLE_DONE_MESSAGE)  

        for order in all_history_records:
            print(tuple(order))

        database_config, table_name = config_service.get_database_config()
        
        # database_provider_MySQL = database_provider_MySQL_decorator.get_instance()
        # database_provider_MySQL.output_in_MySQL(all_history_records, logger, database_config, table_name)
        
workflow.workflow()