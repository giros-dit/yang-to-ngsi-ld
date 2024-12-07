import sys
import os
import logging
import logging.config
import psycopg2
import time
import yaml
from datetime import datetime, timedelta
from check_client import NGSILDHealthInfoClient

log_config_path = os.path.join('config', 'log.yaml')
#assuming the log config file name is log.yaml
with open(log_config_path, 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

#read the file to logging config
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

ngsi_ld_health_info_api = NGSILDHealthInfoClient(
    url="http://scorpio:9090",
    headers={"Accept": "application/json"},
    context="http://context-catalog:8080/context.jsonld")

# Check if Scorpio API is up
ngsi_ld_health_info_api.check_scorpio_status()

# Check Scorpio build info
ngsi_ld_health_info_api.check_scorpio_info()

# DB connection
connection = psycopg2.connect(
    host="postgres",        
    port="5432",
    database="ngb",
    user="ngb",      
    password="ngb"
)

# Create cursor for making DB queries
cursor = connection.cursor()

try:
    # Run query each minute
    while True:
        now = datetime.now()
        now_datetime =now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        logger.info("Date and time right now: " + now_datetime)
        filtered_datetime = now - timedelta(minutes=int(sys.argv[2]))
        filtered_datetime_str = filtered_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        logger.info("Date and time " + sys.argv[2] + " minutes before: " + filtered_datetime_str)

        # SELECT SQL Query
        cursor.execute("SELECT * FROM entity;")
        connection.commit()

        logger.info("Old registries...")

        # Obtaining registry results
        registros = cursor.fetchall()

        '''
         # Print results
        for registro in registros:
            logger.info(registro)
        '''

        # Cascade delete OF NGSI-LD entities:
        cursor.execute("DELETE FROM temporalentityattrinstance WHERE modifiedat < '" + str(filtered_datetime_str) +"';")
        connection.commit()

        cursor.execute("DELETE FROM temporalentity WHERE modifiedat < '" + str(filtered_datetime_str) +"';")
        connection.commit()

        cursor.execute("DELETE FROM entity WHERE modifiedat < '" + str(filtered_datetime_str) +"';")
        connection.commit()

        cursor.execute("SELECT * FROM entity;")
        connection.commit()

        logger.info("Current registries...")
        
        # Obtaining registry results
        registros = cursor.fetchall()

        '''
        # Print results
        for registro in registros:
            logger.info(registro)
        '''

        time.sleep(int(sys.argv[1]))

except Exception as e:
    logger.exception("Error executing query:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()