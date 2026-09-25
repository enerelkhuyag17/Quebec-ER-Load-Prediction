"""
Connector for ER (emergency room) load data — sante.handled.tools
Free JSON API, no key, no rate limit, cached ~120s server-side.
Data ultimately comes from MSSS (Quebec health ministry) open data,
republished under CC-BY 4.0. Cite MSSS as the source if you publish results.
"""
from __future__ import annotations
import requests
from typing import Optional

BASE_URL = "https://sante.handled.tools/api"


def get_facilities() -> list[dict]:
    """Directory of all ~120 ERs: name, establishment, region, address, coordinates, id."""
    r = requests.get(f"{BASE_URL}/facilities", timeout=15)
    r.raise_for_status()
    facilities = r.json()["rows"]
    facilities_dict = {item["name"]: item for item in facilities}
    return facilities


def find_facility(name_contains: str) -> list[dict]:
    """Case-insensitive substring search over facility names, e.g. 'Honoré-Mercier'."""
    needle = name_contains.lower()
    return [f for f in get_facilities() if needle in f.get("name", "").lower()]


def get_current_status(facility_id: Optional[str] = None) -> list[dict] | dict:
    """
    Current reading for all ERs (stretchers, present, waiting, avg stay, occupancy).
    If facility_id is given, returns just that facility's current reading.
    """
    r = requests.get(f"{BASE_URL}/now", timeout=15)
    r.raise_for_status()
    data = r.json()["rows"]
    if facility_id is None:
        return data
    match = [d for d in data if str(d.get("id")) == str(facility_id)]
    return match[0] if match else {}


def get_facility_history(facility_id: str) -> list[dict]:
    """
    One ER's full hourly history (archive starts 2026-08-10).
    facility_id must be the MSSS permit number, as returned by get_facilities()/find_facility().
    """
    r = requests.get(f"{BASE_URL}/facility/{facility_id}/history", timeout=30)
    r.raise_for_status()
    return r.json()["rows"]


if __name__ == "__main__":
    hospital_name = "Hôpital général du Lakeshore"  # change to your target hospital
    matches = find_facility(hospital_name)
    if not matches:
        print(f"No facility matching '{hospital_name}'")
    else:
        facility = matches[0]
        print("Facility:", facility)
        current = get_current_status(facility["id"])
        print("Current reading:", current)
        history = get_facility_history(facility["id"])
        print(f"History points: {len(history)} (first: {history[0] if history else None})")
