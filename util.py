import hashlib
import zlib
import os
import pickle

def getSHA(path):
    with open(path,'rb') as file:
        data = file.read()
        hash = hashlib.sha256(data).hexdigest()
        return hash

def compress_file(path):
    data = open(path, 'rb').read()
    hash = hashlib.sha256(data).hexdigest()
    c_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    f = open('./.vcs/obj/'+hash, 'wb')
    f.write(c_data)
    f.close()
    perm = oct(os.stat(path).st_mode)[2:]
    fname = os.path.basename(path)
    dic = {}
    dic['filename'] = fname
    dic['permissions'] = perm
    dic['sha256'] = hash
    return dic

def compress_tree(dic):
    data = pickle.dumps(dic)
    hash = hashlib.sha256(data).hexdigest()
    c_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    f = open('./.vcs/objs/'+hash, 'wb')
    f.write(c_data)
    f.close()
    perm = oct(os.stat('./.vcs/obj/'+hash).st_mode)[2:]
    fname = os.path.basename('./.vcs/obj/'+hash)
    dic = {}
    dic['filename'] = fname
    dic['permissions'] = perm
    dic['sha256'] = hash
    return dic

def decompress_file(hash,path):
    data = open('./.vcs/obj/'+hash, 'rb').read()
    data = zlib.decompress(data)
    f = open(path, 'wb')
    f.write(data)
    f.close()

def decompress_tree(hash):
    data = open('./.vcs/obj/'+hash, 'rb').read()
    data = zlib.decompress(data)
    dic = pickle.loads(data)
    return dic
     
def get_head():
    data = open('./.vcs/HEAD', 'rb').read()
    return data

def get_branch(name):
    data = open('./.vcs/branch/'+name).read()
    return data



