import os
from add import get_modified_enteries

# obj_directory = '.objs'
# cwd = ''
directory = ".vcs"
# cwd = os.getcwd()
# path = os.path.join(cwd, directory)

# obj_path = os.path.join(path, obj_directory)

# def initial_check():
#     #check if .vcs folder is present in the same directory
#     if(os.path.exists(path)):
#         os.chdir(path)

#         #check if objs folder present
#         if os.path.exists(obj_path):
#             os.chdir(obj_path)
#             commit_tree()
#     else:
#         print('first run init')


# entry = {
#     'mode' : '',
#     'name' : "",
#     "sha" : '',
#     'type' : ''
# }

# def helper2(filepath):
#     tree_entries = list()

#     for something in list(os.listdir(filepath)):
#         new_path = os.path.join(filepath, something)
#         if(os.path.isdir(new_path)):
#             entry = helper2(new_path)
#             entry['type'] = 'tree'
#             tree.append(entry)

#         elif(os.path.isfile(new_path)):
#             entry = addblob(new_path)
#             entry['type'] = 'blob'
#             tree.append(entry)

#     tree = dict()
#     tree['name'] = os.path.split(filepath)[1]
#     tree['entries'] = tree_entries
#     entry = add_blob(tree)
#     return entry


# get_staged_files
# {
# 'base':{
#     'files' : {'index.html',}   #set
#     'dirs':{
#         'lib':{
#             'files' : {}   #set
#               'dirs':{}
#         },
#         'lib2':{

#         }
#     }
# }
# }

cwd = os.getcwd()


def helper(staged_files:dict, tree_dict:dict, tree_path:str)->str:
    """[summary]

    Args:
        staged_files (dict): tree hierarchy directory structure object
        tree_dict (dict): [description]
        tree_path (str): file path

    Returns:
        str: returns the sha of the directory tree
    """
    tree = dict()
    tree["name"] = tree_dict["name"]
    tree_entries = []

    new_entries = set()

    for entry in tree_dict["entries"]:
        if entry["name"] in staged_files["dirs"].keys():
            sub_tree_dict = fetch_tree_dict(entry["sha"])
            # if not sub_tree_dict:
            #     sub_tree_dict = helper2(
            #         staged_files["dirs"][entry["name"]],
            #         os.path.join(tree_path, entry["name"]),
            #     )
            tree_obj = dict()
            tree_obj['sha'] = helper(
                staged_files["dirs"][entry["name"]],
                tree_dict,
                os.path.join(tree_path, entry["name"]),
            )
            tree_obj['mode'] = os.stat(os.path.join(cwd, tree_path)).st_mode
            tree_obj["type"] = "tree"
            tree_entries.append(tree_obj)
            new_entries.add(entry["name"])

        # elif entry["name"] in staged_files["files"].keys():
        #     # blob_obj = addblob(os.path.join(tree_path, entry["name"]))
        #     # blob_obj["type"] = "blob"
        #     blob_obj = dict()
        #     blob_obj["name"] = entry
        #     blob_obj["sha"] = staged_files["files"][entry].sha
        #     blob_obj["mode"] = staged_files["files"][entry].stat.st_mode
        #     blob_obj["type"] = "blob"
        #     tree_entries.append(blob_obj)
        #     new_entries.add(entry["name"])
            
        else:
            if os.path.isfile(os.path.join(cwd, tree_path)):
                blob_obj = dict()
                blob_obj["name"] = entry
                blob_obj["sha"] = staged_files["files"][entry].sha
                blob_obj["mode"] = staged_files["files"][entry].stat.st_mode
                blob_obj["type"] = "blob"
                tree_entries.append(blob_obj)
                new_entries.add(entry["name"])
            
            else:
                tree_obj = dict()
                tree_obj["sha"] = helper2(
                    staged_files["dirs"][entry], os.path.join(tree_path, entry)
                )
                tree_obj["type"] = "tree"
                tree_obj["mode"] = os.stat(os.path.join(cwd, tree_path)).st_mode
                tree_obj["name"] = os.path.split(tree_path)[1]
                
                tree_entries.append(tree_obj)
                new_entries.add(entry["name"])

    for entry in tree_dict["entries"]:
        if entry["name"] not in new_entries:
            tree_entries.append(entry)

    tree["entries"] = tree_entries

    return add_tree_obj(tree)


def helper2(staged_files: dict, tree_path: str) -> str:
    """[summary]

    Args:
        staged_files (dict): tree hierarchy directory structure object
        tree_path (str): file path

    Returns:
        str: returns the sha of the directory tree
    """
    tree = dict()
    tree["name"] = os.path.split(tree_path)[1]
    tree_entries = list()

    for entry in staged_files["dirs"].keys():
        tree_obj = dict()
        tree_obj["sha"] = helper2(
            staged_files["dirs"][entry], os.path.join(tree_path, entry)
        )
        tree_obj["type"] = "tree"
        tree_obj["mode"] = os.stat(os.path.join(cwd, tree_path)).st_mode
        tree_obj["name"] = os.path.split(tree_path)[1]

        tree_entries.append(tree_obj)

    for entry in staged_files["files"].keys():
        blob_obj = dict()
        blob_obj["name"] = entry
        blob_obj["sha"] = staged_files["files"][entry].sha
        blob_obj["mode"] = staged_files["files"][entry].stat.st_mode
        blob_obj["type"] = "blob"
        tree_entries.append(blob_obj)

    tree["entries"] = tree_entries

    return add_tree_obj(tree)


def helper3(staged_files: dict) -> str:
    """[summary]

    Args:
        staged_files (dict): tree hierarchy directory structure object

    Returns:
        str: returns the sha of the directory tree
    """
    tree_name = os.path.split(cwd)[1]
    return helper2(staged_files, tree_name)


def commit_tree():
    added_values = get_staged_tree()
    main_tree_sha = get_last_commit_tree()
    if main_tree_sha:
        main_tree = fetch_tree_dict(main_tree_sha)
        # if main_tree["name"] in added_values.keys():
        return helper(added_values[main_tree["name"]], main_tree, main_tree["name"])

    return helper3(added_values)


def get_staged_tree() -> dict:
    """Convert List of Entries to tree structure

    Returns:
        dict: modified/staged tree object
    """
    modified_entries = get_modified_enteries()
    if not modified_entries:
        return
    staged_tree = dict()
    common_object = {"files": None, "dirs": None}
    root_dir_name = os.path.split(cwd)[1]
    staged_tree[root_dir_name] = {**common_object}

    for entry in modified_entries:
        file_path_parts = os.path.normpath(entry.file_path).split(os.sep)
        curr_dir = staged_tree[root_dir_name]
        for part in file_path_parts[:-1]:
            if not curr_dir["dirs"]:
                curr_dir["dirs"] = dict()
            if part not in curr_dir["dirs"]:
                curr_dir["dirs"][part] = {**common_object}
            curr_dir = curr_dir["dirs"][part]

        if not curr_dir["files"]:
            curr_dir["files"] = dict()
        curr_dir["files"][file_path_parts[-1]] = entry

    return staged_tree


# def commit_tree():
# objs = os.listdir()
# if not objs:
#     #objs folder empty
#     print('nothing to commit')
#     return
