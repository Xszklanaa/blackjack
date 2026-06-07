import time, hashlib

def crypto_shuffle(deck, seed=None):
    if seed is None:
        seed = str(time.time_ns())
    n = len(deck)
    current_seed = seed
    for i in range(n-1, 0,-1):
        hasher = hashlib.sha256(current_seed.encode("UTF-8"))
        hex_hash = hasher.hexdigest()
        hash_int = int(hex_hash, 16)
        j = hash_int % i
        deck[i], deck[j] = deck[j], deck[i]
        current_seed = hex_hash
    return seed