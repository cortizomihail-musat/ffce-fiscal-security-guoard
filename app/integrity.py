import hashlib
import json
import time
from pathlib import Path

# audit log stored next to this module
LOG_FILE = Path(__file__).resolve().parent / "audit_log.jsonl"


def _hash(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def append_event(event: dict) -> str:
    """
    Append-only audit log with hash chaining.
    """
    timestamp = time.time()

    prev_hash = "GENESIS"
    if LOG_FILE.exists():
        with LOG_FILE.open("r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                prev_hash = json.loads(lines[-1])["entry_hash"]

    entry = {
        "timestamp": timestamp,
        "event": event,
        "prev_hash": prev_hash,
    }

    entry_hash = _hash(json.dumps(entry, sort_keys=True))
    entry["entry_hash"] = entry_hash

    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    return entry_hash


def verify_log() -> bool:
    """
    Verify integrity of the audit log.
    """
    if not LOG_FILE.exists():
        return True

    prev_hash = "GENESIS"
    with LOG_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)

            check = {
                "timestamp": entry["timestamp"],
                "event": entry["event"],
                "prev_hash": entry["prev_hash"],
            }

            if _hash(json.dumps(check, sort_keys=True)) != entry["entry_hash"]:
                return False

            if entry["prev_hash"] != prev_hash:
                return False

            prev_hash = entry["entry_hash"]

    return True
