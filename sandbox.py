# Given the list of strings in the Sample Input below, display the Sample Output in the console.

# Sample Input
# create file /home/jack/diary/2023-04-01.txt
# create file /home/jack/diary/2023-04-02.txt
# create file /home/jack/photos/1.jpg
# create file /home/jack/diary/2023-04-03.txt


# Sample Output
# - home
#   - jack
#     - diary
#       - 2023-04-01.txt
#       - 2023-04-02.txt
#     - photos
#       - 1.jpg


# class folder:
#     def __init__(self, name: str, child=None, Parent=None):
#         self.name: str = name
#         self.child: folder = child
#         self.Parent: folder = Parent


# def folder_structure(paths_list: str):
#     folder_structure_names_list = [i.split("/") for i in paths_list]
#     for path_list in folder_structure_names_list:
#         for indx, name in path_list[:-1]:
#             parent_folder = folder(path_list[indx - 1])
#             child_folder = folder(path_list[indx + 1])
#             current_folder = folder(name, child=child_folder, Parent=parent_folder)


# paths_list = [
#     "/home/jack/diary/2023-04-01.txt",
#     "/home/jack/diary/2023-04-02.txt",
#     "/home/jack/photos/1.jpg",
# ]
# print(folder_structure(paths_list))

# def create_directory_tree(file_paths):
#     directory_tree = {}
    
#     for file_path in file_paths:
#         path_components = file_path.split('/')
#         current_node = directory_tree
        
#         for component in path_components[1:]:
#             if component not in current_node:
#                 current_node[component] = {}
#             current_node = current_node[component]
    
#     return directory_tree

# def display_directory_tree(directory_tree, indentation=0):
#     for key, value in directory_tree.items():
#         print(" " * indentation + "- " + key)
#         display_directory_tree(value, indentation + 2)


from typing import List,Dict
def create_directory_tree(file_paths:List[str]) ->Dict:
    directory_tree={}
    file_paths=[i.split('/') for i in file_paths]
    for path_list in file_paths:
        current_dir=directory_tree
        for folder in path_list[1:]:
            if folder not in current_dir:
                current_dir[folder]={}
            current_dir=current_dir[folder]
    return directory_tree
def display_directory_tree(directory_tree :Dict, indentation=0) -> None: 
    for key,value in directory_tree.items():
        print(' '*indentation+'-'+key)
        display_directory_tree(value, indentation+2)
if __name__ == "__main__":
    file_paths = [
        "/home/jack/diary/2023-04-01.txt",
        "/home/jack/diary/2023-04-02.txt",
        "/home/jack/photos/1.jpg",
        "/home/jack/diary/2023-04-03.txt"]
    
    directory_tree = create_directory_tree(file_paths)
    display_directory_tree(directory_tree)
    
class folder:
    def __init__(self, name: str, child=None, Parent=None):
        self.name: str = name
        self.child: folder = child
        self.Parent: folder = Parent


def construct_folder_structure(paths_list: list):
    folder_structure_names_list = [i.split("/") for i in paths_list]
    root_folder = folder('-')  # Create a root folder to serve as the starting point of the tree

    folder_dict = {root_folder.name: root_folder}

    for path_list in folder_structure_names_list:
        current_folder = root_folder
        for name in path_list[1:]:
            if name not in folder_dict:
                # If the child folder doesn't exist, create a new one and link it to the current folder
                child_folder = folder(name, Parent=current_folder)
                folder_dict[name] = child_folder
                current_folder.child = child_folder
            else:
                child_folder = folder_dict[name]
                current_folder.child = child_folder

            current_folder = child_folder

    return root_folder
def display_folder_structure(folder_node, indentation=0):
    if folder_node is not None:
        print(" " * indentation + "- " + folder_node.name)
        display_folder_structure(folder_node.child, indentation + 2)
root_folder = construct_folder_structure(file_paths)
display_folder_structure(root_folder.child)