import os

VCS_FOLDER = '.vcs'
VCS_BASE = os.path.join('.temp', VCS_FOLDER)
CWD = os.path.join(os.getcwd(), '.temp')
INDEX_PATH = os.path.join(VCS_BASE, 'index')
OBJ_DIR = os.path.join(VCS_BASE, 'objects')
HEAD_PATH = os.path.join(VCS_BASE, 'HEAD')
REFS_DIR = os.path.join(VCS_BASE, 'refs')
BRANCH_DIR = os.path.join(REFS_DIR, 'branch')