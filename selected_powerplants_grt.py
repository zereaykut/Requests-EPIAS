# -*- coding: utf-8 -*-
import os
import json
import time
import logging
from datetime import datetime, date, timedelta
from src.utils import get_selected_powerplants, get_tgt, save_json
from src.services import EpiasTransparencyerServices

def main() -> None:
    start_date = str(date.today() - timedelta(days=7))
    end_date = str(date.today() - timedelta(days=1))

    # start_date = "2024-08-20"
    # end_date = "2024-08-21"

    logging.info(f"Start Date: {start_date}  End Date: {end_date}")

    tgt = get_tgt()
    epias_services = EpiasTransparencyerServices()

    pps_info = get_selected_powerplants()

    os.makedirs("data/selected_powerplants_data/", exist_ok=True)

    for index, pp_info in enumerate(pps_info):
        grt_id = pp_info.get("id")
        name = pp_info.get("name")
        
        print(f"{str(index).zfill(3)} - {str(grt_id).zfill(4)} - Santral: {name}")
        
        if (grt_id is not None):

            pp_grt = epias_services.grt(tgt, start_date, end_date, grt_id)
            if pp_grt.status_code in [200, 201]:
                save_json(pp_grt.json(), f"data/selected_powerplants_data/{name}_{grt_id}.json")
                logging.info(f"Successful Response for index: {index} & grt_id: {grt_id} & name: {name}")
            else:
                save_json({"Error": pp_grt.text}, f"data/selected_powerplants_data/error_{name}_{grt_id}.json")
                logging.error(f"Response Error for index: {index} & grt_id: {grt_id} & name: {name}")
        else:
            logging.error(f"grt_id is none for index: {index} & name: {name}")
        time.sleep(2)

if __name__ == "__main__":
    main()

