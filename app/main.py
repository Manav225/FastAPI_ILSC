from fastapi import FastAPI
from app.models import IPCSingleRequest
from app.utils import clean_section_label, build_ipc_bns_map
import os

app = FastAPI(title="IPC to BNS Mapping API")

CSV_PATH = os.path.join(os.path.dirname(__file__), "data/ipc_bns_dataset_100.csv")
IPC_BNS_MAP = build_ipc_bns_map(CSV_PATH)

@app.post("/map_ipc_to_bns/one")
async def map_ipc_to_bns_one(request: IPCSingleRequest):
    norm_sec = clean_section_label(request.ipc_section)
    mapping = IPC_BNS_MAP.get(norm_sec)
    if mapping:
        return mapping
    else:
        return {"ipc": norm_sec, "ipc_label": "", "ipc_description": "", "bns_section": ""}
