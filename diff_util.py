""" display difference between a file(indexed) and another file(not indexed) """

from hashlib import sha256 
import difflib
import pickle
import zlib
import os

def diff_strstr(str1, str2):
    """ 
        Input:
        2 strings

        Output:
        Their difference
    """

    list1 = str1.splitlines()
    list2 = str2.splitlines()

    for line in difflib.unified_diff(list1, list2, fromfile='Commited File', tofile='Staged File', lineterm=''):
        print(line)


def diff_util(blob_hash, file_path):
    """ 
        find the diff between commited file and the file in working directory

        Input:
        blob_hash = name of blob object
        file_path = name of file in working directory

        Output:
        Their differences
    """

    commit_obj_file = open('./.vcs/obj/'+blob_hash, 'rb').read()

    current_file = open(file_path, 'r').read()

    commit_obj_file = zlib.decompress(commit_obj_file)

    print("Difference:", file_path)

    diff_strstr(commit_obj_file, current_file)


def get_sha_from_index(filepath):
    with shelve.open(INDEX_PATH) as index:
        try:
            sha = index[filepath].sha
            return sha
        except KeyError:
            return

def diff(file_path):
    """ 
        Input:
        file or a directory

        print the diff of a file

        if the input is a directory, 
        print diff of all the file in that directory
        (recursive)
    """
    if os.path.isfile(file_path):
        commited_file_hash = get_sha_from_index(file_path)
        
        if(commited_file_hash == None):
            print("New file:", f)
        else:    
            diff_util(commited_file_hash, file_path)
    
    elif os.path.isdir(file_path):
        for filename in os.listdir(file_path):
            f = os.path.join(file_path, filename)
            
            if os.path.isfile(f):
                commited_file_hash = get_sha_from_index(f)
                if(commited_file_hash == None):
                    print("New file:", f)
                else:    
                    diff_util(commited_file_hash, f)
            
            elif os.path.isdir(f):
                diff(f)
            