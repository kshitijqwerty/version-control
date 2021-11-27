import sys

from add import add
from checkout import checkout
from commit import commit
from diff_util import diff
from init import init
from log_util import log
from pull import pull_from_remote
from push import push_to_remote
from status_util import status
from rollback import rollback
from branch import create_branch
from constants import CWD
import os


def main():
    try:
        cmmnd = sys.argv[1]

        if cmmnd == "init":
            init(CWD)

        elif cmmnd == "add":
            add(os.path.normpath(sys.argv[2]))

        elif cmmnd == "commit":
            commit(commit_msg=sys.argv[2])

        elif cmmnd == "diff":
            diff(os.path.normpath(sys.argv[2]))

        elif cmmnd == "log":
            log()

        elif cmmnd == "checkout":
            checkout(os.path.normpath(sys.argv[2]))
        
        elif cmmnd == "pull":
            pull_from_remote(os.path.normpath(sys.argv[2]))
        
        elif cmmnd == "push":
            push_to_remote(os.path.normpath(sys.argv[2]))
        
        elif cmmnd == "status":
            status()
        
        elif cmmnd == "rollback":
            rollback()

        elif cmmnd == "branch":
            create_branch(os.path.normpath(sys.argv[2]))


    except IndexError:
        print("Invalid no of args")
        return


if __name__ == "__main__":
    main()
