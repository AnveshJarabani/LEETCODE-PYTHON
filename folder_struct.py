file_paths = [
    "/home/jack/diary/2023-04-01.txt",
    "/home/jack/diary/2023-04-02.txt",
    "/home/jack/photos/1.jpg",
    "/home/dack/diary/2023-04-03.txt",
    "/gome/back/biry/xly.txt"
]

from typing import List
class Node:
    def __init__(self,name=None,folders={},files=[]):
        self.name:str=name
        self.folders:dict[str,Node]={}
        self.files:List[str] = []
    def add_folders(self,path_list:List[str]):
        cur_node=self
        for folder in path_list:
            if folder not in cur_node.folders:
                cur_node.folders[folder]=Node()
            cur_node=cur_node.folders[folder]
    def add_files(self,folder_list,file:str):
        cur_node=self
        for folder in folder_list:
            if folder not in cur_node.folders:
                cur_node.folders[folder]=Node()
            cur_node=cur_node.folders[folder]
        cur_node.files.append(file)
    def print_tree(self,cur_node,indent=0):
        if not cur_node:
            return
        for folder_name,folder in cur_node.folders.items():
            print(' '*indent+f'-{folder_name}')
            self.print_tree(folder,indent+1)
        for file in cur_node.files:
            print(' '*(indent+1)+f'-{file}')
tree=Node()
for i in file_paths:
    folders=i.split('/')[1:]
    file=folders.pop()
    tree.add_folders(folders)
    tree.add_files(folders,file)
tree.print_tree(tree)

    
    