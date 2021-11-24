import util


def checkout_util(tree):
    for entry in tree['entries']:
        print("tree entry: ", entry)
        file = util.decompress_file(entry['sha'])
        print(file)


def checkout(commit_hash):
    commit = util.decompress_commit(commit_hash)
    print("commit: ", commit)
    tree = util.decompress_tree(commit['tree'])
    print("tree: ", tree)
    checkout_util(tree)


if __name__ == '__main__':
    commit_hash = util.get_branch_content(util.get_head_content())
    checkout(commit_hash)
