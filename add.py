import os
import shelve
import util
import sys
from constants import VCS_BASE

# how does git add check for changes ?


# modified flag will be reset at commit


def stage(file_path, modified):
    # create a blob object
    sha = util.compress_file(file_path)['sha1']

    entry = util.Entry(file_path, sha, os.stat(file_path), modified)
    print("entry: ", entry)
    print(type(entry))

    with shelve.open(os.path.join(VCS_BASE, 'index')) as index:
        index[file_path] = entry


def get_entry(file_path):
    with shelve.open(os.path.join(VCS_BASE, 'index')) as index:
        return index[file_path]


# def get_modified_enteries():
#     with shelve.open(os.path.join(VCS_BASE, 'index')) as index:
#         modified_enteries = []
#         for key in index.keys():
#             entry = index[key]
#             if entry.modified:
#                 modified_enteries.append(entry)
#     return modified_enteries


def add(file_path):
    file_stat = os.stat(file_path)
    modified = False
    try:
        index_stat = get_entry(file_path).stat
        modified = file_stat != index_stat
        if not modified:
            return
    except KeyError:
        modified = True

    # if modified - create blob object of the file and add to staging area
    stage(file_path, modified)


if __name__ == '__main__':
    fpath = sys.argv[1]
    add(fpath)

    print(util.get_modified_entries())
