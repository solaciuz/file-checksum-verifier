import hashlib
def hash_file(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()