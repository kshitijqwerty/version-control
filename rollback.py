from util import get_last_commit_hash
from checkout import checkout

def rollback():
    checkout(get_last_commit_hash())