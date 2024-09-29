import os
import logging
from datetime import date

os.makedirs(f"logs/", exist_ok=True)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler(f"logs/{date.today()}.log")])

def logger(func):
    def wrapper(*args, **kwargs):
        start_date, end_date = args
        logging.info(f"Running {func.__name__} function from {start_date} to {end_date}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Successfully run {func.__name__} function")
            return result
        except requests.exceptions.RequestException as e:
            logging.error(f"Error running {func.__name__} function: {e}")
            return None
    return wrapper