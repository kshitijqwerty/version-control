""" Display the status of files; Tracked, Untracked, Tracked and Modifyed """
import shelve
import sys

import util
from constants import OBJ_DIR, BRANCH_DIR, HEAD_PATH, INDEX_PATH, VCS_FOLDER
from hashlib import sha256
import difflib
import pickle
import zlib
import os

def get_modified_status(filepath):
    with shelve.open(INDEX_PATH) as index:
        try:
            return index[filepath].modified
        except KeyError:
            return

tracked = []
tracked_modified = []
untracked = []

def status_util(file_path):
    if os.path.isfile(file_path):
        modified_status = get_modified_status(file_path)
        index_file_sha = util.get_sha_from_index(file_path)
        if index_file_sha == None:
            untracked.append(file_path)
        else:
            file_sha = util.get_sha(file_path)
            if file_sha != index_file_sha:
                tracked_modified.append(file_path)
            else:
                tracked.append(file_path)
    
    elif os.path.isdir(file_path):
        for file_name in os.listdir(file_path):
            if file_name != VCS_FOLDER:
                status_util(os.path.join(file_path, file_name))


def status():
    status_util("./.temp")


    print("Untracked files")
    print(untracked)

    print("Tracked files")
    print(tracked)

    print("Tracked but modifyed files")
    print(tracked_modified)


if __name__ == "__main__":
    status()

    
    