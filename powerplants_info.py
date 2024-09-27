# -*- coding: utf-8 -*-
from src.utils import save_json, get_tgt
from src.services import EpiasTransparencyerServices

def main() -> None:
    tgt = get_tgt()

    epias_services = EpiasTransparencyerServices()

    pps_info = epias_services.info_powerplant_list(tgt)
    
    if pps_info.status_code in [200, 201]:
        save_json(pps_info.json(), "data/powerplants_info.json")

if __name__ == "__main__":
    main()

