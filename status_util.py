""" Display the status of files; Tracked, Untracked, Tracked and Modified """
import util
from constants import VCS_DIR_NAME, CWD
import os
from io_util import print_purple, print_red, print_green, print_yellow

tracked = []
tracked_modified = []
untracked = []


def status_util(file_path):

    if os.path.isfile(file_path):
        # modified_status = get_modified_status(file_path)
        print(file_path)
        index_file_sha = util.get_sha_from_index(file_path)
        # print("status util index file sha: ", index_file_sha)
        # print(index_file_sha)
        if index_file_sha is None:
            untracked.append(file_path)
        else:
            file_sha = util.compute_sha(file_path)
            print("status util file sha", file_sha)
            if file_sha != index_file_sha:
                tracked_modified.append(file_path)
            else:
                tracked.append(file_path)

    elif os.path.isdir(file_path):
        for file_name in os.listdir(file_path):
            if file_name != VCS_DIR_NAME:
                status_util(os.path.join(file_path, file_name))


def status():
    status_util(CWD)

    print_purple("STATUS")
    print_green("HEAD: " + util.get_head_content())

    if len(tracked) != 0:
        print_purple("\nTracked files:")
        for file in tracked:
            print_green(file)

    if len(tracked_modified) != 0:
        print_purple("\nModified files:")
        for file in tracked_modified:
            print_red(file)

    if len(untracked) != 0:
        print_purple("\nUntracked files:")
        for file in untracked:
            print_yellow(file)
