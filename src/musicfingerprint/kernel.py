
from collections import defaultdict
def _block(rec):
    nm = str(rec.get("name", "")).lower().replace(" ", "")
    return nm[:6] or "x"
def process(record):
    return {"block_key": _block(record)}
def reduce(records):
    g = defaultdict(set)
    for r in records:
        g[r["block_key"]].add(str(r.get("id")))
    for r in records:
        members = sorted(g[r["block_key"]])
        r["cluster_size"] = len(members)
        r["cluster_representative"] = members[0] if members else r.get("id")
    return records
