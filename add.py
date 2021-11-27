"""FIXED"""
import os
import shelve
import util
from constants import VCS_DIR_NAME, INDEX_PATH


def stage(file_path, modified):
    # create a blob object
    sha = util.compress_file(file_path)['sha256']

    print(file_path)
    entry = util.Entry(file_path, sha, os.stat(file_path), modified)
    print("entry: ", entry)
    print(type(entry))

    with shelve.open(INDEX_PATH) as index:
        index[file_path] = entry


def add(path):
    print("path: ", path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            if filename != VCS_DIR_NAME:
                print("add file name: ", filename)
                add(os.path.join(path, filename))
    else:
        try:
            index_sha = util.get_entry_from_index(path).sha
            # print(index_sha)
            file_sha = util.compute_sha(path)
            # print(file_sha)
            modified = file_sha != index_sha
            print(modified)
            if not modified:
                return
        except AttributeError:
            modified = True

        # if modified - create blob object of the file and add to staging area
        stage(path, modified)
