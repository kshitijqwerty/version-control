import hashlib
import zlib
import os
import pickle
import shelve
from constants import OBJ_DIR, INDEX_PATH, HEAD_PATH, BRANCH_DIR


class Entry:
    def __init__(self, file_path, sha, stat, modified=False):
        self.file_path = file_path
        self.sha = sha
        self.stat = stat
        self.modified = modified


def get_sha(path):
    with open(path, 'rb') as file:
        data = file.read()
        hash = hashlib.sha1(data).hexdigest()
        return hash


def compress_file(path):
    data = open(path, 'rb').read()
    hash = hashlib.sha1(data).hexdigest()
    c_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    f = open(os.path.join(OBJ_DIR, hash), 'wb')
    f.write(c_data)
    f.close()
    perm = oct(os.stat(path).st_mode)[2:]
    fname = os.path.basename(path)
    dic = {}
    dic['filename'] = fname
    dic['permissions'] = perm
    dic['sha1'] = hash
    return dic


def compress_tree(dic):
    data = pickle.dumps(dic)
    hash = hashlib.sha1(data).hexdigest()
    c_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    f = open(os.path.join(OBJ_DIR, hash), 'wb')
    f.write(c_data)
    f.close()
    perm = oct(os.stat(os.path.join(OBJ_DIR, hash)).st_mode)[2:]
    fname = os.path.basename(os.path.join(OBJ_DIR, hash))
    dic = {}
    dic['filename'] = fname
    dic['permissions'] = perm
    dic['sha1'] = hash
    return dic


def decompress_file(hash, path):
    data = open(os.path.join(OBJ_DIR, hash), 'rb').read()
    data = zlib.decompress(data)
    f = open(path, 'wb')
    f.write(data)
    f.close()


def decompress_tree(hash):
    data = open(os.path.join(OBJ_DIR, hash), 'rb').read()
    data = zlib.decompress(data)
    dic = pickle.loads(data)
    return dic


def get_head():
    data = open(HEAD_PATH).read()
    print("get_head: ", data)
    return data


def get_branch(name):
    print(name)
    data = open(os.path.join(BRANCH_DIR, name)).read()
    print(data)
    return data


def get_last_commit_tree():
    return get_branch(get_head())


def get_modified_entries():
    """
    :return: list of entries that are new or modified in the index file
    """
    modified_entries = []
    with shelve.open(INDEX_PATH) as index:
        for key in index.keys():
            print(key)
            entry = index[key]
            if entry.modified:
                modified_entries.append(entry)
    return modified_entries


def get_sha_from_index(filepath):
    with shelve.open(INDEX_PATH) as index:
        try:
            sha = index[filepath].sha
            return sha
        except KeyError:
            return
