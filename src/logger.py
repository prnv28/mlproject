import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,

)

if __name__ == "__main__":
    logging.info("Logging has been set up successfully.")
    logging.error("This is an error message for testing purposes.")
    logging.warning("This is a warning message for testing purposes.")
    logging.debug("This is a debug message for testing purposes.")
    logging.critical("This is a critical message for testing purposes.")