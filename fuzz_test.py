# fuzz_test.py
import hashlib
import pytest
from hypothesis import given, settings, strategies as st

# Helper function to simulate the server's hashing behavior
def server_hash(data: bytes) -> bytes:
    hash_obj = hashlib.sha256()
    hash_obj.update(data)
    return hash_obj.digest()

# Helper function to simulate the client's hashing behavior
def client_hash(data: bytes) -> bytes:
    hash_obj = hashlib.sha256()
    hash_obj.update(data)
    return hash_obj.digest()

@settings(max_examples=1000)
@given(st.binary(min_size=1, max_size=4096))
def test_hashes(data: bytes):
    server_digest = server_hash(data)
    client_digest = client_hash(data)
    assert server_digest == client_digest
