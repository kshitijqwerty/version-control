""" Display the commits from the latest commit to the first commit """

from constants import OBJ_DIR, BRANCH_DIR, HEAD_PATH
from hashlib import sha256 
import pickle
import zlib
import os

class ANSI():
	def background(code):
		return "\33[{code}m".format(code=code)

	def style_text(code):
		return "\33[{code}m".format(code=code)

	def color_text(code):
		return "\33[{code}m".format(code=code)

def print_red(message):
    encoding = ANSI.background(1) + ANSI.color_text(49) + ANSI.style_text(31) + message
    encoding +=  ANSI.background(0) + ANSI.color_text(0) + ANSI.style_text(0)
    print(encoding)

def print_green(message):
    encoding = ANSI.background(1) + ANSI.color_text(49) + ANSI.style_text(32) + message
    encoding +=  ANSI.background(0) + ANSI.color_text(0) + ANSI.style_text(0)
    print(encoding)

def print_commit_log(commit_obj, commit_hash):
    print_red("LOG:" + commit_hash)
    print_green("tree:" + commit_obj["tree"])
    try:
        print_green("parent:" + commit_obj["parent"])
    except KeyError:
        pass
    print_green("author:" + commit_obj["author"])
    print_green("committer:" + commit_obj["committer"])
    print_green("message:" + commit_obj["message"] + "\n")


def log_util(commit_hash):
    if commit_hash == "":
        return
    
    with open(os.path.join(OBJ_DIR, commit_hash), "rb") as f:
        commit_obj = f.read()
        commit_obj = zlib.decompress(commit_obj)
        commit_obj = pickle.loads(commit_obj)

        print_commit_log(commit_obj, commit_hash)

        try:
            commit_hash = commit_obj["parent"]
            log_util(commit_hash)
        except KeyError:
            pass

def log():
    head = ""
    commit_hash = ""

    with open(HEAD_PATH) as head_file:
        head = head_file.read()
    
    with open(os.path.join(BRANCH_DIR, head)) as branch_file:
        commit_hash = branch_file.read()
    
    print_red("Head:" + head + "\n")

    log_util(commit_hash)

log()
