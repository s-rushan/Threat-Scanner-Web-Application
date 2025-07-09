import hashlib, itertools
from config import VT_KEYS, KOODOUS_KEYS, URLSCAN_KEYS  # <-- Add URLSCAN_KEYS

# API key cycles
vt_key_cycle = itertools.cycle(VT_KEYS)
koodous_key_cycle = itertools.cycle(KOODOUS_KEYS)
urlscan_key_cycle = itertools.cycle(URLSCAN_KEYS)  # <-- Add this line

# Hash function
def get_sha256(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

# Key rotation functions
def get_vt_key(): return next(vt_key_cycle)
def get_koodous_key(): return next(koodous_key_cycle)
def get_urlscan_key(): return next(urlscan_key_cycle)  # <-- Add this function
