# -*- coding: utf-8 -*-
import logging
from src.utils import save_json
from src.services import EpiasTransparencyerServices as epias_services

def main() -> None:
    tgt = epias_services.tgt()
    if tgt.status_code in [200, 201]:
        save_json(tgt.json(), "data/tgt.json")
        logging.error(f"TGT successfull, status code: {tgt.status_code}")
    else:
        logging.error(f"TGT error: {tgt.text}")
    

if __name__ == "__main__":
    main()

