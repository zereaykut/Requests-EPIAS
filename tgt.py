# -*- coding: utf-8 -*-
from src.utils import save_json
from src.services import EpiasTransparencyerServices as epias_services

def main() -> None:
    tgt = epias_services.tgt()
    if tgt.status_code in [200, 201]:
        save_json(tgt.json(), "data/tgt.json")

if __name__ == "__main__":
    main()

