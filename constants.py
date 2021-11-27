import os

# CWD = os.path.join(os.getcwd(), '.temp')
# Fixed
CWD = ".temp"

VCS_DIR_NAME = '.vcs'
VCS_DIR_PATH = os.path.join(CWD, VCS_DIR_NAME)
INDEX_PATH = os.path.join(VCS_DIR_PATH, 'index')
OBJ_DIR = os.path.join(VCS_DIR_PATH, 'objects')
HEAD_PATH = os.path.join(VCS_DIR_PATH, 'HEAD')
REFS_DIR = os.path.join(VCS_DIR_PATH, 'refs')
BRANCH_DIR = os.path.join(REFS_DIR, 'branch')