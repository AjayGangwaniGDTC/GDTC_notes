'''This file is used to load the data from the api into mongoDB database'''

import mysql.connector
from .config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, logger
from .decorators import log_phase

@log_phase("Load to MySQL")
def load_to_mysql(data):
    '''function to connect to the database and then inserting the values'''
    #Connecting to the database
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = conn.cursor()
    #Traversing through the data and and inserting each value to the sql database
    for entry in data:
        sql = """
        INSERT INTO powerpulse (period, stateId, stateDescription, producertypeid, producerTypeDescription, energysourceid, energySourceDescription)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            entry.get('period'),
            entry.get('stateId'),
            entry.get('stateDescription'),
            entry.get('producertypeid'),
            entry.get('producerTypeDescription'),
            entry.get('energysourceid'),
            entry.get('energySourceDescription')
        )
        cursor.execute(sql, values)
    conn.commit()
    logger.info("Inserted %s records into MySQL database.", len(data))
    cursor.close()
    conn.close()
