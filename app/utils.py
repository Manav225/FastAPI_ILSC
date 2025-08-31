import pandas as pd
import re

def clean_section_label(label: str) -> str:
    # Normalization logic
    if not isinstance(label, str):
        return str(label)
    m = re.search(r"Section\s+(\d+)", label, flags=re.IGNORECASE)
    if m:
        return m.group(1)
    m2 = re.search(r"IPC[_\s-]*(\d+)", label, flags=re.IGNORECASE)
    if m2:
        return m2.group(1)
    m3 = re.search(r"\b(\d{1,4})\b", label)
    if m3:
        return m3.group(1)
    return re.sub(r"[^0-9A-Za-z]+", "_", label).strip("_")[:20]

def build_ipc_bns_map(csv_path: str):
    df = pd.read_csv(csv_path)
    ipc2bns = {}
    for _, row in df.iterrows():
        ipc_raw = str(row["IPC"]) if not pd.isna(row["IPC"]) else ""
        if not ipc_raw:
            continue
        m = re.search(r"(\d+)", ipc_raw)
        if not m:
            continue
        ipc_num = m.group(1)
        ipc2bns[ipc_num] = {
            "ipc": ipc_num,
            "ipc_label": ipc_raw,
            "ipc_description": str(row["IPC description"]) if not pd.isna(row["IPC description"]) else "",
            "bns_section": str(row["BNS"]) if not pd.isna(row["BNS"]) else ""
        }
    return ipc2bns
