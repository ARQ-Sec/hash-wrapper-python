import hashlib as digest_lib

def sign(payload: bytes) -> str:
    return digest_lib.md5(payload).hexdigest()
