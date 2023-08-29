from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys


if __name__ == "__main__":
    logging.info("Execution Started")


    try:
        a = 1/0
    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e, sys)