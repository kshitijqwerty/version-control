from hashlib import sha256
import pickle
import zlib
import commit_tree
import util
from constants import HEAD_PATH
import os


def commit_util(tree_hash, author_name, commiter_name, commit_message):
    '''
        input : hash of a tree

        tasks :
            1) create a new commit dict
                tree e1b3ec
                parent a11bef

                author Scott Chacon 
                    <schacon@gmail.com> 1205624433
                committer Scott Chacon 

                    <schacon@gmail.com> 1205624433
                my second commit, which is better than the first
            
            2) generate its hash

            3) compress it 

            4) store the compressed object in /obj

            5) update branch/main
    '''

    head = open('./.vcs/HEAD', 'r').read()
    prev_commit_hash = open('./.vcs/branch/' + head, 'r').read()

    commit_dict = {
        "tree": tree_hash,
        "author": author_name,
        "committer": commiter_name,
        "message": commit_message
    }

    if prev_commit_hash != "":
        commit_dict["parent"] = prev_commit_hash

    data = pickle.dumps(commit_dict)

    hash = sha256(data).hexdigest()

    c_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)

    commit_obj_file = open('./.vcs/obj/' + hash, 'wb')

    commit_obj_file.write(c_data)

    open('./.vcs/branch/' + head, 'w').write(hash)

    print(commit_dict)


# commit_util("1234asdf", "sarthak", "rawat", "my first commit")

def commit(author_first_name, author_last_name, commit_msg):
    sha = commit_tree.commit_tree()
    if sha is not None:
        commit_util(sha, author_first_name, author_last_name, commit_msg)


if __name__ == '__main__':
    first_name = "user1"
    last_name = "xyz"
    commit_msg = "First commit"

    print(util.get_modified_entries())
    commit(first_name, last_name, commit_msg)
