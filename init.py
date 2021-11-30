import os
import constants as const


def init():
    try:
        os.mkdir(const.VCS_DIR_PATH)
        os.mkdir(const.OBJ_DIR)
        os.mkdir(const.REFS_DIR)
        os.mkdir(const.BRANCH_DIR)

        main_branch_path = os.path.join(const.BRANCH_DIR, 'main')

        with open(main_branch_path, 'w') as branch:
            pass

        with open(const.HEAD_PATH, "w") as head:
            head.write("main")
    except FileExistsError:
        pass
