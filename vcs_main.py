import sys

from add import add
from checkout import checkout
from commit import commit
from diff_util import diff
from init import init
from log_util import log


def main():
    try:
        cmmnd = sys.argv[1]

        if cmmnd == "init":
            init(sys.argv[2])

        elif cmmnd == "add":
            add(sys.argv[2])

        elif cmmnd == "commit":
            commit(commit_msg=sys.argv[2])

        elif cmmnd == "diff":
            diff(sys.argv[2])

        elif cmmnd == "log":
            log()

        elif cmmnd == "checkout":
            checkout(sys.argv[2])

    except IndexError:
        print("Invalid no of args")
        return


if __name__ == "__main__":
    main()