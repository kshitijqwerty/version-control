import hashlib
import zlib
import os
import pickle

def getSHA(path):
    with open(path,'rb') as file:
        data = file.read()
        hash = hashlib.sha256(data).hexdigest()
        return hash

def compress(path):
    data = open(path, 'rb').read()
    hash = hashlib.sha256(data).hexdigest()
    c_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    f = open('./git/objs/'+os.path.pathsep+hash, 'wb')
    f.write(c_data)
    f.close()
    perm = oct(os.stat(path).st_mode)[2:]
    fname = os.path.basename(path)
    dic = {}
    dic['filename'] = fname
    dic['permissions'] = perm
    dic['sha256'] = hash
    return dic

def compress(dic):
    data = pickle.dumps(dic)
    hash = hashlib.sha256(data).hexdigest()
    c_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    f = open('./.vcs/objs/'+hash, 'wb')
    f.write(c_data)
    f.close()
    perm = oct(os.stat('./.vcs/objs/'+hash).st_mode)[2:]
    fname = os.path.basename('./.vcs/objs/'+hash)
    dic = {}
    dic['filename'] = fname
    dic['permissions'] = perm
    dic['sha256'] = hash
    return dic

def decompress(hash,path):
    data = open('./git/objs/'+hash, 'rb').read()
    data = zlib.decompress(data)
    f = open(path, 'wb')
    f.write(data)
    f.close()

def decompress(hash):
    data = open('./git/objs/'+hash, 'rb').read()
    data = zlib.decompress(data)
    dic = pickle.loads(data)
    return dic
def get_head():
