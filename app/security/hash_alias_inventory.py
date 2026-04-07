import hashlib as digest_lib

def supported_algorithms() -> tuple[str, ...]:
    return ('sha256', digest_lib.sha512().name)
