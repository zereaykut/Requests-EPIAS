# -*- coding: utf-8 -*-
import requests
import json
import logging

from datetime import date, datetime, timedelta

import warnings
warnings.filterwarnings("ignore")

main_url = "https://seffaflik.epias.com.tr/electricity-service"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', 
                    handlers=[logging.FileHandler("epias_v2.log")])

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

def export_json(data:json, file_name:str) -> None:
    json_object = json.dumps(data, indent=4)
    with open(f"{file_name}.json", "w") as f:
        f.write(json_object)
    logging.info(f"Successfully saved {file_name}.json file")

@logger
def get_mcp(start_date: date, end_date: date) -> json:
    response = requests.post(f"{main_url}/v1/markets/dam/data/mcp", 
                            json={
                                "startDate": f"{start_date}T00:00:00+03:00",
                                "endDate": f"{end_date}T23:00:00+03:00"
                                    })
    response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    data = response.json()
    return data

def main() -> None:
    start_date = date.today() - timedelta(days=7)
    end_date = date.today() - timedelta(days=1)

    logging.info(f"startDate: {start_date}  endDate: {end_date}")

    mcp = get_mcp(start_date, end_date)

    if mcp:
        logging.info("MCP received")
        export_json(mcp, "mcp")
    else:
        logging.error("Failed to receive MCP data")

if __name__ == "__main__":
    main()
