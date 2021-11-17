import os
import shelve

# how does git add check for changes ?

vcs_base = '.temp/.vcs'


class Entry:
    def __init__(self, file_path, sha, stat):
        self.file_path = file_path
        self.sha = sha
        self.stat = stat


def stage(file_path):
    # create a blob object and find sha
    # {'sha256'} - compress
    # TODO: replace it with kshitiz's module
    sha = "some sha"
    mode = "some mode"

    entry = Entry(file_path, sha, os.stat(file_path))

    with shelve.open(os.path.join(vcs_base, 'index')) as index:
        index[file_path] = entry;


def get_entry(file_path):
    with shelve.open(os.path.join(vcs_base, 'index')) as index:
        return index[file_path]


def add(file_path):
    file_stat = os.stat(file_path)
    try:
        index_stat = get_entry(file_path).stat
        if file_stat == index_stat:
            return
    except KeyError:
        pass

    # if modified - create blob object of the file and add to staging area
    # stage(file_path)


if __name__ == '__main__':
    add('README.md')
    add('util.py')
    add('init.py')

    entry = get_entry('init.py')

    print(entry.sha)
    print(entry.file_path)
