import Constant_values_for_orders as const
from mysql.connector import Error, MySQLConnection

class database_provider_MySQL:
    __instance__ = None 

    def __init__(self):      
        if database_provider_MySQL.__instance__ is None: 
            database_provider_MySQL.__instance__ = self 
        else: 
            raise Exception(const.MORE_ONE_INSTANCE_EXCEPTION_MESSAGE) 
        
    def output_in_MySQL(self, data_for_output, logger, database_config, table_name):
        try:
            connection = MySQLConnection(**database_config)
            all_orders_string_for_output_in_database = str(tuple(data_for_output.get_order(0)))
            for index in range(1, data_for_output.len()):
                all_orders_string_for_output_in_database += ', ' + str(tuple(data_for_output.get_order(index)))
            orders_insert_query = const.INSTER_QUERY % table_name + all_orders_string_for_output_in_database
            connection._execute_query(orders_insert_query)
            connection.commit()       
            logger.info(const.INFO_DATA_INSERTED_INTO_DATABASE)
        except Error:
            logger.critical(Error)
        finally:
            connection.close()